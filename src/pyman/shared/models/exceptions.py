from .enums import LogMessage


class FolderExistsError(Exception):
    def __init__(self, path: str):
        super().__init__(f'{LogMessage.EXISTING_FOLDER.value}: {path}')
