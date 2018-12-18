from ColorPicker import PickColor
from ImageProcessing import ImageProcessing


class CubeFace:

    def __init__(self,image, faceID = -1):
        self.cp = PickColor()
        self.ip = ImageProcessing()
        self.faceID = faceID
        self.cells = [[None for i in range(0, 3)] for j in range(0, 3)]
        self.image = image
        #self.io.saveImages()[self.faceID] #change to recieve from elsewhere

    def setImage(self, image):
        self.cells = [[None for i in range(0, 3)] for j in range(0, 3)]
        self.image = image
        self.initFace()

    def setFaceID(self, faceID):
        self.faceID = faceID

    def initFace(self):
        cells = self.ip.splitImage(self.image)
        #print(np.shape(cells.get((0, 0))))
        for i in range(0, 3):
            for j in range(0, 3):
                self.cells[i][j] = self.cp.calculateColorinCell(cells.get((i, j)))






