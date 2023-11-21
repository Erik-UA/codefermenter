from .input_args.app_args import parse_app_parameters
from .file_preparing import get_preparing
from .file_builder import get_builder
from .file_cleaner import get_cleaner, remove_build_dir


def main():
    app_parameters = parse_app_parameters()
    preparing = get_preparing(app_parameters=app_parameters)
    builder = get_builder(app_parameters=app_parameters)
    cleaner = get_cleaner(app_parameters=app_parameters)

    for file in preparing:
        builder(file)
        cleaner(file)

    remove_build_dir()


if __name__ == "__main__":
    main()
