import typing
from pathlib import Path
from .abstract_preparing import AbstractPreparing
from .helpers import abs_formatting_list
from ..models import FileData


class DirectPreparing(AbstractPreparing):
    def __init__(self, direct_files, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.direct_files = direct_files

    def preparing(self) -> typing.Iterator[FileData]:
        for file in abs_formatting_list(self.direct_files):
            if Path(file).stat().st_size == 0:
                continue

            yield FileData(name=Path(file).resolve().stem, path=str(file))
