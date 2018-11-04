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
        cv2.imshow("Cube Section",imgRegions.get((0,0)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return imgRegions

    @classmethod
    def isBlue(cls, colorstats):
        b,g,r = colorstats
        return ((b > r) and (r == g) or (b == g) and (b > r) or (b > g) and (g > r) or (b > r) and (r > g))

    @classmethod
    def calulatecolorstats(cls, color):
        sum = color[0]+color[1]+color[2]
        return color[0]/sum, color[1]/sum,color[2]/sum


