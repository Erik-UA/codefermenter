import argparse
import re
from typing import List


def validate_arg(arg: str, pattern: str) -> List[str]:
    """
    Validates a given string argument against a provided regex pattern.

    This function checks if the argument matches the pattern. It then removes
    spaces and splits the argument by commas into a list of strings.

    Parameters:
    arg (str): The string argument to validate.
    pattern (str): The regex pattern to match the argument against.

    Returns:
    List[str]: A list of strings, split by comma, from the validated argument.

    Raises:
    argparse.ArgumentTypeError: If the argument does not match the pattern.
    """
    _pattern = re.compile(pattern)
    if not _pattern.match(arg):
        raise argparse.ArgumentTypeError("Invalid arg format.")
    arg = arg.replace(" ", "")
    return arg.split(",")


def validate_py_file_list(file_arg: str) -> List[str]:
    """
    Validates a list of Python file paths provided as a single string.

    The paths should be comma-separated and can include relative paths such as './',
    '../', or absolute paths. Spaces are ignored. The function validates that all
    provided files have a '.py' extension and conform to the expected pattern.

    Parameters:
    file_arg (str): The string containing comma-separated Python file paths to validate.

    Returns:
    List[str]: A list of validated Python file paths.
    """
    pattern = r"^((\.{0,2}\/)([\w\-\_\/]*[\w\-\_]+\.py)([\s])*([,])?([\s])*)*$"
    return validate_arg(file_arg, pattern)


def validate_directories_list(file_arg: str) -> List[str]:
    """
    Validates a list of directory paths provided as a single string.

    The directory paths should be comma-separated and can include './', '../' for
    relative paths or could be absolute paths. Each directory path is trimmed for spaces.

    Parameters:
    file_arg (str): The string containing comma-separated directory paths to validate.

    Returns:
    List[str]: A list of validated directory paths.
    """
    pattern = r"^(((\/|\.{0,2}\/)([\w\-\_]+)(\/)?)([\s])*([,])?([\s])*)*$"
    return validate_arg(file_arg, pattern)


def validate_directory(file_arg: str) -> str:
    """
    Validates a single directory path.

    The directory path can include './', '../' for relative paths or could be an
    absolute path. Spaces and commas are ignored.

    Parameters:
    file_arg (str): The directory path to validate.

    Returns:
    str: The last validated directory path from the argument if multiple are provided.
    """
    pattern = r"^(((\/|\.{0,2}\/)([\w\-\_]+)(\/)?)([\s])*([,])?([\s])*)*$"
    return validate_arg(file_arg, pattern)[-1]
