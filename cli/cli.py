import argparse
from .github.tests import run_github_test, select_github_test


def init_cli():
    parser = argparse.ArgumentParser(description="Scytale compliance CLI")

    github_choices = ['a', 'b', 'c']
    parser.add_argument('--github', nargs="*", help="Run GitHub tests",
                        choices=github_choices)
    parser.add_argument('--disconnect', action="store_true", help="Disconnect from github")

    return parser.parse_args()


def run_cli():
    args = init_cli()

    if args.github is not None:
        print(args.github)
        if not args.github:
            select_github_test()
        else:
            arg_name = args.github[0]
            print(arg_name)

            run_github_test(arg_name)

    if args.disconnect:
        print('Disconnected from integration...')
