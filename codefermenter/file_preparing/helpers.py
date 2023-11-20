import os
from pathlib import Path 

def abs_formatting(item:str)->str:
    """
    Convert a single file or directory path to its absolute path.

    This function takes a file or directory path as a string, expands any user abbreviations (like '~' for the home directory),
    and converts it to an absolute path. It's useful for standardizing paths in file operations.

    Parameters:
    item (str): A file or directory path as a string.

    Returns:
    str: The absolute path corresponding to the input item.
    """
    expanded = os.path.expanduser(item)
    return Path(expanded).resolve() 


def abs_formatting_list(item_list:list[str])->list[str]:
    """
    Convert a list of file or directory paths to their absolute paths using the formatting_list function.

    This function iterates over a list of file or directory paths, converts each to its absolute path using the 
    formatting_list function, and collects them into a new list. It's useful for batch processing of path standardization.

    Parameters:
    item_list (list[str]): A list of file or directory paths as strings.

    Returns:
    list[str]: A list containing the absolute paths corresponding to the items in the input list.
    """
    abs_excluded_items = []
    for item in item_list:
        abs_excluded_items.append(abs_formatting(item)) 
    return abs_excluded_items