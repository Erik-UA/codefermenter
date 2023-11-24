from abc import ABC, abstractmethod
from typing import Generator
from ..models import FileData


class AbstractPreparing(ABC):
    def __iter__(self) -> Generator[FileData, None, None]:
        return self.preparing()

    @abstractmethod
    def preparing(self) -> Generator[FileData, None, None]:
        ...
