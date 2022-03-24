import argparse
from models.github import GithubIntegration
from models.test_suite import TestSuite

github_test_suite = TestSuite(GithubIntegration())


def init_cli():
    parser = argparse.ArgumentParser(description="Scytale compliance CLI")

    parser.add_argument('--github', nargs="*", help="Run GitHub tests",
                        choices=github_test_suite.choices)
    parser.add_argument('--aws', nargs="*", help="Run AWS tests",
                        choices=github_test_suite.choices)
    parser.add_argument('--disconnect', action="store_true", help="Disconnect from github")  # Deleted tokens.

    return parser.parse_args()


def run_integration_operations(integration_args, integration_name):
    test_suite = {}
    if integration_name == 'github':
        test_suite = github_test_suite

    if integration_args is not None and test_suite is not None:
        # TODO - Check if authenticated
        if not integration_args:
            test_suite.select_test()
        else:
            test_name = integration_args[0]

            test_suite.run_test(test_name)


def run_cli():
    args = init_cli()

    if args.github is not None:
        run_integration_operations(args.github, 'github')

    elif args.aws is not None:
        run_integration_operations(args.aws, 'aws')

    elif args.disconnect:
        print('Disconnected from integration...')
