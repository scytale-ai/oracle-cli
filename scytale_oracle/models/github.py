import os
from datetime import datetime, timedelta

import pandas as pd
from github import Github
from github import Repository

from .integration import Integration

GITHUB_TOKEN_ENV_VAR_NAME = 'GITHUB_TOKEN'


class GithubIntegration(Integration):
    """ github integration to work with the 3rd party service github """

    def __init__(self, organization):
        Integration.__init__(self, 'GitHub')
        self.organization = organization

    def _get_auth_obj(self):
        """ get authentication object for GitHub from environment variable """
        try:
            api_token = os.environ[GITHUB_TOKEN_ENV_VAR_NAME]
            return Github(api_token)
        except KeyError:
            raise RuntimeError(
                f"Authentication Failed - please provide your personal github token as an environment variable named '{GITHUB_TOKEN_ENV_VAR_NAME}'")

    def __get_repo(self, repo_name) -> Repository.Repository:
        """ get repo object """
        search_res = self._auth_obj.search_repositories(query=f'org:{self.organization} {repo_name}')
        return search_res[0]

    def __get_all_repos(self):
        """ get all repo objects in the given organization """
        repos = []
        _repos = self._auth_obj.search_repositories(query=f'org:{self.organization}')
        for repo in _repos:
            repos.append(repo)
        return repos

    def get_all_repo_names(self):
        """List Repositories"""
        github_repos = []
        repos = self.__get_all_repos()
        for repo in repos:
            github_repos.append(repo.full_name)
        return pd.DataFrame(
            {
                'repo_name': github_repos,
                'severity': [3] * len(github_repos)
            }
        )

    def get_repo_branch_protection_status(self, repo_name):
        """Get Repository Branch Protection Status"""
        branch_names = []
        protection_statuses = []
        severities = []
        repo = self.__get_repo(repo_name)
        for branch in repo.get_branches():
            severity = 0
            protection_status = branch.protected
            if not protection_status:
                severity = 2
            branch_names.append(branch.name)
            protection_statuses.append(protection_status)
            severities.append(severity)
        return pd.DataFrame(
            {
                'github_repo': [repo.name] * len(branch_names),
                'branch_name': branch_names,
                'is_protected': protection_statuses,
                'severity': severities
            }
        )

    def get_all_users_repo_permissions(self):
        """Get All Users Repositories Permissions"""
        repo_names = []
        usernames = []
        permissions = []
        severities = []

        organization = self._auth_obj.get_organization(self.organization)
        repos = self.__get_all_repos()
        for member in organization.get_members():
            print(f' - getting repository permissions for {member.login}')
            for repo in repos:
                permission = repo.get_collaborator_permission(member.login)
                severity = 0
                if permission == 'write':
                    severity = 1
                elif permission == 'admin':
                    severity = 2
                severities.append(severity)
                usernames.append(member.login)
                repo_names.append(repo.name)
                permissions.append(permission)
        return pd.DataFrame({
            'repo_name': repo_names,
            'username': usernames,
            'permission': permissions,
            'severity': severities
        })

    def get_user_repos_permissions(self, username):
        """Get User's Repositories Permissions"""
        severities = []
        repo_names = []
        permissions = []
        repos = self.__get_all_repos()
        for repo in repos:
            permission = repo.get_collaborator_permission(username)
            severity = 0
            if permission == 'write':
                severity = 1
            elif permission == 'admin':
                severity = 2
            severities.append(severity)
            repo_names.append(repo.name)
            permissions.append(permission)
        return pd.DataFrame({
            'repo_name': repo_names,
            'permission': permissions,
            'severity': severities
        })

    def list_prs(self):
        """List Pull Requests from the Past 24hrs"""
        repos = self.__get_all_repos()
        all_pulls = []
        pulls_repos = []
        for repo in repos:
            print(f' - getting PRs from repo {repo.name}')
            pulls = repo.get_pulls()
            for pull in pulls:
                now = datetime.now()
                yesterday = now - timedelta(hours=24)
                if pull.created_at >= yesterday:
                    pulls_repos.append(repo.name)
                    all_pulls.append(pull)

        return pd.DataFrame({
            'title': map(lambda pr: pr.title, all_pulls),
            'repo': pulls_repos,
            'severity': [3] * len(all_pulls)
        })
