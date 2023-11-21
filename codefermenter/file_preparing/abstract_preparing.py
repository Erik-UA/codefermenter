from abc import ABC, abstractmethod


class AbstractPreparing(ABC):
    def __iter__(self):
        return self.preparing()

    @abstractmethod
    def preparing(self):
        ...
