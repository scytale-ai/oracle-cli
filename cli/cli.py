import argparse


def init_cli():
    parser = argparse.ArgumentParser(description="Check your com")

    parser.add_argument('--github', action="store_true", help="Run GitHub tests")
    parser.add_argument('--disconnect', action="store_true", help="Disconnect from github")

    return parser.parse_args()


def run_cli():
    args = init_cli()

    if args.github:
        print('running github')
    elif args.disconnect:
        print('Disconnected from integration...')
