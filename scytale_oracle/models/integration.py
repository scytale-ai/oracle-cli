class Integration:
    """ integration to work with a 3rd party service """
    def __init__(self, display_name):
        self.display_name = display_name
        self._auth_obj = self._get_auth_obj()

    def _get_auth_obj(self):
        """ Get an authentication object for the integration to work with a 3rd party service """
        self._auth_obj = {}
