from abc import ABC, abstractmethod
from os.path import join
from pathlib import Path
from typing import List

from pydantic import BaseModel

from src.pyman.utils import FileManager

from .enums import ETemplate


class Project(ABC):
    """
    Class that defines the basic behavior of any type of project

    The root folder for the project is created when the class is initialized
    """

    def __init__(self, name: str, path: str):
        self.__name = name
        self.__path = Path(path)
        self.__root_path = Path(join(path, name))
        self.__root_path.mkdir(parents=True, exist_ok=True)

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
        """
        Creates a folder to the relative path specified with the basic files
        '__init__.py' and '__main__.py' (if selected)
        """
        mod = Path(join(self.root_path, *relative_path))
        mod.mkdir(exist_ok=True)
        self._add_file(relative_path, ETemplate.INIT)
        if with_main:
            self._add_file(relative_path, ETemplate.MAIN)
        return mod

    def _add_file(self, relative_path: List[str],
                  template: ETemplate) -> Path:
        """ Touches a file to the relative location defined """
        return FileManager.touch_file(
            join(self.root_path, *relative_path, template.file_name))


class BasicProject(Project):
    def __init__(self, name: str, path: str):
        super().__init__(name, path)

    def create(self):
        self.root_path.mkdir(exist_ok=True)
        self.create_module(['src'])
        self.create_module(['tests'], True)


class PackageSetup(BaseModel):
    """ Object used to create the setup.py file """
    name: str
    author: str
    author_email: str
    description: str
    repo_url: str
    python_version: float = 3.9
    template: ETemplate = ETemplate.SETUP

    def create_file(self, path: str) -> str:
        new_file_path = FileManager.add_template(ETemplate.SETUP,
                                                 Path(path))
        FileManager.replace_variables(new_file_path, {
            'author': self.author,
            'author_email': self.author_email,
            'description': self.description,
            'name': self.name,
            'python_version': self.python_version,
            'repo_url': self.repo_url,
        })
        return new_file_path


class PackageProject(Project):
    def __init__(self, setup: PackageSetup, path: str):
        super().__init__(setup.name, path)
        self.__setup = setup

    def create(self):
        self.create_readme()
        FileManager.add_template(ETemplate.PYPROJECT, self.root_path)
        FileManager.add_template(ETemplate.LICENSE, self.root_path)
        FileManager.add_template(ETemplate.MAKEFILE, self.root_path)
        self.__setup.create_file(str(self.root_path))

    def create_readme(self):
        new_file_path = FileManager.add_template(
            ETemplate.README, self.root_path)
        FileManager.replace_variables(new_file_path, {
            'name': self.__setup.name,
            'description': self.__setup.description,
        })
        return new_file_path
