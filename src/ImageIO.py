import os
import cv2
import Cube_1
import inspect
class ImageIO:

    valid_types = [".jpg", ".gif", ".png", ".tga"]

    @classmethod
    def loadImages(cls, side, filetype):
        if cls.checkValidImageFormat(filetype):

            path = os.path.dirname(inspect.getfile(Cube_1)) + "/Side_" + side + filetype
            img = cv2.imread(path, 1)
            if img is None:
                print("File I/O Error")
            return img
        print("INVALID FILE TYPE")

    @classmethod
    def checkValidImageFormat(cls,filetype):

        if filetype in cls.valid_types:
            return True
        return False




