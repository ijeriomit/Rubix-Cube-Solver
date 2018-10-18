from PIL import Image


class ImageIO:
    valid_types = [".jpg", ".gif", ".png", ".tga"]

    @classmethod
    def loadImages(cls, side, filetype):

        if not cls.checkValidImageFormat(filetype):
            print("INVALID FILE TYPE")
        path = "/Ijeri/Documents/PycharmProjects/Rubix-Cube/Cube_1/Side_"+side+filetype
        img = Image.open(path,'rb')
        return img

    @classmethod
    def checkValidImageFormat(cls,filetype):

        if filetype in cls.valid_types:
            return True
        return False




