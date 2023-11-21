import typing
from .abstract_preparing import AbstractPreparing
from pathlib import Path
from .helpers import abs_formatting_list, abs_formatting
from ..models import FileData


class RecursivePreparing(AbstractPreparing):
    exclude_system_files = ["__init__", "__pycache__"]

    def __init__(
        self, source_dir, exclude_files, exclude_directories, *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.exclude_directories = exclude_directories
        self.source_dir = source_dir
        self.exclude_files = exclude_files

    def get_source_dir(self):
        if self.source_dir:
            return abs_formatting(self.source_dir)
        return Path(__file__).resolve().parent

    def _check_exclude(self, file: Path) -> bool:
        exclude_directories = abs_formatting_list(self.exclude_directories)
        exclude_files = abs_formatting_list(self.exclude_files)
        filename = Path(file).resolve().stem

        for ex_dir in exclude_directories:
            if str(ex_dir) in str(file):
                return True

        if file in exclude_files or filename in self.exclude_system_files:
            return True

        return False

    def preparing(self) -> typing.Iterator[FileData]:
        for file in list(self.get_source_dir().glob("**/*.py")):
            if file.stat().st_size == 0 or self._check_exclude(file):
                continue
            yield FileData(name=Path(file).resolve().stem, path=str(file))
