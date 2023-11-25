from typing import Generator, List, Any
from .abstract_preparing import AbstractPreparing
from pathlib import Path
from .helpers import abs_formatting_list, abs_formatting
from ..models import FileData


class RecursivePreparing(AbstractPreparing):
    """
    Prepares file data using a recursive method, by scanning directories for files.

    Excludes specified files and directories, and ignores empty files.
    """

    exclude_system_files = ["__init__", "__pycache__"]

    def __init__(
        self,
        source_dir: str | None,
        exclude_files: List[str],
        exclude_directories: List[str],
        *args: Any,
        **kwargs: Any
    ) -> None:
        """
        Initializes the RecursivePreparing with paths to exclude and the starting directory.

        Args:
            source_dir (str, optional): The path to the directory from which the recursive search
                                        will start. If not provided, it defaults to the directory
                                        of this file.
            exclude_files (List[str]): A list of file paths to exclude from the preparations.
            exclude_directories (List[str]): A list of directory paths to exclude from the preparations.
        """
        super().__init__(*args, **kwargs)
        self.exclude_directories = exclude_directories
        self.source_dir = source_dir
        self.exclude_files = exclude_files

    def get_source_dir(self) -> Path:
        """
        Gets the source directory for recursive searching.

        Returns:
            Path: The path object of the source directory.
        """
        if self.source_dir:
            return abs_formatting(self.source_dir)
        return Path(__file__).resolve().parent

    def _check_exclude(self, file: Path) -> bool:
        """
        Checks if a file should be excluded based on the exclude patterns.

        Args:
            file (Path): The file path object that is being checked.

        Returns:
            bool: True if the file should be excluded, otherwise False.
        """
        exclude_directories = abs_formatting_list(self.exclude_directories)
        exclude_files = abs_formatting_list(self.exclude_files)
        filename = Path(file).resolve().stem

        for ex_dir in exclude_directories:
            if str(ex_dir) in str(file):
                return True

        if file in exclude_files or filename in self.exclude_system_files:
            return True

        return False

    def preparing(self) -> Generator[FileData, None, None]:
        """
        Implementation of the abstract preparing method, specific to the recursive method.

        It recursively scans the source directory and yields FileData for non-empty,
        non-excluded files.

        Returns:
            Generator[FileData, None, None]: A generator yielding FileData instances for
                                             non-empty and non-excluded files.
        """
        for file in list(self.get_source_dir().glob("**/*.py")):
            if file.stat().st_size == 0 or self._check_exclude(file):
                continue
            yield FileData(name=Path(file).resolve().stem, path=str(file))
