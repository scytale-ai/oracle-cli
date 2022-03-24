from halo import Halo
from colored import stylize, fg, attr, bg
import os
from datetime import datetime
from pandas import DataFrame
from termcolor import colored, cprint

PREFIX_SYMBOLS = {
    0: stylize('\u2713', fg(10) + attr(1)),  # GREEN V
    1: stylize('~', fg(3) + attr(1)),  # YELLOW ~
    2: stylize('\u2716', fg(9) + attr(1)),  # RED X
}

SEVERITY_COLORS = {
    0: 'green',
    1: 'yellow',
    2: 'red',
    3: 'white'
}

DEFAULT_OUTPUT_CSV_DIR = './'
MAX_COLUMN_WIDTH = 30

scytale_colored_squares = stylize('\u25A0', fg('#DD4973')) + stylize('\u25A0', fg('#F7BE33')) + stylize('\u25A0', fg('#60C9E2'))
scytale_message = stylize(
    "\nWant to pass a SOC2 audit? For our complete compliance automation platform check us out! https://scytale.ai",
    fg(13)) + " " + scytale_colored_squares


def get_loader(text):
    return Halo(text=text, spinner="dots")


def get_success_message(success_text):
    return f"{PREFIX_SYMBOLS[0]} {success_text}"


def get_failure_message(failure_text):
    return f"{PREFIX_SYMBOLS[2]} {failure_text}"


def convert_dataframe_to_csv(dataframe: DataFrame):
    """Convert the given dataframe to a CSV"""
    now = datetime.now().strftime("%Y_%m_%d-%H_%M")
    output_csv_path = os.path.join(DEFAULT_OUTPUT_CSV_DIR, f'results_{now}.csv')
    dataframe.drop("severity", axis=1, errors='ignore', inplace=True)
    dataframe.to_csv(output_csv_path, index=False)
    print(f'- Result CSV path: {output_csv_path}')


def pretty_print_dataframe(dataframe: DataFrame):
    """Pretty print the given DataFrame"""
    headers = list(dataframe.columns)
    headers.remove('severity')
    header_str = ''
    for col_name in headers:
        header_str += str(col_name).ljust(MAX_COLUMN_WIDTH, ' ')[:MAX_COLUMN_WIDTH] + " "
    print(header_str)

    for row in dataframe.iterrows():
        row_dict = row[1].to_dict()
        fmt_row = ''
        for key in row_dict.keys():
            if key != 'severity':
                attr = row_dict[key]
                fmt_row += str(attr).ljust(MAX_COLUMN_WIDTH, ' ')[:MAX_COLUMN_WIDTH] + " "
        if row_dict['severity'] == 3:
            print(fmt_row)
        else:
            cprint(colored(fmt_row, SEVERITY_COLORS[row_dict['severity']]))
