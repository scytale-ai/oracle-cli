import argparse
from .github.tests import run_github_test, select_github_test, github_choices


def init_cli():
    parser = argparse.ArgumentParser(description="Scytale compliance CLI")

    parser.add_argument('--github', nargs="*", help="Run GitHub tests",
                        choices=github_choices)
    parser.add_argument('--aws', nargs="*", help="Run AWS tests",
                        choices=github_choices)
    parser.add_argument('--disconnect', action="store_true", help="Disconnect from github")  # Deleted tokens.

    return parser.parse_args()


def run_integration_operations(integration_args, integration_name):
    integration_functions = {
        "github": {
            "selector": select_github_test,
            "runner": run_github_test
        },
    }

    print(integration_functions)

    if integration_args is not None:
        # TODO - Check if authenticated
        if not integration_args:
            integration_functions[integration_name]['selector']()
        else:
            arg_name = integration_args[0]

            integration_functions[integration_name]['runner'](arg_name)


def run_cli():
    args = init_cli()

    if args.github is not None:
        run_integration_operations(args.github, 'github')

    elif args.aws is not None:
        run_integration_operations(args.aws, 'aws')

    elif args.disconnect:
        print('Disconnected from integration...')
