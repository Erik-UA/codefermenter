import argparse, re, sys
from ..models import AppParameters, PreparingType
from ..exceptions import AppBaseException
from .args_helper import validate_py_files, validate_directories_files



def add_recursive_parser(sub_command):
    recursive_parser = sub_command.add_parser(
        'recursive',
        help='Help for the "recursive" command'
    )
    recursive_parser.add_argument(
        "--source-dir", type=str, default=None, required=True, 
        help="Specify the directory of source code files. Example: --source-dir ./src or /home/user/project/src"
    )
    recursive_parser.add_argument(
        "--exclude-files", default=None, type=validate_py_files,
        help="List of files to exclude, separated by commas. Example: --exclude-files main.py,example.py"
    )
    recursive_parser.add_argument(
        "--exclude-directories", default=None, type=validate_directories_files,
        help="List of directories to exclude, separated by commas. Example: --exclude-directories /home/user/project/src/models"
    )


def add_direct_parser(sub_command):
    direct_parser = sub_command.add_parser(
        'direct',
        help='Help for the "direct" command'
    )
    direct_parser.add_argument(
        "--direct-files", default=None, type=validate_py_files, required=True,
        help="List of specific files to compile, separated by commas. Example: --direct-files ./src/lib0.py, /home/user/src/lib1.py"
    )


def create_main_parser():
    parser = argparse.ArgumentParser(description="File conversion utility.")
    sub_command = parser.add_subparsers(dest="command", help="Sub-command help")
    add_recursive_parser(sub_command)
    add_direct_parser(sub_command)
    parser.add_argument('--remove-source', action='store_true', help='Delete source file')
    return parser



def create_app_parameters_for_recursive(args):
    return AppParameters(
        preparing_type=PreparingType.RECURSIVE,
        source_dir=args.source_dir,
        exclude_directories=args.exclude_directories if args.exclude_directories else [],
        exclude_files=args.exclude_files if args.exclude_files else [],
        remove_source=args.remove_source,
        direct_files=None
    )

def create_app_parameters_for_direct(args):
    return AppParameters(
        preparing_type=PreparingType.DIRECT,
        direct_files=args.direct_files if args.direct_files else [],
        remove_source=args.remove_source,
        source_dir=None,
        exclude_directories=None,
        exclude_files=None
    )



def parse_app_parameters() -> AppParameters:
    parser = create_main_parser()
    args = parser.parse_args()

    if args.command == 'recursive':
        return create_app_parameters_for_recursive(args)
    
    elif args.command == 'direct':
        return create_app_parameters_for_direct(args)
    
    else:
        parser.print_help()
        sys.exit(1)
        
