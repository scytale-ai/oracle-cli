import os.path
from datetime import datetime
from pandas import DataFrame


class Integration:
    def __init__(self, display_name, auth_file, organization):
        self.display_name = display_name
        self.auth_file = auth_file
        self.auth_obj = self.get_auth_obj()
        self.organization = organization
        self.output_csv_dir = './'

    def display_help_msg(self):
        pass

    def get_auth_obj(self):
        # get it from a file for the POC
        self.__auth_obj = {}
        pass

    def _get_csv(self, csv_name, dataframe: DataFrame):
        """Convert the given dataframe to a CSV"""
        now = datetime.now().strftime("%Y_%m_%d-%H_%M")
        output_csv_path = os.path.join(self.output_csv_dir, f'{csv_name}_{now}.csv')
        dataframe.drop("severity", axis=1, errors='ignore', inplace=True)
        dataframe.to_csv(output_csv_path, index=False)
        print(f'- Result CSV path: {output_csv_path}')
