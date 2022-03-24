
class Integration:
    def __init__(self, display_name, auth_file, organization):
        self.display_name = display_name
        self.auth_file = auth_file
        self.auth_obj = self.get_auth_obj()
        self.organization = organization

    def get_auth_obj(self):
        # get it from a file for the POC
        self.__auth_obj = {}
        pass

