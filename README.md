# Multisig Wallet Workshop

## Overview

This workshop will guide you through the creation of a multisig wallet using Python and the Bitcoin utilities library. A multisig wallet requires multiple signatures to authorize a transaction, enhancing security.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Required Python packages listed in `requirements.txt`

You can create a new virtual environment using:

```bash
python -m venv .hxckr
```

You can install the required packages using:

```bash
pip install -r requirements.txt
```

## Running the Program

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
