from ..models import AppParameters
from ..constant import BUILD_DIR
from .abstract_cleaner import AbstractCleaner
from .default_cleaner import DefaultCleaner
import shutil


def remove_build_dir():
    shutil.rmtree(BUILD_DIR, ignore_errors=True)


def get_cleaner(app_parameters: AppParameters) -> AbstractCleaner:
    """
    Returns an instance of a parser class based on the reader type specified in app_parameters.

    This function currently supports the creation of a CsvReader. If the specified reader type
    is not supported, it raises an InvalidReaderTypeException.

    Parameters:
    - app_parameters (AppParameters): Application parameters, including the reader type,
                                      and parameters for skipping and taking items in the parsing process.

    Returns:
    - AbstractParser: An instance of a subclass of AbstractParser.

    Raises:
    - InvalidReaderTypeException: If the reader type in app_parameters is not supported.
    """
    return DefaultCleaner(remove_source=app_parameters.remove_source)
