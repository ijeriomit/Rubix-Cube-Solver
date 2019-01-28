from ImageIO import ImageIO
from ImageProcessing import ImageProcessing
from ColorPicker import PickColor


class CubeFaces:

    max_num_images = 6

    def __init__(self, filetype=".jpg"):
        self.imageio = ImageIO()
        self.filetype = filetype
        self.images = [None for _ in range(self.max_num_images)]
        self.pickColor = PickColor()
        self.imgPro = ImageProcessing()
        self.faces = [[[None for _ in range(3)] for _ in range(3)] for _ in range(6)]

    def saveImage(self, i):
        self.images[i] = self.imageio.loadImage(str(i), self.filetype)  # figure out filetypes

    def init_face_color(self, image, face):
        cells = self.imgPro.splitImage(image)
        for i in range(0, 3):
            for j in range(0, 3):
                face[i][j] = self.pickColor.calculateColorinCell(cells.get((i, j)))
        return face

    def init_all_faces(self):
        for i in range(0, self.max_num_images):
            self.saveImage(i)
            self.init_face_color(self.images[i], self.faces[i])





