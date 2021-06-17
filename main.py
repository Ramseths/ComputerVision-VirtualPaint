import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
# 1 para camaras externas, 0 para camara integrada
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
# 115 36 23 135 255 200
# Se crea la lista con los colores necesarios
lista_colores = [[115, 36, 23, 135, 255, 200]]

def encontrarColor(img, lista_colores):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in lista_colores:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        obtenerContornos(mask)
        #cv2.imshow(str(color[0]), mask)


def obtenerContornos(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    encontrarColor(img, lista_colores)
    cv2.imshow("Salida", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break