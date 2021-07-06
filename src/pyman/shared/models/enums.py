from enum import Enum


class LogMessage(Enum):
    EXISTING_FOLDER = 'The program stopped, the project specified already existed'


class FileTemplates(Enum):
    SETUP = 'setup.py'
    INIT = '__init__.py'
    MAIN = '__main__.py'
    MAKEFILE = 'Makefile'
    README = 'README.md'
    GITIGNORE = '.gitignore'
