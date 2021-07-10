from enum import Enum


class LogMessage(Enum):
    EXISTING_FOLDER = 'The program stopped, the project specified already existed'


class ETemplateType(Enum):
    PACKAGE = 'package'
    COMMON = 'common'
    API = 'api'
    GLOBAL = 'global'


class ETemplate(Enum):

    GITIGNORE = '.gitignore', ETemplateType.GLOBAL
    INIT = '__init__.py', ETemplateType.GLOBAL
    MAIN = '__main__.py', ETemplateType.GLOBAL
    MAKEFILE = 'Makefile', ETemplateType.COMMON
    README = 'README.md', ETemplateType.COMMON
    SETUP = 'setup.py', ETemplateType.PACKAGE
    PYPROJECT = 'pyproject.toml', ETemplateType.PACKAGE
    LICENSE = 'LICENSE', ETemplateType.PACKAGE

    def __init__(self, file_name: str, type: ETemplateType):
        self.file_name = file_name
        self.type = type.value
