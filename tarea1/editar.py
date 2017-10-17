import cv2
import numpy as np

img = cv2.imread('imagen.jpg')

for i in xrange(340):
    if (i >0 and i < 339):
        for j in xrange(514):
            if j>0 and j < 513:
                img[i][j][0] =  (int(img[i][j][0]) + int(img[i-1][j][0]) + int(img[i][j+1][0]) + int(img[i+1][j][0]) + int(img[i][j-1][0]))/5
                img[i][j][1] =  (int(img[i][j][1]) + int(img[i-1][j][1]) + int(img[i][j+1][1]) + int(img[i+1][j][1]) + int(img[i][j-1][1]))/5
                img[i][j][2] =  (int(img[i][j][2]) + int(img[i-1][j][2]) + int(img[i][j+1][2])+ int(img[i+1][j][2]) + int(img[i][j-1][2]))/5

cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()