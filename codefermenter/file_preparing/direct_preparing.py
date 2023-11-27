from typing import Generator, List, Any
from pathlib import Path
from .abstract_preparing import AbstractPreparing
from .helpers import abs_formatting_list
from ..models import FileData


class DirectPreparing(AbstractPreparing):
    """
    Prepares file data for the direct method of operation.

    This class is used to iterate over a predefined list of files.
    """

    def __init__(self, direct_files: List[str], *args: Any, **kwargs: Any) -> None:
        """
        Initializes the DirectPreparing with a list of files to include in the preparations.

        Args:
            direct_files (List[str]): A list of file paths to include in the preparations.
        """
        super().__init__(*args, **kwargs)
        self.direct_files = direct_files

    def preparing(self) -> Generator[FileData, None, None]:
        """
        Implementation of the abstract preparing method, specific to the direct method.

        Yields only non-empty files from the list of direct_files.

        Returns:
            Generator[FileData, None, None]: A generator yielding FileData instances for
                                             non-empty files in the direct_files list.
        """
        for file in abs_formatting_list(self.direct_files):
            if Path(file).stat().st_size == 0:
                continue

            yield FileData(name=Path(file).resolve().stem, path=str(file))
