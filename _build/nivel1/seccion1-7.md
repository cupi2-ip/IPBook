---
title: 'Un programa para leer (2)'
prev_page:
  url: /nivel1/seccion1-6.html
  title: 'Definición de funciones'
next_page:
  url: /nivel1/seccion1-8.html
  title: 'Lógica vs. Interacción'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|



# Un programa para leer (2)

Volvemos ahora al programa completo que usted leyó al inicio del capítulo. Vuelva a leerlo detenidamente: todo lo que aparece en este programa ya lo estudiamos y usted debería estar en capacidad de entenderlo.


```python
# Este programa está escrito en el archivo perimetro.py

def perimetro_triangulo(cateto1: float, cateto2: float)->float:
    """
    Esta función calcula el perímetro de un triángulo rectángulo
    dada la longitud de sus dos catetos
    Parámetros:
      cateto1 (float): la longitud del primer cateto del triángulo
      cateto2 (float): la longitud del segundo cateto del triángulo
    Retorno
      (float): la longitud del perímetro del triángulo
    """
    # Usar la función calcular_hip para calcular la longitud del lado faltante
    hipotenusa = calcular_hip(cateto1, cateto2)
    
    # Sumar los tres lados y convertirlos en la respuesta de la función
    return cateto1 + cateto2 + hipotenusa


def calcular_hip(cateto1: float, cateto2: float)->float:
    """
    Esta función calcula la longitud de la hipotenusa en un triángulo rectángulo
    dada la longitud de sus dos catetos
    Parámetros:
      cateto1 (float): la longitud del primer cateto del triángulo
      cateto2 (float): la longitud del segundo cateto del triángulo
    Retorno
      (float): la longitud de la hipotenusa
    """
    # Sumar la longitud de los catetos elevados al cuadrado
    suma_cuadrados = (cateto1 ** 2) + (cateto2 ** 2)
    
    # Calcular la raiz cuadrada de la suma usando la función pow y el exponente 0.5
    hipotenusa = pow(suma_cuadrados, 0.5)
    return hipotenusa


# Solicitarle al usuario la longitud de los dos catetos
cadena_cat_1 = input("Indique la longitud del primer cateto: ")
cadena_cat_2 = input("Indique la longitud del segundo cateto: ")

# Convertir los caracteres dados por el usuario en un número decimal
cat_1 = float(cadena_cat_1)
cat_2 = float(cadena_cat_2)

# Llamar a la función con los valores recibidos
perimetro = perimetro_triangulo(3,4)

# Mostrarle al usuario el resultado de la operación
print("El perímetro de un triángulo rectángulo que tenga catetos de longitud", cat_1, "y", cat_2, "es", perimetro)

```

**Preguntas:**
A partir de su lectura del programa, intente responder las siguientes preguntas.

* ¿Cuál es el objetivo del programa?
* ¿Qué información tendrá que suministrar el usuario que ejecute el programa?
* ¿Cuál es el objetivo de cada bloque?
* ¿Qué es lo que primero se ejecuta?
* ¿Cuál es la diferencia entre las cosas que están escritas en español y las que están escritas en inglés?
* ¿Cuáles son los valores que tiene que proporcionar el usuario?
* ¿Qué ve el usuario al finalizar la ejecución?


## Ejercicios

1. Copie el programa a su computador y ejecútelo. Hágale modificaciones y observe los cambios que se producen en sus resultados.

2. Escriba un programa completo que le pida al usuario la temperatura actual en grados Celsius y le informe cuál es esa temperatura en Fahrenheit.

3. Observe la siguiente figura:

![Ejercicio Área](images/area.png)

Construya un programa que le pida al usuario la medida del lado del cuadrado y le informe al usuario el tamaño del área de la zona negra.