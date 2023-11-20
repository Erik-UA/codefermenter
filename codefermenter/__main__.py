
import argparse, re, sys
from models import AppParameters, PreparingType
from exceptions import AppBaseException
from file_preparing import get_preparing
from file_builder import get_builder
from file_cleaner import get_cleaner, remove_build_dir

def validate_py_files(file_list):
    pattern = re.compile(r"^((\.{0,2}\/)([\w\-\_\/]*[\w\-\_]+\.py)([\s])*([,])?([\s])*)*$")
    if not pattern.match(file_list):
        raise argparse.ArgumentTypeError("Invalid file list format. Please provide a comma-separated list of .py files.")
    file_list = file_list.replace(" ","")
    return file_list.split(',')


def validate_directories_files(file_list):
    pattern = re.compile(r"^(((\/|\.{0,2}\/)([\w\-\_]+)(\/)?)([\s])*([,])?([\s])*)*$")
    if not pattern.match(file_list):
        raise argparse.ArgumentTypeError("Invalid directories list format. Please provide a comma-separated list of .py files.")
    file_list = file_list.replace(" ","")
    return file_list.split(',')

def parse_app_parameters() -> AppParameters:

    parser = argparse.ArgumentParser(description="File conversion utility.")
    sub_command = parser.add_subparsers(dest="command", help="Sub-command help")
    recursive_parser = sub_command.add_parser(
        'recursive',
        help='Help for the "preparing" command'
    )

    recursive_parser.add_argument(
        "--source-dir", type=str, default=None, required=True, 
        help="Specify the directory of source code files. Example: --source-dir ./src or /home/user/project/src"
    ) 
 
    recursive_parser.add_argument(
        "--exclude-files", default=None, type = validate_py_files,
        help="List of files to exclude, separated by commas. Example: --exclude-files main.py,example.py"
    )

    recursive_parser.add_argument(
        "--exclude-directories", default=None, type = validate_directories_files,
        help="List of directories to exclude, separated by commas. Example: --exclude-directories /home/user/project/src/models"
    )

    direct_parser = sub_command.add_parser(
        'direct',
        help='Help for the "preparing" command'
    )

    direct_parser.add_argument(
        "--include-files", default=None, type = validate_py_files, required=True,
        help="List of specific files to compile, separated by commas. Example: --include-files lib0.py,lib1.py"
    )

    parser.add_argument(
        '--remove-source', action='store_true', help='Delete source file')


    args = parser.parse_args()

    if args.command == 'recursive':
        return AppParameters(
            preparing_type = PreparingType.RECURSIVE,
            source_dir = args.source_dir,
            exclude_directories = args.exclude_directories if args.exclude_directories else [],
            exclude_files = args.exclude_files if args.exclude_files else [],
            remove_source = args.remove_source,
            include_files = None
        )
    
    elif args.command == 'direct':
        ...

    else:
        parser.print_help()
        sys.exit(1)       


    




def main():

    app_parameters = parse_app_parameters()
    preparing = get_preparing(app_parameters=app_parameters)
    builder = get_builder(app_parameters=app_parameters)
    cleaner = get_cleaner(app_parameters=app_parameters)



    for file in preparing:
        builder.build(file)
        cleaner.clean(file)

    remove_build_dir()

main()