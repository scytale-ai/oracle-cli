from halo import Halo
from colored import stylize, fg, bg, attr


def get_loader(text):
    return Halo(text=text, spinner="dots")


check_mark = stylize('\u2713', fg(10) + attr(1))

failure_x = stylize('\u2716', fg(9) + attr(1))


def get_success_message(success_text):
    return f"{check_mark} {success_text}"


def get_failure_message(failure_text):
    return f"{failure_x} {failure_text}"


scytale_colored_squares = stylize('\u25A0', fg('#DD4973')) + stylize('\u25A0', fg('#F7BE33')) + stylize('\u25A0',
                                                                                                        fg('#60C9E2'))

scytale_message = stylize(
    "\nWant to pass a SOC2 audit? For our complete compliance automation platform check us out! https://scytale.ai",
    bg(91)) + " " + scytale_colored_squares
