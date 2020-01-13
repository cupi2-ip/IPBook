import random

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def cargar_imagen_matriz(ruta_imagen: str)-> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz de MxNx3
    """
    imagen = mpimg.imread(ruta_imagen)
    return imagen

def visualizar_imagen_matriz(imagen: list) -> None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list): Matriz de MxNx3 que representa la imagen a visualizar.
    """
    plt.imshow(imagen)
    plt.show()

imagen = cargar_imagen_matriz("muestra.jpg")
visualizar_imagen_matriz(imagen)


def visualizar_imagen(imagen: list) -> None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list): Matriz de MxN con tuplas (R,G,B) que representan la imagen a visualizar.
    """
    alto = len(imagen)
    ancho = len(imagen[0])
    matriz = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            r, g, b = imagen[i][j]
            fila.append([r, g, b])
        matriz.append(fila)
    plt.imshow(matriz)
    plt.show()


def cargar_imagen(ruta_imagen: str)-> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz de MxN con tuplas (R,G,B).
    """
    matriz = mpimg.imread(ruta_imagen).tolist()
    alto = len(matriz)
    ancho = len(matriz[0])
    imagen = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            r = matriz[i][j][0]
            g = matriz[i][j][1]
            b = matriz[i][j][2]
            tupla = (r, g, b)
            fila.append(tupla)
        imagen.append(fila)
    return imagen




def generar_imagen_negra(ancho: int)->list:
  imagen = []
  for i in range(0, ancho):
    fila = []
    for j in range(0, ancho):
      rojo = 0.0
      verde = 0.0
      azul = 0.0
      pixel = (rojo, verde, azul)
      fila.append(pixel)
    imagen.append(fila)
  return imagen


def generar_imagen_tuplas(ancho: int)->list:
  factor = 1/ancho
  imagen = []
  for i in range(0, ancho):
    fila = []
    for j in range(0, ancho):
      rojo = random.randint(0, i)/ancho
      verde = random.randint(0, j)/ancho
      azul = max(0,1 - rojo - verde)
      pixel = (rojo*255, verde*255, azul*255)
      fila.append(pixel)
    imagen.append(fila)
  return imagen


def generar_imagen(ancho: int)->list:
  factor = 1/ancho
  imagen = []
  for i in range(0, ancho):
    fila = []
    for j in range(0, ancho):
      rojo = random.randint(0, i)/ancho
      verde = random.randint(0, j)/ancho
      azul = max(0,1 - rojo - verde)
      pixel = (rojo, verde, azul)
      fila.append(pixel)
    imagen.append(fila)
  return imagen


def convertir_a_grises(imagen: list)->None:
  alto = len(imagen)
  ancho = len(imagen[0])
  for i in range(0, alto):
    for j in range(0, ancho):
      rojo, verde, azul = imagen[i][j]
      gris = (rojo + verde + azul) // 3
      imagen[i][j] = (gris, gris, gris)
  

def binarizar(imagen: list, umbral: int)->None:
  alto = len(imagen)
  ancho = len(imagen[0])
  for i in range(0, alto):
    for j in range(0, ancho):
      rojo, verde, azul = imagen[i][j]
      gris = (rojo + verde + azul) // 3
      if gris < umbral:
      	imagen[i][j] = (0,0,0)
      else:
        imagen[i][j] = (255,255, 255)  

def copiar_imagen(imagen: list)->list:
  copia = []
  alto = len(imagen)
  for i in range(0, alto):
    fila = imagen[i]
    nueva_fila = fila.copy()
    copia.append(nueva_fila)
  return copia


def sharpening(imagen: list)->None:
  mascara = [[-1, -1, -1],[-1, 9, -1], [-1, -1, -1]]
  copia = copiar_imagen(imagen)
  alto = len(imagen)
  ancho = len(imagen[0])
  for i in range(1, alto-1):
    for j in range(1, ancho-1):
      rojo, verde, azul = (0,0,0)
      for i_mascara in range(-1, 2):
        for j_mascara in range(-1, 2):          
          rojo_vecino, verde_vecino, azul_vecino = imagen[i+i_mascara][j+j_mascara]
          valor_mascara = mascara[i_mascara][j_mascara]
          rojo += rojo_vecino * valor_mascara
          verde += verde_vecino * valor_mascara
          azul += azul_vecino * valor_mascara
      nuevo_pixel = (rojo, verde, azul)    
      copia[i][j] = nuevo_pixel
  return copia

def sumar(imagen, copia)->None:
  alto = len(imagen)
  ancho = len(imagen[0])
  for i in range(0, alto):
    for j in range(0, ancho):
      rojo1, verde1, azul1 = imagen[i][j]   
      rojo2, verde2, azul2 = copia[i][j] 
      if rojo2 != 0 and verde2 != 0 and azul2 != 0:
        imagen[i][j] = ( rojo1, verde1, azul1)
      else:
        imagen[i][j] = ( rojo1//2, verde1//2, azul1//2)

"""
imagen = generar_imagen(100)
visualizar_imagen(imagen)
convertir_a_grises(imagen)
visualizar_imagen(imagen)
"""
#imagen = cargar_imagen("muestra.jpg")
#visualizar_imagen(imagen)
# convertir_a_grises(imagen)
#copia = sharpening(imagen)
#copia2 = sharpening(copia)
#copia3 = sharpening(copia2)
#copia4 = sharpening(copia3)
# binarizar(imagen, 50)
# binarizar(copia, 3)
#visualizar_imagen(copia)
#visualizar_imagen(copia2)
#visualizar_imagen(copia3)
#visualizar_imagen(copia4)

#sumar(imagen, copia)
#visualizar_imagen(imagen)



