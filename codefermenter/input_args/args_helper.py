import argparse
import re
from typing import List


def validate_arg(arg: str, pattern: str) -> List[str]:
    _pattern = re.compile(pattern)
    if not _pattern.match(arg):
        raise argparse.ArgumentTypeError("Invalid arg format.")
    arg = arg.replace(" ", "")
    return arg.split(",")


def validate_py_file_list(file_arg: str) -> List[str]:
    pattern = r"^((\.{0,2}\/)([\w\-\_\/]*[\w\-\_]+\.py)([\s])*([,])?([\s])*)*$"
    return validate_arg(file_arg, pattern)


def validate_directories_list(file_arg: str) -> List[str]:
    pattern = r"^(((\/|\.{0,2}\/)([\w\-\_]+)(\/)?)([\s])*([,])?([\s])*)*$"
    return validate_arg(file_arg, pattern)


def validate_directory(file_arg: str) -> str:
    pattern = r"^(((\/|\.{0,2}\/)([\w\-\_]+)(\/)?)([\s])*([,])?([\s])*)*$"
    return validate_arg(file_arg, pattern)[-1]
