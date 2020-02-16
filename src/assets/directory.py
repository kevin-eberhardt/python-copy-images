from src.assets.folder import Folder
from src.assets.file import File

class Directory():
    def __init__(self, head):
        self._head = head
        self._folder = []
        self._metadata = []
    def push(self, element):
        if(element[2] is not None):
            newFolder = Folder(element[0])
            for file in element[2]:
                newFolder.push(file)
            self._folder.append(newFolder)
        else:
            print("Nix gemacht")

    def whatAmI(self):
        return self._head

    def getRoot(self):
        print("Folder in der Directory '" + self._head + "':")
        for element in self._folder:
            print(element.getName())

    def getHierarchy(self):
        for folder in self._folder:
            print(folder.getName())
            folder.getHierarchy()

    def getImages(self):
        for folder in self._folder:
            folder.getImages()