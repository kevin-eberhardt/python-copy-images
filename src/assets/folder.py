from src.assets.file import File
class Folder:
    def __init__(self, head):
        self._head = head
        self._files = []
        self._metadata = []

    def push(self, file):
        file = file.lower()
        if(file.endswith(".jpg", 4) or file.endswith(".jpeg", 4)):
            self._files.append(File(file, self))

    def getName(self):
        return self._head

    def getHierarchy(self):
        for file in self._files:
            print("-    " + file.getName())

    def getImages(self):
        for file in self._files:
            if file._type == "Image":
                print(file._head + " erstellt am: " + str(file._metadata[0]['datetime']))
                print(str(file._metadata))
            else:
                pass