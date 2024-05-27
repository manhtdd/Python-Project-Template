# Python Project Template

Welcome to the Python Project Template! This template is designed to provide a comprehensive starting point for your Python projects, including essential features such as logging, profiling, and testing. This README will guide you through the setup, structure, and usage of this template.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Logging](#logging)
5. [Profiling](#profiling)
6. [Testing](#testing)
7. [Contributing](#contributing)
8. [License](#license)

## Project Structure

```
Python-Project-Template/
├── python-project-template/
│   ├── __init__.py
│   ├── main.py
│   ├── module1/
│   │  ├── __init__.py
│   │   └── example1.py
│   └── module2/
│       ├── __init__.py
│       └── example2py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── module/
│       └── test_example.py
├── logs/
│   └── app.log
├── profiles/
│   └── profile.prof
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

## Installation

To set up this project template, follow these steps:

1. Clone the repository:
    ```bash
    https://github.com/manhtdd/Python-Project-Template.git
    cd Python-Project-Template
    ```

2. Create and activate a virtual environment *(optional but recommended, either conda and python env is fine)*

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. To run the main script:
    ```bash
    python python-project-template/main.py
    ```

2. To run a single module:
    ```bash
    python -m python-project-template.module1.example1
    ```
## Logging

This project template includes logging setup to help with tracking the application's runtime behavior. Log files are stored in the `logs/` directory.

- The logging configuration is defined in `python-project-template/main.py` and can be customized as needed.
- By default, logs are written to `logs/app.log`.

## Profiling

Profiling is integrated to help identify performance bottlenecks.

- To run the profiler, use the `cProfile` module or any other preferred profiling tool.
- Profile reports are stored in the `profiles/` directory.

Example profiling command:
```bash
python -m cProfile -o profiles/profile.prof python-project-template/main.py
```

## Testing

This project template includes a testing framework using `unittest` to ensure code quality and reliability.

- Test files are located in the `tests/` directory, mirroring the structure of the `python-project-template/` directory.
- To run the tests:
    ```bash
    pytest
    ```
- To run the a single test:
    ```bash
    pytest -k <test function>
    ```

---

Thank you for using the Python Project Template! If you have any questions or suggestions, please feel free to open an issue or submit a pull request. Happy coding!