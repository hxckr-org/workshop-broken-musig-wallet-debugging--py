# Multisig Wallet Workshop

## Overview

This workshop will guide you through the creation of a multisig wallet using Python and the Bitcoin utilities library. A multisig wallet requires multiple signatures to authorize a transaction, enhancing security.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Git

## Quick Start

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

2. Run the setup script:

```bash
chmod +x setup.sh
./setup.sh
```

This will:

- Create a Python virtual environment
- Install all required dependencies
- Make the program executable

3. Activate the virtual environment:

```bash
source .hxckr/bin/activate
```

## Manual Setup

If you prefer to set up manually, you can:

1. Create a new virtual environment:

```bash
python3 -m venv .hxckr
```

2. Activate the virtual environment:

```bash
source .hxckr/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Passing the First Stage

The entry point to the workshop is the [main.py](app/main.py) file. To pass the first stage, you need to create an empty commit and push it to the remote repository.

```bash
git commit --allow-empty -m "Pass the first stage"
git push
```

## Passing Other Stages

Study the code in the [main.py](app/main.py) file and fix the bugs. There are comments in the code that will guide you to the solution. When you are done, create a new commit and push it to the remote repository.

```bash
git commit -am "Pass the stage"
git push
```

You can also run the program manually to test your changes.

```bash
./your_program.sh
```

## Goals

- Fix the bugs in the program

## Bugs

1. Missing validation for required_signatures > 0
2. Ignoring config parameter
3. Missing initialization of redeem_script and addresses
4. Not clearing existing keypairs before generating new ones
5. Not calling create_multisig_addresses()

## Fixing the Bugs

1. Add a check for required_signatures > 0
2. Add a check for config parameter
3. Initialize redeem_script and addresses
4. Clear existing keypairs before generating new ones
5. Call create_multisig_addresses()

## Exit the virtual environment

```bash
deactivate
```
