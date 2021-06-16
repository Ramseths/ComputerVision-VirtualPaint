import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
# 1 para camaras externas, 0 para camara integrada
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

# Se crea la lista con los colores necesarios
lista_colores = [[5, 107, 0, 19, 255, 255],
                 [133, 56, 0, 159, 156, 255],
                 [57, 76, 0, 100, 255, 255]]

def encontrarColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("Mask", mask)

while True:
    success, img = cap.read()
    cv2.imshow("Salida", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break