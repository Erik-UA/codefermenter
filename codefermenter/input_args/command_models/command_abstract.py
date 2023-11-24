from abc import ABC, abstractmethod
from typing import Any
from ...models import AppParameters


class CommandAbstract(ABC):
    _name = type[str]

    @abstractmethod
    def parse_command(self, arg_parser: Any) -> None:
        ...

    @abstractmethod
    def create_app_parameters_for_command(self, arg_parser: Any) -> AppParameters:
        ...
