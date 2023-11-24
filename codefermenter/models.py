from dataclasses import dataclass
from .enums import PreparingType
from typing import List, Optional


@dataclass
class FileData:
    name: str
    path: str


@dataclass
class AppParameters:
    source_dir: Optional[str]
    exclude_directories: List[str]
    exclude_files: List[str]
    direct_files: List[str]
    remove_source: bool
    preparing_type: PreparingType
