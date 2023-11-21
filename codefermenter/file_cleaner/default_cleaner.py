from .abstract_cleaner import AbstractCleaner
from pathlib import Path
import os


class DefaultCleaner(AbstractCleaner):
    extension_list = ["c"]

    def __init__(self, remove_source) -> None:
        super().__init__()
        if remove_source:
            self.extension_list.append("py")

    def clean(self, file: str):
        abs_fullpath = os.path.dirname(file.path)
        filename = Path(file.path).resolve().stem
        for extension in self.extension_list:
            Path(os.path.join(abs_fullpath, f"{filename}.{extension}")).unlink()
