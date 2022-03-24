from halo import Halo
from colored import stylize, fg, attr
import os
from datetime import datetime
from pandas import DataFrame

DEFAULT_OUTPUT_CSV_DIR = './'


def get_loader(text):
    return Halo(text=text, spinner="dots")


check_mark = stylize('\u2713', fg(10) + attr(1))

failure_x = stylize('\u2716', fg(9) + attr(1))


def get_success_message(success_text):
    return f"{check_mark} {success_text}"


def get_failure_message(failure_text):
    return f"{failure_x} {failure_text}"


def convert_dataframe_to_csv(dataframe: DataFrame):
    """Convert the given dataframe to a CSV"""
    now = datetime.now().strftime("%Y_%m_%d-%H_%M")
    output_csv_path = os.path.join(DEFAULT_OUTPUT_CSV_DIR, f'results_{now}.csv')
    dataframe.drop("severity", axis=1, errors='ignore', inplace=True)
    dataframe.to_csv(output_csv_path, index=False)
    print(f'- Result CSV path: {output_csv_path}')
