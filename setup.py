from setuptools import setup, find_packages

setup(
    name='scytale_cli',
    version='1.0',
    packages=['scytale_cli', 'scytale_cli/cli'],
    # packages=find_packages(),
    entry_points={
        'console_scripts': ['scytale-cli=scytale_cli.cli.cli:run_cli']
    },
    url='https://scytale.ai/',
    license='GNU General Public License v3.0',
    author='evoosa & idan91',
    author_email='idan.ram91@gmail.com, evaosher@gmail.com, info@scytale.ai',
    description='get complience info from 3rd party apps like github'
)
