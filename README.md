
# CodeFermenter

## Overview
CodeFermenter is a tool designed for on-the-fly code obfuscation during deployment or for partial use to protect key parts of an algorithm in public repositories. Built upon Cython, it incorporates an abstraction layer for rapid and functional extension.

## Usage Modes

### 1. Recursive Mode
Enables specifying a project directory for recursive processing, excluding certain files or directories.

#### Example:
```bash
python -m codefermenter --source-dir ~/project/src --exclude-files ~/project/src/main.py --exclude-directories '~/project/src/tests, ~/project/src/models'
```

### 2. Direct Mode
Allows specifying specific files for obfuscation, useful for protecting individual files or parts of a project, such as a trading strategy.

#### Example:
```bash
python -m codefermenter direct --direct-files ~/project/src/app.py
```

## Additional Options

- **--remove-source**: Removes the source files immediately after obfuscation, convenient for builds in Docker containers.

## Important Note
The entry point of the application should remain in its original form. Only auxiliary modules can be obfuscated. For example, if `app.py` is the obfuscated part, and `main.py` serves as the entry point, the code would look like this:

- **app.py** (Obfuscated):
  ```python
  print("hello world")
  ```

- **main.py** (Entry Point):
  ```python
  import app
  ```

#### Single File Application:
```bash
python -m codefermenter direct --direct-files ./app.py
```
