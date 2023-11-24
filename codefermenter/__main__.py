from .input_args import get_app_params
from .file_preparing import get_preparing
from .file_builder import get_builder
from .file_cleaner import get_cleaner, remove_build_dir


def main() -> None:
    app_parameters = get_app_params()
    preparing = get_preparing(app_parameters=app_parameters)
    builder = get_builder(app_parameters=app_parameters)
    cleaner = get_cleaner(app_parameters=app_parameters)

    for file in preparing:
        builder(file)
        cleaner(file)

    remove_build_dir()


if __name__ == "__main__":
    main()
