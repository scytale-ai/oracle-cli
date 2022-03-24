import inspect
import inquirer
from cli.utils import get_loader, get_success_message, get_failure_message


class TestSuite:
    def __init__(self, integration_instance):
        self.integration = integration_instance
        self.methods = inspect.getmembers(integration_instance, predicate=inspect.ismethod)

        self.tests = {}
        self.test_args = []

        for method in self.methods:
            method_name = method[0]
            method_display_name = method[1].__doc__
            if method_display_name:
                self.test_args.append(method_name)
                self.tests[method_display_name] = method[1]

        self.test_names = self.tests.keys()

    def get_test_name(self, method_name):
        for method in self.methods:
            if method[0] == method_name:
                return method[1].__doc__

    def run_test(self, test_name):
        """Run Test"""
        if test_name in self.tests:
            success = True
            spinner = get_loader(f"Running test: {test_name}" + "\n")

            try:
                test = self.tests[test_name]
                test_signature = inspect.signature(test).parameters.keys() or []

                results = None
                if len(test_signature) == 0:
                    spinner.start()
                    results = test()
                else:
                    args = []
                    print("This test needs some inputs.\n")
                    for arg in test_signature:
                        value = input(f"{arg}: ")
                        args.append(value)

                    spinner.start()
                    results = test(*args)

                spinner.stop()
                print(results)
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

    def select_test(self):
        questions = [
            inquirer.List('test_name',
                          message=f"Which {self.integration.display_name} test would you like to run?",
                          choices=self.test_names,
                          carousel=True
                          ),
        ]
        answers = inquirer.prompt(questions)
        self.run_test(answers['test_name'])
