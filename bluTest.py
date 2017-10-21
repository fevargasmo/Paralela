mport cv2
import numpy as np

img = cv2.imread('imagen.jpg')
height = np.size(img, 0)
width = np.size(img, 1)

print height
print width

#Kernel
n=6

for i in xrange(height):    
    for j in xrange(width):        
        for v in xrange(n):
            for color in range(3):
                total = 0
                p=1                
                if i-v <height:
                    total += int(img[i-v][j][color])
                    p+=1
                if i-v < height and j+v <width:
                    total += int(img[i-v][j+v][color])
                    p+=1
                if j+v < width:
                    total += int(img[i][j+v][color])
                    p+=1
                if i+v < height and j+v < width:
                    total += int(img[i+v][j+v][color])
                    p+=1
                if i+v < height:
                    total += int(img[i+v][j][color])
                    p+=1
                if i+v < height and j-v < width:
                    total += int(img[i+v][j-v][color])
                    p+=1
                if j-v < width:
                    total += int(img[i][j-v][color])
                    p+=1
                if i-v < height and j-v < width:
                    total += int(img[i-v][j-v][color])
                    p+=1

                
                img[i][j][color] = int(total)/p
                #print img[i][j][color]
                


cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
