from src.assets.folder import Folder
from src.assets.file import File

class Directory():
    def __init__(self, head):
        self._head = head
        self._items = []
        self._folder = []
    def push(self, element):
        if(element[2] is not None):
            self._folder.append(Folder(element))
        else:
            self._items.append(File(element))

    def whatAmI(self):
        return self._head

    def getContent(self):
        print("Inhalte in der Directory '" + self._head + "':")
        for element in self._items:
            print(element)

    def getRoot(self):
        print("Folder in der Directory '" + self._head + "':")
        for element in self._folder:
            print(element)