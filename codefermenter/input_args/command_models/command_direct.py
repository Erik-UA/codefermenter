from typing import Any
from .command_abstract import CommandAbstract
from ..args_helper import validate_py_file_list
from ...enums import PreparingType
from ...models import AppParameters
from ...constant import COMMAND_DIRECT


class CommandDirect(CommandAbstract):
    _name = COMMAND_DIRECT

    def parse_command(cls, arg_parser: Any) -> None:
        direct_parser = arg_parser.add_parser(
            COMMAND_DIRECT, help=f'Help for the "{COMMAND_DIRECT}" command'
        )

        direct_parser.add_argument(
            "--direct-files",
            default=None,
            type=validate_py_file_list,
            required=True,
            help="List of specific files to compile, separated by commas. Example: --direct-files ./src/lib0.py, /home/user/src/lib1.py",
        )

    def create_app_parameters_for_command(cls, arg_parser: Any) -> AppParameters:
        return AppParameters(
            preparing_type=PreparingType.DIRECT,
            direct_files=arg_parser.direct_files if arg_parser.direct_files else [],
            remove_source=arg_parser.remove_source,
            source_dir=None,
            exclude_directories=[],
            exclude_files=[],
        )
