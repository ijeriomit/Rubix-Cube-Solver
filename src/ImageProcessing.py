import numpy as np
import cv2


def displayImage(windowname, image):
    cv2.imshow(windowname, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class ImageProcessing:

    def __init__(self):
        self.imageCells = dict()


    def splitImage(self, image):
        height, width = np.size(image, 0), np.size(image, 1)
        splitimage = dict()
        for i in range(0, 3):
            yupperbound = int((i+1) * (height / 3))
            ylowerbound = int(yupperbound - (height / 3))
            for j in range(0, 3):
                xupperbound = int((j + 1) * (width / 3))
                xlowerbound = int(xupperbound-(width / 3))
                splitimage[(i, j)] = image[ylowerbound:yupperbound, xlowerbound:xupperbound]
        return splitimage

    def saveCells(self, image):
        self.imageCells = self.splitImage(image)




