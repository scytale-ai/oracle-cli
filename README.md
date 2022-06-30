<div align="center"> 
  <br/>
  <br/>
  <a href="https://scytale.ai/">
    <img src="https://scytale.ai/wp-content/uploads/2021/07/scytale-logo.svg" alt="scytale-logo" width="200px"/>
  </a>  
  <br/>
  <br/>
  <hr/>
  <h1>🔮 The Scytale Oracle 🔮</h1>
  <strong style="color:cornflowerblue">Get a quick GitHub compliance assessment</strong>
  <br/>
  <br/>
</div>
<hr />

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

* Ubuntu
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

set your GitHub token as an environment variable named GITHUB_TOKEN, the Oracle uses it for authenticating with Github

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
  <strong style="color:cornflowerblue">
  🔮 Created by the <a href="https://scytale.ai/">Scytale</a> Hackathon Blue Team; Idan Ram, Eva Osherovsky, Jess Gopas &#169; 2022 🔮
  </strong>
</div>
<hr />