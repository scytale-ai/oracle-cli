from .integration import Integration


class GithubIntegration(Integration):
    def __init__(self):
        Integration.__init__(self, 'GitHub')

    def get_mfa_users(self):
        """Get MFA Users"""
        print('here you go')

    def display_help_msg(self):
        """Display Help Message"""
        print('help me')
