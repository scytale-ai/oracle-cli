class Integration:
    def __init__(self, display_name, auth_file):
        self.display_name = display_name
        self.auth_file = auth_file
        self._auth_obj = self._get_auth_obj()

    def _get_auth_obj(self):
        # get it from a file for the POC
        self._auth_obj = {}
