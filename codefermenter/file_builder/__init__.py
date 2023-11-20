from ..models import AppParameters, PreparingType
from ..exceptions import InvalidReaderTypeException
from .abstract_builder import AbstractBuilder
from .cython_builder import CythonBuilder

def get_builder(app_parameters: AppParameters) -> AbstractBuilder:
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
    return CythonBuilder()
