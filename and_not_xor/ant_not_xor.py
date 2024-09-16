# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:03:08 2024

@author: Efrain Jimenez M
"""

import cv2
import numpy as np

img1 = cv2.imread('xray_neck.jpeg', cv2.IMREAD_GRAYSCALE)

# Verificar si la imagen fue cargada correctamente
if img1 is None:
    print("Error: No se pudo cargar la imagen.")
    exit()

# Crear una segunda máscara para la operación lógica
# Podrías usar una imagen diferente o crear una región de interés (en este caso, un círculo)
img2 = np.zeros_like(img1)
img2 = cv2.circle(img2, (img1.shape[1]//2, img1.shape[0]//2), 100, (255), -1)  # Un círculo en el centro


#AND
AND = cv2.bitwise_and(img1, img2)
cv2.imshow('AND', AND)
#OR
OR = cv2.bitwise_or(img1, img2)
cv2.imshow('OR',OR)
#NOT
NOT = cv2.bitwise_not(img1)
cv2.imshow('NOT', NOT)
#XOR
XOR = cv2.bitwise_xor(img1, img2)
cv2.imshow('XOR', XOR)

cv2.imwrite('img1.jpg', img1)
cv2.imwrite('img2.jpg', img2)
cv2.imwrite('and.jpg', AND)
cv2.imwrite('OR.jpg', OR)
cv2.imwrite('NOT.jpg', NOT)
cv2.imwrite('XOR.jpg', XOR)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()