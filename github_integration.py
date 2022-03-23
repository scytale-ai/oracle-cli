from integration import Intgration
from github import Github, Repository
import pandas as pd


class GithubIntegration(Intgration):
    def __init__(self, auth_file, organization):
        super().__init__()
        self.auth_file = auth_file
        self.auth_obj = self.get_auth_obj()
        self.organization = organization  # FIXME - all of them

    def display_help_msg(self):
        print('Github Integration - Fixme, maybe remove this?')

    def get_auth_obj(self):
        with open(self.auth_file, 'r') as f:
            api_token = f.read().strip()
        return Github(api_token)

    def get_users_permissions(self):
        pass

    def _get_repo(self, repo_name) -> Repository.Repository:
        search_res = self.auth_obj.search_repositories(query=f'org:{self.organization} {repo_name}')
        return search_res[0]

    def get_all_repo_names(self):
        github_repos =[]
        repos = self.auth_obj.search_repositories(query=f'org:{self.organization}')
        for repo in repos:
            github_repos.append(repo.full_name)
        return pd.DataFrame(
            {
                'repo_name': github_repos
             }
        )

    def get_repo_branch_protection_status(self, repo_name):
        repo = self._get_repo(repo_name)
        branch_names = []
        protection_statuses = []
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

    def get_prs(self):
        pass

    def check_cr_enforce_on_repos(self):
        pass


if __name__ == '__main__':
    gi = GithubIntegration(auth_file='/home/evoosa/secrets/github_token', organization='scytale-ai')
    print(gi._())
