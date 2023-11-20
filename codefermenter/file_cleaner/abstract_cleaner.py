from abc import ABC, abstractmethod

 
class AbstractCleaner(ABC):

    @abstractmethod
    def clean(self, file:str):
        ...