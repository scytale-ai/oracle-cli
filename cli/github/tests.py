import inquirer
import time
from ..utils import get_loader, get_success_message, get_failure_message


def test_example(test_name, success):
    spinner = get_loader(f"Running test {test_name}")
    spinner.start()
    time.sleep(2)
    spinner.stop()
    if success:
        get_success_message(f"{test_name} ran successfully")
    else:
        get_failure_message(f"{test_name} run failed")


def test_a():
    test_example("A", True)


def test_b():
    test_example("B", False)


github_tests = {
    'A': test_a,
    'B': test_b
}

github_choices = github_tests.keys()


def run_github_test(test_name):
    if test_name in github_tests:
        github_tests[test_name]()
    else:
        print("Invalid test name")


def select_github_test():
    questions = [
        inquirer.List('test_name',
                      message="Which GitHub test would you like to run?",
                      choices=github_choices,
                      carousel=True
                      ),
    ]
    answers = inquirer.prompt(questions)
    run_github_test(answers['test_name'])
