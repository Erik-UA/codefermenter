from ..models import AppParameters
from .command_manager import CommandManager
from .command_models import CommandDirect
from .command_models import CommandRecursive


def get_app_params() -> AppParameters:
    args_manager = CommandManager()

    args_manager.append_command_parser(CommandDirect())
    args_manager.append_command_parser(CommandRecursive())

    app_parameters = args_manager.finalize_arg_parser()
    return app_parameters
