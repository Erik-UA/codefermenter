from dataclasses import dataclass
from enums import PreparingType


@dataclass
class FileData:
    name: str
    path: str


@dataclass
class AppParameters:
    source_dir: str
    exclude_directories: list
    exclude_files: list
    include_files: list
    remove_source: bool
    preparing_type:PreparingType
