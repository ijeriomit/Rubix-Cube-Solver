from ImageIO import ImageIO
from CubeFace import CubeFace

class Cube:

    max_num_images = 6

    def __init__(self, filetype=".jpg"):
        self.faces = [CubeFace(i) for i in range(1, 7)]
        self.imageio = ImageIO()
        self.cubematrix = [[[None for _ in range(3)] for _ in range(3)] for _ in range(6)]
        self.images = [None for _ in range(self.max_num_images)]
        self.filetype = filetype

    def saveImage(self, i):
        self.images[i] = self.imageio.loadImage(str(i + 1), self.filetype)  #figure out filetypes

    def FillCube(self):
        for i in range(0, self.max_num_images):
            self.saveImage(i)
            self.faces[i].saveColorCells(self.images[i])
            self.cubematrix[i] = self.faces[i].colorcells






