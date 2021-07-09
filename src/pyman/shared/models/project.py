from abc import ABC, abstractmethod
from os.path import join
from pathlib import Path
from typing import List

from pydantic import BaseModel

from src.pyman.utils import FileManager

from .enums import FileTemplates


class Project(ABC):
    def __init__(self, name: str, path: str):
        self.__name = name
        self.__path = Path(path)
        self.__root_path = Path(join(path, name))

    @property
    def name(self) -> str:
        return self.__name

    @property
    def path(self) -> Path:
        return self.__path

    @property
    def root_path(self) -> Path:
        return self.__root_path

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


class PackageSetup(BaseModel):
    name: str
    author: str
    author_email: str
    description: str
    repo_url: str
    python_version: float = 3.9
    file_name: FileTemplates = FileTemplates.SETUP

    def create_file(self, path: str) -> str:
        tmp_setup_path = FileManager.get_template_path(
            'package', self.file_name)
        setup_file_path = FileManager.copy_file(
            tmp_setup_path, join(path, self.file_name.value))
        FileManager.replace_variables(setup_file_path, {
            'author': self.author,
            'author_email': self.author_email,
            'description': self.description,
            'name': self.name,
            'python_version': self.python_version,
            'repo_url': self.repo_url,
        })
        return setup_file_path


class Package(Project):
    def __init__(self, setup: PackageSetup, path: str):
        super().__init__(setup.name, path)
        self.__setup = setup

    def create(self):
        self._add_file([], FileTemplates.MAKEFILE)
        self.__setup.create_file(str(self.root_path))
