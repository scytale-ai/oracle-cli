from setuptools import setup

setup(
    name='scytale-oracle',
    version='1.0',
    packages=['scytale_oracle', 'scytale_oracle/cli'],
    entry_points={
        'console_scripts': ['scytale-oracle=scytale_oracle.cli.cli:run_cli']
    },
    url='https://scytale.ai/',
    license='GNU General Public License v3.0',
    author='evoosa & idan91',
    author_email='idan.ram91@gmail.com, evaosher@gmail.com, info@scytale.ai',
    description='get complience information from 3rd party apps like github'
)
