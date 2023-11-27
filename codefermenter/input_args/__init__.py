from ..models import AppParameters
from .command_manager import CommandManager
from .command_models import CommandDirect
from .command_models import CommandRecursive


def get_app_params() -> AppParameters:
    """
    Initializes the command manager, adds the command parsers and
    operations, and finalizes the argument parsing to generate and return application parameters.

    This function sets up the various components needed for command-line argument
    handling, delegates the addition of specific command parsers to the command manager,
    and uses it to finalize the argument parsing process. It will parse and handle
    the command-line arguments provided to the application when the function is called.

    Returns:
        AppParameters: An instance of the AppParameters class, containing the parsed
                       command-line arguments and any configurations that correspond
                       to the input command.
    """
    args_manager = CommandManager()

    # Append parsers for specific commands
    args_manager.append_command_parser(CommandDirect())

    # Finalize argument parsing and extract application parameters
    args_manager.append_command_parser(CommandRecursive())

    app_parameters = args_manager.finalize_arg_parser()
    return app_parameters
