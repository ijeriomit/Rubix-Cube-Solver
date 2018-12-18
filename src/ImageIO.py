import errno
import os
import cv2
from Cube import Cube_1
import inspect


class ImageIO:

    valid_types = [".jpg", ".png", ".tga"]
    max_num_images = 6

    def __init__(self, filetype=".jpg"):
        self.images = [None for i in range(0, self.max_num_images)]
        self.filetype = filetype

    def loadImage(self, face, filetype):
        self.checkValidImageFormat(filetype)
        path = os.path.dirname(inspect.getfile(Cube_1 )) + "/Face_" + face + filetype
        self.checkValidPath(path)
        img = cv2.imread(path, 1)
        return img

    def saveImages(self):
        for i in range(0, self.max_num_images):
            self.images[i] = self.loadImage(str(i + 1), self.filetype)
        return self.images

    def setFileType(self, filetype):
        self.filetype = filetype

    def checkValidPath(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

    def checkValidImageFormat(self, filetype):
        if filetype not in self.valid_types:
            raise FileNotFoundError





