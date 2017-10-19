import cv2
import sys
import threading
import logging
import time


def bluring(Imagen, PY, PX, BYm, BXm):
    Img = Imagen
    for i in range(PY):
        for j in range(PX):
            R = int(Imagen[i][j][0])
            G = int(Imagen[i][j][1])
            B = int(Imagen[i][j][2])
            if i - BYm + 1 < 0:
                pass
            elif i + BYm + 1 > PY:
                pass
            elif j - BXm + 1 < 0:
                pass
            elif j + BXm + 1 > PX:
                pass
            else:
                for k in range(BXm):
                    R += int(Imagen[i][j + k][0]) + int(Imagen[i][j - k][0])
                    G += int(Imagen[i][j + k][1]) + int(Imagen[i][j - k][1])
                    B += int(Imagen[i][j + k][2]) + int(Imagen[i][j - k][2])
                for k in range(BYm):
                    R += int(Imagen[i + k][j][0]) + int(Imagen[i - k][j][0])
                    G += int(Imagen[i + k][j][1]) + int(Imagen[i - k][j][1])
                    B += int(Imagen[i + k][j][2]) + int(Imagen[i - k][j][2])
                R /= ((BXm * 4) - 1)
                G /= ((BXm * 4) - 1)
                B /= ((BXm * 4) - 1)
            Img[i][j][0] = R
            Img[i][j][1] = G
            Img[i][j][2] = B
    return Img


def blur(Imagen, LongitudBuffer, NumeroHilos):
    BX = LongitudBuffer[0]
    BY = LongitudBuffer[1]
    PY = len(Imagen) - 1
    PX = len(Imagen[0]) - 1

    BXm = int((BX - 1) / 2)
    BYm = int((BY - 1) / 2)

    Imagen = bluring(Imagen, PY, PX, BYm, BXm)
    return Imagen


def main(argv):
    if len(argv) > 1:
        print(argv)
        bx, by = 3, 3
        h = 1
        if argv[1] == "-i":
            Imagen = cv2.imread(argv[2])
        if argv[3] == "-bx":
            bx = int(argv[4])
        if argv[5] == "-bx":
            by = int(argv[6])

        if argv[7] == "-bx":
            h = int(argv[8])
        Imagen = blur(Imagen, [bx, by], h)
        #Imagen = cv2.blur(Imagen, (bx,by))
        
        cv2.imshow('imagen', Imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Uso: \n\t python blur.py -i 'img.jpg' \n")
        print("\tEjemplo: \n\t\t python blur.py - \n")


if __name__ == '__main__':
    main(sys.argv)
