# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:27:47 2024

@author: Efrain Jimenez M
"""

import cv2
import numpy as np

# Cargar la imagen médica (por ejemplo, un rayos X) en escala de grises
imagen = cv2.imread("resonancia_brain.jpg", 0) 

# Definir un filtro de detección de bordes (Kernel Sobel horizontal)
Kernel = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

# Obtener el tamaño de la imagen
m, n = imagen.shape

# Crear una imagen vacía del mismo tamaño para almacenar el resultado filtrado
filtrada = np.zeros_like(imagen)

# Aplicar la convolución (filtro de detección de bordes)
for x in range(m - 2):
    for y in range(n - 2):
        res = np.sum(imagen[x:x+3, y:y+3] * Kernel)
        if abs(res) > 50:
            filtrada[x, y] = 255

# Mostrar la imagen original (Rayos X)
cv2.imshow("Imagen Original - Rayos X", imagen)

# Mostrar la imagen filtrada que resalta bordes y contornos
cv2.imshow("Imagen Filtrada - Detección de Bordes", filtrada)

# Guardar la imagen filtrada
cv2.imwrite("rayos_x_filtrada.jpg", filtrada)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()
