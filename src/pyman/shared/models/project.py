from abc import ABC, abstractmethod
from os.path import join
from pathlib import Path
from typing import List

from src.pyman.shared.models.exceptions import FolderExistsError
from src.pyman.utils import FileManager

from .enums import FileTemplates


class Project(ABC):
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = Path(path)
        self.root_path = Path(join(self.path, self.name))

    @abstractmethod
    def create(self):
        """ Method to create the initial structure of the project"""

    def create_module(self, relative_path: List[str], with_main: bool =
                      False) -> Path:
        mod = Path(join(self.root_path, *relative_path))
        mod.mkdir(exist_ok=True)
        self._add_file(relative_path, FileTemplates.INIT)
        if with_main:
            self._add_file(relative_path, FileTemplates.MAIN)
        return mod

    def _add_file(self, relative_path: List[str],
                  template: FileTemplates) -> Path:
        return FileManager.touch_file(
            join(self.root_path, *relative_path, template.value))


class BasicProject(Project):
    def __init__(self, name: str, path: str):
        super().__init__(name, path)

    def create(self):
        self.root_path.mkdir(exist_ok=True)
        self.create_module(['src'])
        self.create_module(['tests'], True)
