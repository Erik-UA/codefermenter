import argparse
import sys
from typing import List
from .command_models import CommandAbstract
from ..models import AppParameters


class CommandManager:


    def __init__(self) -> None:
        self.main_parser = argparse.ArgumentParser(description="File conversion utility.")
        self.sub_parser = self.main_parser.add_subparsers(dest="command", help="Sub-command help")
        self.command_list: List[CommandAbstract] = []
        self.add_main_args()


    def add_main_args(self) -> None:
        self.main_parser.add_argument(
            "--remove-source", action="store_true", help="Delete source file"
        )

    def append_command_parser(self, command: CommandAbstract) -> None:
        self.command_list.append(command)
        command.parse_command(self.sub_parser)

    def finalize_arg_parser(self) -> AppParameters:
        args = self.main_parser.parse_args()
        for command in self.command_list:
            if args.command == command._name:
                app_params = command.create_app_parameters_for_command(args)
                print(app_params)
                return app_params

        self.main_parser.print_help()
        sys.exit(1)
