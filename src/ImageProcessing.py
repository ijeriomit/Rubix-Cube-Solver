import numpy as np
import cv2
class ImageProcessing:
    #redboundary =
    #blueboundary =
    #yellowboundary =
    #whiteboundary =
    #orangeboundary =
    #greenboundary =
    @classmethod
    def splitImage(cls,image):
        imgRegions = dict()
        height,width = np.size(image,0),np.size(image,1)
        print(height,width)
        for i in range(0,3):
            yupperbound = int((i+1) * (height / 3))
            ylowerbound = int(yupperbound - (height / 3))
            print("YL: ", ylowerbound, "YU: ", yupperbound)
            for j in range(0,3):
                xupperbound = int((j+1)*(width/3))
                xlowerbound = int(xupperbound-(width/3))
                print("XL: ", xlowerbound, "XU: ", xupperbound)
                imgRegions[(i,j)] = image[ylowerbound:yupperbound,xlowerbound:xupperbound]
        return imgRegions
