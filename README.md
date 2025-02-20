# FakeEmailGenerator

A small Python project to generate a list of fake email addresses (seeded by [Faker](https://pypi.org/project/Faker/)) ending with `@gmail.com`. By default, the script (`createAccounts.py`) generates 2,000 email addresses and saves them to `FakedEmail.txt`.

---

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation & Usage](#installation--usage)
4. [Code Explanation](#code-explanation)
5. [Contributing](#contributing)
6. [License](#license)

---

## Features
- Uses the [Faker](https://pypi.org/project/Faker/) library to generate random usernames.
- Appends `@gmail.com` to each username.
- Automatically writes the generated emails to a text file, one address per line.

---

## Prerequisites
- **Python 3.7+** (it’s recommended to use a more recent version).
- The Faker library:
  ```bash
  pip install Faker
