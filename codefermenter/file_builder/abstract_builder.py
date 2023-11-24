from abc import ABC, abstractmethod
from typing import Any
from ..models import FileData


class AbstractBuilder(ABC):
    def __call__(self, *args: Any, **kwargs: Any) -> None:
        self.build(*args, **kwargs)

    @abstractmethod
    def build(self, file: FileData) -> None:
        ...
