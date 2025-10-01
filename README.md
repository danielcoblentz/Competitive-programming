# Competitive Programming Repo

Welcome to the Competitive Programming repository! This repo contains solutions to various competitive programming problems. Below, you'll find instructions on how to set up and use the files in this repository.

## Table of Contents
- [Setup](#setup)
- [Required Extensions](#required-extensions)
- [File Structure](#file-structure)
- [Usage](#usage)


## Setup

To get started with this project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/competitive-programming.git
   cd competitive-programming

 ## Required extensions

- To view the questions from previous years, you will need to install a PDF viewer (if not already installed in VS Code).
- Extensions --> "pdf viewer"

 ## File structure
- Each set of problems is categorized into folders corresponding to the year of the problems. The files within each folder are the solutions to the questions. For consistency, please name each solution  `<Year><Problem#> ` (e.g., 2023Problem1.py) and place it in the respective year's folder.

 ## Usage
- If multiple people are working on the same problem, please create a new branch to avoid confusion. Otherwise, feel free to work on any problems you'd like! 

## Running tests

This repository includes a small automated test suite that exercises a handful of implemented problems (example-based smoke tests). The tests are implemented using Python's built-in unittest framework and are located in the `tests/` folder.

What the tests cover right now:
- A selection of 2022 problems (example inputs/outputs): `2022Problem3.py`, `2022Problem8.py`, and `2022Problem9.py`.
- A couple of 2024 problems (small smoke checks): `2024Problem7.py` and `2024Problem8.py` preprocess smoke test.

How to run the tests (Windows/PowerShell):

```powershell
# use the Python you normally run the scripts with
python -m unittest discover -v
```

Notes:
- Tests run the solution scripts as subprocesses, providing example input via stdin and comparing stdout against the expected example outputs taken from the contest PDFs.
- If you add or modify solution scripts, update or add tests under `tests/` to keep coverage current.

If you'd like, I can wire up a GitHub Actions workflow to run these tests automatically on push or pull requests — tell me and I'll add it.