from src.assets.directory import Directory
from src.assets.file import File
class Folder:
    def __init__(self, head):
        self._head = head
        self._files = []

    def push(self, file):
        self._files.append(File(file, self))