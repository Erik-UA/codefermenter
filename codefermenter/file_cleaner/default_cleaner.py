import os
from .abstract_cleaner import AbstractCleaner
from ..models import FileData
from pathlib import Path


class DefaultCleaner(AbstractCleaner):
    extension_list = ["c"]

    def __init__(self, remove_source: bool) -> None:
        super().__init__()
        if remove_source:
            self.extension_list.append("py")

    def clean(self, file: FileData) -> None:
        abs_fullpath = os.path.dirname(file.path)
        filename = Path(file.path).resolve().stem
        for extension in self.extension_list:
            Path(os.path.join(abs_fullpath, f"{filename}.{extension}")).unlink()
