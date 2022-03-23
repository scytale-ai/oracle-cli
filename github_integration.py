from integration import Intgration
from github import Github, Repository
import pandas as pd


class GithubIntegration(Intgration):
    def __init__(self, auth_file, organization):
        super().__init__()
        self.auth_file = auth_file
        self.auth_obj = self.get_auth_obj()
        self.organization = organization

    def display_help_msg(self):
        print('Github Integration - Fixme, maybe remove this?')

    def get_auth_obj(self):
        with open(self.auth_file, 'r') as f:
            api_token = f.read().strip()
        return Github(api_token)

    def __get_repo(self, repo_name) -> Repository.Repository:
        """ get github repo object """
        search_res = self.auth_obj.search_repositories(query=f'org:{self.organization} {repo_name}')
        return search_res[0]

    def __get_all_repos(self):
        """ get all repo objects in the given organization """
        repos = []
        _repos = self.auth_obj.search_repositories(query=f'org:{self.organization}')
        for repo in _repos:
            repos.append(repo)
        return repos

    def get_all_repo_names(self):
        """ get all repositories names in the given organization """
        github_repos = []
        repos = self.__get_all_repos()
        for repo in repos:
            github_repos.append(repo.full_name)
        return pd.DataFrame(
            {
                'repo_name': github_repos
            }
        )

    def get_repo_branch_protection_status(self, repo_name):
        """ get all the repo's brnanches protection status """
        branch_names = []
        protection_statuses = []
        repo = self.__get_repo(repo_name)
        for branch in repo.get_branches():
            branch_names.append(branch.name)
            protection_statuses.append(branch.protected)
        return pd.DataFrame(
            {
                'github_repo': [repo.name] * len(branch_names),
                'branch_name': branch_names,
                'is_protected': protection_statuses
            }
        )

    def get_all_users_repo_permissions(self):
        """ get all the given organization repo permissions of all users """
        repo_names = []
        usernames = []
        permissions = []
        organization = self.auth_obj.get_organization(self.organization)
        repos = self.__get_all_repos()
        for member in organization.get_members():
            print(f'- getting repository permissions for {member.login}')
            for repo in repos:
                usernames.append(member.login)
                repo_names.append(repo.name)
                permissions.append(repo.get_collaborator_permission(member.login))
        return pd.DataFrame({
            'repo_name': repo_names,
            'username': usernames,
            'permission': permissions
        })

    def get_user_repos_permissions(self, username):
        """ get the given user's permissions on all of the organization's repositories """
        repo_names = []
        permissions = []
        repos = self.__get_all_repos()
        for repo in repos:
            repo_names.append(repo.name)
            permissions.append(repo.get_collaborator_permission(username))
        return pd.DataFrame({
            'repo_name': repo_names,
            'permission': permissions
        })

    def get_prs(self):
        pass

    def check_cr_enforce_on_repos(self):
        pass


if __name__ == '__main__':
    gi = GithubIntegration(auth_file='/home/evoosa/secrets/github_token', organization='scytale-ai')
    print(gi.get_user_repos_permissions('evoosa'))
