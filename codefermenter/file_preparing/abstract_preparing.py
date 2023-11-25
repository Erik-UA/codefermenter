from abc import ABC, abstractmethod
from typing import Generator
from ..models import FileData


class AbstractPreparing(ABC):
    """
    Abstract base class for preparing file data.

    Concrete subclasses should implement the 'preparing' method to provide a generator
    iterating over FileData instances.
    """

    def __iter__(self) -> Generator[FileData, None, None]:
        """
        Returns a generator that yields FileData instances as defined by the concrete
        implementation of the 'preparing' method.

        Returns:
            Generator[FileData, None, None]: A generator yielding FileData instances.
        """
        return self.preparing()

    @abstractmethod
    def preparing(self) -> Generator[FileData, None, None]:
        """
        Abstract method to be implemented by subclasses. It should return a generator
        yielding FileData instances.

        Returns:
            Generator[FileData, None, None]: A generator yielding FileData instances.
        """
        ...
