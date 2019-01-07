from ImageIO import ImageIO
from ColorCells import ColorCells

class CubeFaces:

    max_num_images = 6

    def __init__(self, filetype=".jpg"):
        self.faces = [ColorCells() for _ in range(0, 6)]
        self.imageio = ImageIO()
        self.cubematrix = [[[None for _ in range(3)] for _ in range(3)] for _ in range(6)]
        self.images = [None for _ in range(self.max_num_images)]
        self.filetype = filetype

    def saveImage(self, i):
        self.images[i] = self.imageio.loadImage(str(i), self.filetype)  #figure out filetypes

    def FillCubeMatrix(self):
        for i in range(0, self.max_num_images):
            self.saveImage(i)
            self.faces[i].saveColorCells(self.images[i])
            self.cubematrix[i] = self.faces[i].colorcells






