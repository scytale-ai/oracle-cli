import inspect
import inquirer
from ..cli.utils import get_loader, get_success_message, get_failure_message, scytale_message, pretty_print_dataframe


class TestSuite:
    def __init__(self, integration_instance):
        self.integration_class = integration_instance
        self.methods = self._get_integration_methods()
        self.tests_display_names = self._get_tests_display_names()

    def check_test_existance(self, test_name):
        """ check if the given test exists in the integration class """
        valid_test_names = self.methods.keys()
        if test_name not in valid_test_names:
            print(f'"{test_name}" is an invalid test! please choose one of: {list(valid_test_names)}')
            exit(1)

    def _get_integration_methods(self) -> dict:
        """ get all the integration's methods """
        integration_methods = inspect.getmembers(self.integration_class, predicate=inspect.ismethod)
        return {method[0]: method[1] for method in integration_methods if not method[0].startswith('_')}

    def _get_tests_display_names(self) -> dict:
        """ get a mapping between the test's display names, and the test's method name """
        return {method_obj[1].__doc__: method_obj[0] for method_obj in self.methods.items()}

    def run_test(self, test_name):
        """ run a test if exists, given it's name"""
        self.check_test_existance(test_name)
        test_display_name = dict((new_val, new_k) for new_k, new_val in self.tests_display_names.items()).get(test_name)
        success = True
        spinner = get_loader(f"Running test: {test_display_name}" + "\n")
        try:
            test = self.methods[test_name]
            test_arguments = inspect.signature(test).parameters.keys() or []

            # get arguments if needed
            if len(test_arguments) == 0:
                spinner.start()
                results = test()
            else:
                args = []
                print("This test needs some inputs.\n")
                for arg in test_arguments:
                    value = input(f"{arg}: ")
                    args.append(value)
                spinner.start()
                results = test(*args)

            # if the severity of one of the results is too high, mark the test as failed
            if 'severity' in results.keys():
                for sev in results['severity'].values:
                    if sev == 2:
                        success = False
                        break

            spinner.stop()
            pretty_print_dataframe(results)
            return results
        except Exception:
            success = False
            raise
        finally:
            print("\n")
            if success:
                print(get_success_message(f"{test_display_name} ran successfully"))
            else:
                print(get_failure_message(f"{test_display_name} run failed"))

            print(scytale_message)

    def select_test(self):
        """ give the user the option to select a test to run, and run it """
        questions = [
            inquirer.List('test_name',
                          message=f"Which {self.integration_class.display_name} test would you like to run?",
                          choices=self.tests_display_names,
                          carousel=True
                          ),
        ]
        answers = inquirer.prompt(questions)
        result = self.run_test(self.tests_display_names[answers['test_name']])
        return result
