# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:34:54 2024

@author: Efrain Jimenez M
"""

import cv2
import numpy as np

imagen=cv2.imread("xray_neck.jpeg")

imagen1=imagen.copy()
imagen2=imagen.copy()
imagen3=imagen.copy()
imagen1[:,:,2]+=5
imagen1[:,:,1]+=50    #Edicion de imagen no#1
imagen2[:,:,1]+=60    #Edicion de imagen no#2
imagen3[:,:,2]+=60    #Edicion de imagen no#3

def whitepatch(image):
    m,n,c=image.shape
    # Copia de la imagen de entrada
    imagenc = image.copy().astype(np.float32)
    
    # Normaliza la imagen a valores entre 0 y 1
    imagenc /= 255.0
    
    # Calcula la media de cada canal de color
    mean_b = np.mean(imagenc[:, :, 0])
    mean_g = np.mean(imagenc[:, :, 1])
    mean_r = np.mean(imagenc[:, :, 2])
    
    # Calcula el factor de ajuste para cada canal
    factor_b = 255 / mean_b
    factor_g = 255 / mean_g
    factor_r = 255 / mean_r
    
   
    for x in range(m):
        for y in range(n):
            imagenc[x,y,0]=imagenc[x,y,0]*factor_b
            imagenc[x,y,1]=imagenc[x,y,1]*factor_g
            imagenc[x,y,2]=imagenc[x,y,2]*factor_r
    
    # Convierte la imagen de nuevo al tipo de datos uint8
    imagenc = np.clip(imagenc, 0, 255).astype(np.uint8)
    
    return imagenc

def mostrar(img):
    cv2.imshow("imagen", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

def clasificador(imagen):
    m,n,c=imagen.shape  #Lo convierte a matriz
    imagen_b=np.zeros((m,n))  #Pone la imagen en puros ceros y hace que se haga negra
    imagen_b /= 255.0
    for x in range(m):
        for y in range(n):
            if imagen[x,y,0]<230:  #De forma BGR
                imagen_b[x,y]=255  #Va poniendo de blanco los pixeles que encuentra
                
                
    # Convierte la imagen de nuevo al tipo de datos uint8
    imagen_b = np.clip(imagen_b, 0, 255).astype(np.uint8)
    
    return imagen_b    

imagencls1 = clasificador(imagen1)
imagencls2 = clasificador(imagen2)
imagencls3 = clasificador(imagen3)
img1 = whitepatch(imagen1)
img2 = whitepatch(imagen2)
img3 = whitepatch(imagen3)
imgcls1 = clasificador(img1)
imgcls2 = clasificador(img2)
imgcls3 = clasificador(img3)

cv2.imshow("imagen1", imagen1)
cv2.imwrite("imagen1.jpg", imagen1)
cv2.imshow("imagen2", imagen2)
cv2.imwrite("imagen2.jpg", imagen2)
cv2.imshow("imagen3", imagen3)
cv2.imwrite("imagen3.jpg", imagen3)
cv2.imshow("imagen1_1", imagencls1)
cv2.imwrite("imagen1_1.jpg", imagencls1)
cv2.imshow("imagen2_2", imagencls2)
cv2.imwrite("imagen2_2.jpg", imagencls2)
cv2.imshow("imagen3_3", imagencls3)
cv2.imwrite("imagen3_3.jpg", imagencls3)
cv2.imshow("imagen1_1_1", img1)    #rgba(255,255,232,255)
cv2.imwrite("imagen1_1_1.jpg", img1)
cv2.imshow("imagen2_2_2", img2)    #rgba(254,240,255,255)
cv2.imwrite("imagen2_2_2.jpg", img2)
cv2.imshow("imagen3_3_3", img3)    #rgba(255,255,255,255)
cv2.imwrite("imagen3_3_3.jpg", img3)
cv2.imshow("imagen1_1_1_1", imgcls1)
cv2.imwrite("imagen1_1_1_1.jpg", imgcls1)
cv2.imshow("imagen2_2_2_2", imgcls2)
cv2.imwrite("imagen2_2_2_2.jpg", imgcls2)
cv2.imshow("imagen3_3_3_3", imgcls3)
cv2.imwrite("imagen3_3_3_3.jpg", imgcls3)
cv2.waitKey()
cv2.destroyAllWindows()

