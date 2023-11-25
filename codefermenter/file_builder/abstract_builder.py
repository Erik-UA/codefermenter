from abc import ABC, abstractmethod
from typing import Any
from ..models import FileData


class AbstractBuilder(ABC):
    """
    An abstract base class for builders used to compile various file types.

    This class defines the general interface for builder objects, requiring the implementation
    of a `build` method in subclasses. It also implements the `__call__` method to allow the
    instances of its subclasses to be called as functions, delegating to the `build` method.
    """

    def __call__(self, *args: Any, **kwargs: Any) -> None:
        """
        Allows an instance of a subclass to be called as a function, delegating to the `build` method.

        :param args: Positional arguments to pass to the `build` method.
        :param kwargs: Keyword arguments to pass to the `build` method.
        """
        self.build(*args, **kwargs)

    @abstractmethod
    def build(self, file: FileData) -> None:
        """
        Abstract method that must be implemented by subclasses to build a file.

        Implementing this method in a subclass would handle the logic for compiling or processing
        the given file data, depending on the specifics of the builder.

        :param file: A `FileData` object containing information about the file to be built.
        """
        ...
