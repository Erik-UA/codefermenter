from ..models import AppParameters
from ..constant import BUILD_DIR
from .abstract_cleaner import AbstractCleaner
from .default_cleaner import DefaultCleaner
import shutil


def remove_build_dir() -> None:
    """
    Remove the BUILD_DIR directory and its contents.

    This function uses `shutil.rmtree` to delete the directory specified by the global
    variable BUILD_DIR. If `BUILD_DIR` does not exist or an error occurs, the function
    will not raise an exception due to `ignore_errors=True`.
    """
    shutil.rmtree(BUILD_DIR, ignore_errors=True)


def get_cleaner(app_parameters: AppParameters) -> AbstractCleaner:
    """
    Instantiate and return a cleaner object based on application parameters.

    Args:
        app_parameters (AppParameters): An object containing configuration and
        run-time parameters for the application.

    Returns:
        AbstractCleaner: An instantiated object of the DefaultCleaner class with
        configuration set according to `app_parameters.remove_source`.
    """
    return DefaultCleaner(remove_source=app_parameters.remove_source)
