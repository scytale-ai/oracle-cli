import argparse
from models.github import GithubIntegration
from models.test_suite import TestSuite
from .utils import convert_dataframe_to_csv

github_test_suite = TestSuite(GithubIntegration(organization='scytale-ai'))


def init_cli():
    parser = argparse.ArgumentParser(description="Scytale compliance CLI")

    parser.add_argument('--github', nargs="*", help="Run GitHub tests",
                        choices=github_test_suite.test_args)
    parser.add_argument('--to-csv', action="store_true", help="Output results to CSV")
    parser.add_argument('--github-auth-file', help="file containing Github token", required=False)

    return parser.parse_args()


def run_integration_operations(integration_args, integration_name):
    test_suite = {}
    if integration_name == 'github':
        test_suite = github_test_suite

    if integration_args is not None and test_suite is not None:
        # TODO - Check if authenticated
        if not integration_args:
            result = test_suite.select_test()
        else:
            method_name = integration_args[0]
            test_name = test_suite.get_test_name(method_name)
            result = test_suite.run_test(test_name)
    return result


def run_cli():
    args = init_cli()

    if args.github is not None:
        result = run_integration_operations(args.github, 'github')

    # TODO - not implemented yet
    # elif args.aws is not None:
    #     result = run_integration_operations(args.aws, 'aws')

    if args.to_csv:
        convert_dataframe_to_csv(result)
