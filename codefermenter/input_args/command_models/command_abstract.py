from abc import ABC, abstractmethod
from typing import Any
from ...models import AppParameters


class CommandAbstract(ABC):
    """
    An abstract base class defining the interface for command classes within a
    file conversion application. This interface is used by the CommandManager to
    add, configure, and execute commands within the command-line interface.

    Subclasses of CommandAbstract must implement the following abstract methods:

    - parse_command(self, arg_parser: Any) -> None:
        Defines the arguments for the command and adds them to the argument parser.
        This method is utilized by the CommandManager to configure the argument parser
        for subcommands based on the specifics of each command.

    - create_app_parameters_for_command(self, arg_parser: Any) -> AppParameters:
        Creates and returns an AppParameters instance based on the parsed arguments.
        This method is called by the CommandManager after parsing the arguments to
        create the application parameters, which are then used to execute the
        corresponding command.

    Class Attributes:
    - _name (str): A static property that stores the name of the command, used for
                    recognition during the argument parsing process by the CommandManager.
    """

    _name = type[str]

    @abstractmethod
    def parse_command(self, arg_parser: Any) -> None:
        ...

    @abstractmethod
    def create_app_parameters_for_command(self, arg_parser: Any) -> AppParameters:
        ...
