from ImageProcessing import ImageProcessing
from ColorPicker import PickColor
import os
import cv2
import inspect


class CubeFaces:

    max_num_images = 6
    valid_types = [".jpg", ".png", ".tga"]
    up_pos_matrix = [i for i in range(9)]
    front_pos_matrix = [12, 13, 14, 24, 25, 26, 36, 37, 38]
    right_pos_matrix = [15, 16, 17, 27, 28, 29, 39, 40, 41]
    back_pos_matrix = [18, 19, 20, 30, 31, 32, 42, 43, 44]
    left_pos_matrix = [9, 10, 11, 21, 22, 23, 33, 34, 35]
    down_pos_matrix = [45, 46, 47, 48, 49, 50, 51, 52, 53]
    pos_matrix = [up_pos_matrix, front_pos_matrix, right_pos_matrix, back_pos_matrix, left_pos_matrix, down_pos_matrix]

    def __init__(self, dir):
        self.images = self.load_images(dir)
        self.pickColor = PickColor()
        self.imgPro = ImageProcessing()
        self.faces = [[[None for _ in range(3)] for _ in range(3)] for _ in range(6)]
        self.cube_str_list = ['' for _ in range(54)]

    def create_string_from_face(self, face, posmat, container):
        counter = 0
        for i in range(3):
            for j in range(3):
                container[posmat[counter]] = face[i][j]
                counter += 1
        return container

    def create_cube_string(self):
        self.init_all_faces()
        for i in range(len(self.faces)):
            self.create_string_from_face(self.faces[i], self.pos_matrix[i], self.cube_str_list)
        return ''.join(self.cube_str_list)

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





