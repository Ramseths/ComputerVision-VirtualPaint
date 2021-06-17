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
colores = [[255, 51, 51]]
puntos = []

def encontrarColor(img, lista_colores, colores):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    nuevoPunto = []
    for color in lista_colores:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = obtenerContornos(mask)
        cv2.circle(imgResult, (x, y), 10, colores[count], cv2.FILLED)
        if x != 0 & y != 0:
            nuevoPunto.append([x, y, count])
        count += 1
        #cv2.imshow(str(color[0]), mask)
    return  nuevoPunto


def obtenerContornos(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0 ,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w//2, y

def dibujar(puntos, colores):
    for punto in puntos:
        cv2.circle(imgResult, (punto[0], punto[1]), 10, colores[punto[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    nuevoPunto = encontrarColor(img, lista_colores, colores)
    if len(nuevoPunto) != 0:
        for nuPunto in nuevoPunto:
            puntos.append(nuPunto)
    if len(puntos) != 0:
        dibujar(puntos, colores)

    cv2.imshow("Salida", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break