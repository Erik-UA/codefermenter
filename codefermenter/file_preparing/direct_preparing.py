from typing import Generator, List, Any
from pathlib import Path
from .abstract_preparing import AbstractPreparing
from .helpers import abs_formatting_list
from ..models import FileData


class DirectPreparing(AbstractPreparing):
    def __init__(self, direct_files: List[str], *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.direct_files = direct_files

    def preparing(self) -> Generator[FileData, None, None]:
        for file in abs_formatting_list(self.direct_files):
            if Path(file).stat().st_size == 0:
                continue

            yield FileData(name=Path(file).resolve().stem, path=str(file))
