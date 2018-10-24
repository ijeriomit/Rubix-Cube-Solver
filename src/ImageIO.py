import cv2

class ImageIO:

    valid_types = [".jpg", ".gif", ".png", ".tga"]
    path = "C:/Users/Ijeri/Documents/PycharmProjects/Rubix-Cube/Cube_1/Side "
    @classmethod
    def loadImages(cls, side, filetype):
        if cls.checkValidImageFormat(filetype):
            cls.path += (side+filetype)
            img = cv2.imread(cls.path, 1)
            if img is None:
                print("File I/O Error")
            return img
        print("INVALID FILE TYPE")
    @classmethod
    def checkValidImageFormat(cls,filetype):

        if filetype in cls.valid_types:
            return True
        return False




