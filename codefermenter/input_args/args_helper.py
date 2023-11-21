import argparse, re, sys


def validate_arg(arg: str, pattern: str) -> list:
    pattern = re.compile(pattern)
    if not pattern.match(arg):
        raise argparse.ArgumentTypeError("Invalid arg format.")
    arg = arg.replace(" ", "")
    return arg.split(",")


def validate_py_files(file_list):
    pattern = r"^((\.{0,2}\/)([\w\-\_\/]*[\w\-\_]+\.py)([\s])*([,])?([\s])*)*$"
    return validate_arg(file_list, pattern)


def validate_directories_files(file_list):
    pattern = re.compile(r"^(((\/|\.{0,2}\/)([\w\-\_]+)(\/)?)([\s])*([,])?([\s])*)*$")
    return validate_arg(file_list, pattern)
