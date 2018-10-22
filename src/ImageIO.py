from PIL import Image
import os

class ImageIO:

    valid_types = [".jpg", ".gif", ".png", ".tga"]

    @classmethod
    def loadImages(cls, side, filetype):
        if not cls.checkValidImageFormat(filetype):
            print("INVALID FILE TYPE")
        path = "C:/Users/Ijeri/Documents/PycharmProjects/Rubix-Cube/Cube_1/Side " + side + filetype
        try:
            img = Image.open(path,'r')
        except FileNotFoundError:
            print("FileNotFound")
            return None
        #img.format = "PNG"
        #img.show()
        return img

    @classmethod
    def checkValidImageFormat(cls,filetype):

        if filetype in cls.valid_types:
            return True
        return False




