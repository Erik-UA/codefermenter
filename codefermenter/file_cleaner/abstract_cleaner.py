from abc import ABC, abstractmethod
from typing import Any
from ..models import FileData


class AbstractCleaner(ABC):
    """
    Abstract base class for all cleaner implementations.

    Objects of subclasses derived from this base class are callable and used
    to clean resources based on specific rules implemented in the `clean` method.
    """

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        self.clean(*args, **kwargs)

    @abstractmethod
    def clean(self, file: FileData) -> None:
        """
        Abstract method to clean resources associated with a given file.

        This method must be implemented by subclasses to define the specific cleaning
        operations to perform.

        Args:
            file (FileData): An object containing data about a file to be cleaned.
        """
        ...
