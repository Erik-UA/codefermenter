from abc import ABC, abstractmethod
from typing import Any
from ..models import FileData


class AbstractCleaner(ABC):
    def __call__(self, *args: Any, **kwargs: Any) -> None:
        self.clean(*args, **kwargs)

    @abstractmethod
    def clean(self, file: FileData) -> None:
        ...
