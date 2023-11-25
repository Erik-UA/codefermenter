from ..models import AppParameters
from ..enums import PreparingType
from ..exceptions import InvalidReaderTypeException
from .abstract_preparing import AbstractPreparing
from .recursive_preparing import RecursivePreparing
from .direct_preparing import DirectPreparing


def get_preparing(app_parameters: AppParameters) -> AbstractPreparing:
    """
    Creates an instance of a preparing class based on the preparing type specified in app_parameters.

    Args:
        app_parameters (AppParameters): The application parameters object containing the preparing type
                                        and other related configurations.

    Returns:
        AbstractPreparing: An instance of a concrete subclass of AbstractPreparing as per the
                           preparing_type in app_parameters.

    Raises:
        InvalidReaderTypeException: If the preparing_type is not recognized (neither RECURSIVE nor DIRECT).
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
