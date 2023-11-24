from ..models import AppParameters
from ..enums import PreparingType
from ..exceptions import InvalidReaderTypeException
from .abstract_preparing import AbstractPreparing
from .recursive_preparing import RecursivePreparing
from .direct_preparing import DirectPreparing


def get_preparing(app_parameters: AppParameters) -> AbstractPreparing:
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

    if app_parameters.preparing_type == PreparingType.RECURSIVE:
        return RecursivePreparing(
            source_dir=app_parameters.source_dir,
            exclude_directories=app_parameters.exclude_directories,
            exclude_files=app_parameters.exclude_files,
        )
    elif app_parameters.preparing_type == PreparingType.DIRECT:
        return DirectPreparing(direct_files=app_parameters.direct_files)

    raise InvalidReaderTypeException()
