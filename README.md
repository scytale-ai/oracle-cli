<p align="center">
  <a href="https://scytale.ai/">
    <img src="https://scytale-files.s3.amazonaws.com/scytale-logo/scytale_logo_light_mode.webp#gh-light-mode-only" alt="scytale-logo" width="318px" />
  </a>
  <a href="https://scytale.ai/">
    <img src="https://scytale-files.s3.amazonaws.com/scytale-logo/scytale_logo_dark_mode.svg#gh-dark-mode-only" alt="scytale-logo" width="318px" />
  </a>
</p>
  <hr/>

<h1 align="center">🔮 The Scytale Oracle 🔮</h1>
<p style="font-weight: bold" align="center">Get a quick GitHub compliance assessment</p>
<br />
<hr/>

## Oracle's Purpose

The [Scytale](https://scytale.ai) Oracle is a light-weight, open-source compliance CLI allowing you to get a quick GitHub compliance check for
a multitude of tests.

### Supported Compliance Tests

* List Repositories
* Get All Users Repositories Permissions
* Get Repository Branch Protection Status
* Get User's Repositories Permissions
* List Pull Requests from the Past 24hrs

### Features

* The output can be written to a CSV file

<hr />

## Installation

### Prerequisites

* Python 3.8
* pip 21.3.1

Clone the oracle's repository

```shell 
git clone https://github.com/scytale-ai/cli.git
```

Install Oracle CLI

```shell
cd cli/
pip install ./
```

Check that the CLI is installed
```shell
scytale-oracle -h
```

### Set Up Authentication

set your [GitHub token](https://github.com/settings/tokens) as an environment variable named GITHUB_TOKEN, the Oracle uses it for authenticating with Github

* Make sure the token has read permissions, **no write permissions are required for the Oracle to work**

```shell
export GITHUB_TOKEN='<YOUR_PERSONAL_GITHUB_TOKEN>'
```

<hr />

## Examples & Help

To get help and the supported arguments, run: 
```shell
scytale-oracle -h
```

Example:
```shell
scytale-oracle --github-organization <ORGANIZATION_NAME>
```
* This command will display a dropdown that will let you choose the compliance test you wish to run

<hr/>

<div align="center"> 
  <strong>
  🔮 Created by the <a href="https://scytale.ai/">Scytale</a> Hackathon Blue Team; Idan Ram, Eva Osherovsky, Jess Gopas &#169; 2022 🔮
  </strong>
</div>
<hr />