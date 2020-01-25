from exif import Image
from datetime import datetime
class File():
    def __init__(self, head, folder):
        self._head = head
        self._folder = folder
        image_exts = ["jpeg", "jpg"]
        self._type = ""
        self._metadata = []
        for ext in image_exts:
            if(ext in head.lower()):
                with open(folder.getName()+"/"+head, 'rb') as image_file:
                    my_image = Image(image_file)
                self._type = "Image"
                date = datetime.strptime(my_image.datetime_original, '%Y:%m:%d %H:%M:%S')
                datetime_digitized = datetime.strptime(my_image.datetime_digitized, '%Y:%m:%d %H:%M:%S')
                self._metadata.append({'datetime': date})
                self._metadata.append({'model': my_image.make + " " + my_image.model})
                self._metadata.append({'datetime_digitized': datetime_digitized})

                return

    def getName(self):
        return self._head

    def getFolder(self):
        return self._folder