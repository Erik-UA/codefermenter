import argparse
from typing import Any
from .command_abstract import CommandAbstract
from ..args_helper import (
    validate_py_file_list,
    validate_directories_list,
    validate_directory,
)
from ...enums import PreparingType
from ...models import AppParameters
from ...constant import COMMAND_RECURSIVE


class CommandRecursive(CommandAbstract):
    _name = COMMAND_RECURSIVE

    def parse_command(cls, arg_parser: argparse._SubParsersAction[Any]) -> None:
        recursive_parser = arg_parser.add_parser(
            COMMAND_RECURSIVE, help=f'Help for the "{COMMAND_RECURSIVE}" command'
        )
        recursive_parser.add_argument(
            "--source-dir",
            type=validate_directory,
            default=None,
            required=True,
            help="Specify the directory of source code files. Example: --source-dir ./src or /home/user/project/src",
        )
        recursive_parser.add_argument(
            "--exclude-files",
            default=None,
            type=validate_py_file_list,
            help="List of files to exclude, separated by commas. Example: --exclude-files main.py,example.py",
        )
        recursive_parser.add_argument(
            "--exclude-directories",
            default=None,
            type=validate_directories_list,
            help="List of directories to exclude, separated by commas. Example: --exclude-directories /home/user/project/src/models",
        )

    def create_app_parameters_for_command(cls, arg_parser: Any) -> AppParameters:
        return AppParameters(
            preparing_type=PreparingType.RECURSIVE,
            source_dir=arg_parser.source_dir,
            exclude_directories=arg_parser.exclude_directories
            if arg_parser.exclude_directories
            else [],
            exclude_files=arg_parser.exclude_files if arg_parser.exclude_files else [],
            remove_source=arg_parser.remove_source,
            direct_files=[],
        )
