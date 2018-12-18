import errno
import os
import cv2
from Images import Cube_1
import inspect


class ImageIO:

    valid_types = [".jpg", ".png", ".tga"]


    def loadImage(self, face, filetype):
        self.checkValidImageFormat(filetype)
        path = os.path.dirname(inspect.getfile(Cube_1)) + "/Face_" + face + filetype
        self.checkValidPath(path)
        img = cv2.imread(path, 1)
        return img

    def checkValidPath(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

    def checkValidImageFormat(self, filetype):
        if filetype not in self.valid_types:
            raise FileNotFoundError





