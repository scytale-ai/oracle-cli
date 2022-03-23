import inquirer


def test_a():
    print('running test a')


def run_github_test(test_name):
    tests = {
        'a': test_a
    }

    if test_name in tests:
        tests[test_name]()
    else:
        print("Invalid test name")


def select_github_test():
    questions = [
        inquirer.List('test_name',
                      message="Which GitHub test would you like to run?",
                      choices=['a', 'b', 'c'],
                      ),
    ]
    answers = inquirer.prompt(questions)
    print(answers)
    run_github_test(answers['test_name'])
