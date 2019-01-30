from ImageProcessing import ImageProcessing
from ColorPicker import PickColor
import os
import cv2
import inspect


class CubeFaces:

    max_num_images = 6
    valid_types = [".jpg", ".png", ".tga"]

    def __init__(self, dir):
        self.images = self.load_images(dir)
        self.pickColor = PickColor()
        self.imgPro = ImageProcessing()
        self.faces = [[[None for _ in range(3)] for _ in range(3)] for _ in range(6)]

    def load_images(self, dir):
        images = list()
        path = os.path.dirname(inspect.getfile(dir))
        for filename in os.listdir(path):
            if self.checkValidImageFormat(filename):
                images.append(cv2.imread(os.path.join(path, filename), 1))
        return images

    def checkValidImageFormat(self, file):
        for i in self.valid_types:
            if file.endswith(i):
                return True
        return False

    def init_face_color(self, image, face):
        cells = self.imgPro.splitImage(image)
        for i in range(0, 3):
            for j in range(0, 3):
                face[i][j] = self.pickColor.calculateColorinCell(cells.get((i, j)))
        return face

    def init_all_faces(self):
        for i in range(0, self.max_num_images):
            self.init_face_color(self.images[i], self.faces[i])





