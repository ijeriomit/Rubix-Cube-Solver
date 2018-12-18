import numpy as np
import cv2


def displayImage(windowname, image):
    cv2.imshow(windowname, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class ImageProcessing:

    def splitImage(self, image):
        height, width = np.size(image, 0), np.size(image, 1)
        splitimage = dict()
        for i in range(0, 3):
            ybounds = self.getBounds(i, height)
            for j in range(0, 3):
                xbounds = self.getBounds(j, width)
                splitimage[(i, j)] = image[ybounds[0]:ybounds[1], xbounds[0]:xbounds[1]]
        return splitimage

    def getBounds(self, val, dimension):
        return int((val + 1) * (dimension / 3)-(dimension / 3)), int((val + 1) * (dimension / 3))




