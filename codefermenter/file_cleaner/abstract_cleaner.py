from abc import ABC, abstractmethod


class AbstractCleaner(ABC):
    def __call__(self, *args, **kwargs):
        self.clean(*args, **kwargs)

    @abstractmethod
    def clean(self, file: str):
        ...
