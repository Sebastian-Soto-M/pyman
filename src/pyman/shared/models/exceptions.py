from .enums import LogMessage


class FileExistsError(Exception):
    def __init__(self, path: str):
        super().__init__(message=f'{LogMessage.EXISTING_FOLDER.value}: {path}')
