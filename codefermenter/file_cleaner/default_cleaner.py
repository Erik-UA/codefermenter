import os
from .abstract_cleaner import AbstractCleaner
from ..models import FileData
from pathlib import Path


class DefaultCleaner(AbstractCleaner):
    """
    Default implementation of the AbstractCleaner class.

    This cleaner removes files with specific extensions from the file system.

    Attributes:
        extension_list (list[str]): A list of file extensions that this cleaner will
        target for removal.
    """

    extension_list = ["c"]

    def __init__(self, remove_source: bool) -> None:
        """
        Initialize the DefaultCleaner with the option to remove Python source files.

        Args:
            remove_source (bool): Determines whether '.py' files should be included in
            the list of file extensions to remove.
        """
        super().__init__()
        if remove_source:
            self.extension_list.append("py")

    def clean(self, file: FileData) -> None:
        """
        Remove files matching the predefined extensions associated with the given file's path.

        Args:
            file (FileData): An object containing data and metadata for a file whose
            associated files with specific extensions will be deleted.
        """
        abs_fullpath = os.path.dirname(file.path)
        filename = Path(file.path).resolve().stem
        for extension in self.extension_list:
            Path(os.path.join(abs_fullpath, f"{filename}.{extension}")).unlink()
