import argparse
from models.github import GithubIntegration
from models.test_suite import TestSuite
from .utils import convert_dataframe_to_csv

INTEGRATIONS = {
    'github': GithubIntegration
}


def init_cli():
    parser = argparse.ArgumentParser(description="Scytale compliance CLI")
    parser.add_argument('--integration',
                        default='github',
                        choices=INTEGRATIONS.keys(),
                        help=f"the integration to run. supported options: {INTEGRATIONS.keys()}")
    parser.add_argument('--test-name',
                        required=False,
                        help="choose which test to run, optional")
    parser.add_argument('--github-organization',
                        required=False,
                        help="GitHub organization name")
    parser.add_argument('--github-token-file',
                        help="path to a file containing the github token",
                        required=False)
    parser.add_argument('--to-csv',
                        action="store_true",
                        help="Output results to CSV")

    return parser.parse_args()


def run_cli():
    args = init_cli()

    if args.integration == 'github':
        if not args.github_organization:
            raise ValueError(f'please provide "--github-organization" argument')

        # get github_token file path
        if not args.github_token_file:
            auth_file ='./github_token'
        else:
            auth_file = args.github_token_file

        test_suite = TestSuite(GithubIntegration(organization=args.github_organization, auth_file=auth_file))
    else:
        raise ValueError(f'please provide "--integration" argument')

    # run the given test / let the user choose the test
    if args.test_name:
        result = test_suite.run_test(args.test_name)
    else:
        result = test_suite.select_test()

    if args.to_csv:
        convert_dataframe_to_csv(result)
