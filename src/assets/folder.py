from src.assets.file import File
class Folder:
    def __init__(self, head):
        self._head = head
        self._files = []
        self._metadata = []

    def push(self, file):
        self._files.append(File(file, self))

    def getName(self):
        return self._head

    def getHierarchy(self):
        for file in self._files:
            print("-    " + file.getName())