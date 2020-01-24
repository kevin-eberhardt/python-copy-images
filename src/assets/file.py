class File():
    def __init__(self, head, folder):
        self._head = head
        self._folder = folder
        self._metadata = []

    def getName(self):
        return self._head

    def getFolder(self):
        return self._folder