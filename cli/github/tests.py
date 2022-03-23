import inquirer
import time
import inspect
from cli.utils import get_loader, get_success_message, get_failure_message
from models.github import GithubIntegration


def test_a():
    print("Doing some stuff...")


github_tests = {
    'A': test_a,
}

github_methods = inspect.getmembers(GithubIntegration(), predicate=inspect.ismethod)

for method in github_methods:
    method_name = method[1].__doc__
    if method_name:
        github_tests[method_name] = method[1]

github_choices = github_tests.keys()


def run_github_test(test_name):
    if test_name in github_tests:
        success = True
        spinner = get_loader(f"Running test: {test_name}" + "\n")
        spinner.start()
        time.sleep(2)
        spinner.stop()

        try:
            github_tests[test_name]()
        except Exception:
            success = False
            raise
        finally:
            if success:
                print(get_success_message(f"{test_name} ran successfully"))
            else:
                print(get_failure_message(f"{test_name} run failed"))

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
