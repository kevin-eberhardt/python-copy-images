from datetime import datetime
import exifread
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
                    my_image = exifread.process_file(image_file)
                self._type = "Image"
                if("Image DateTime" in my_image):
                    stripped = str(my_image.get('Image DateTime'))
                    if my_image.get('Image DateTime') is not None:
                        date = datetime.strptime(stripped, '%Y:%m:%d %H:%M:%S')
                else:
                    date = "unknown"
                self._metadata.append({'datetime': date})
                if("Image Make" in my_image or "Image Model" in my_image):
                    make = str(my_image.get('Image Make'))
                    model = str(my_image.get('Image Model'))
                    if(make is not None and model is not None): self._metadata.append({'model': make + " " + model})

    def getName(self):
        return self._head

    def getFolder(self):
        return self._folder