from halo import Halo
from colored import stylize, fg, attr
import os
from datetime import datetime
from pandas import DataFrame

PREFIX_SYMBOLS = {
    0: stylize('\u2713', fg(10) + attr(1)),  # GREEN V
    1: stylize('~', fg(3) + attr(1)),  # YELLOW ~
    2: stylize('\u2716', fg(9) + attr(1)),  # RED X
    4: ''
}

DEFAULT_OUTPUT_CSV_DIR = './'


def get_loader(text):
    return Halo(text=text, spinner="dots")


def print_formatted_line(line_text, prefix_symbol):
    """Print the Given line with the given symbol as a prefix"""


def get_success_message(success_text):
    return f"{PREFIX_SYMBOLS[0]} {success_text}"


def get_failure_message(failure_text):
    return f"{PREFIX_SYMBOLS[1]} {failure_text}"


def convert_dataframe_to_csv(dataframe: DataFrame):
    """Convert the given dataframe to a CSV"""
    now = datetime.now().strftime("%Y_%m_%d-%H_%M")
    output_csv_path = os.path.join(DEFAULT_OUTPUT_CSV_DIR, f'results_{now}.csv')
    dataframe.drop("severity", axis=1, errors='ignore', inplace=True)
    dataframe.to_csv(output_csv_path, index=False)
    print(f'- Result CSV path: {output_csv_path}')


def pretty_print_dataframe(dataframe: DataFrame):
    """Pretty print the given DataFrame"""
    for row in dataframe.iterrows():
        row_data = row[1]
        severity = 4
