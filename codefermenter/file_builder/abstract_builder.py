from abc import ABC, abstractmethod
from ..models import FileData

class AbstractBuilder(ABC):

    def __call__(self, *args, **kwargs):
        self.build(*args, **kwargs)

    @abstractmethod
    def build(self, file:FileData):
        ...