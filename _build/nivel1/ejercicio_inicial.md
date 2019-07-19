---
redirect_from:
  - "/nivel1/ejercicio-inicial"
interact_link: content/nivel1/ejercicio_inicial.ipynb
kernel_name: python3
has_widgets: false
title: 'Experimentos'
prev_page:
  url: /nivel1/seccion1-1
  title: 'Un programa para leer'
next_page:
  url: /nivel1/seccion1-2
  title: 'Ambiente básico de trabajo'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Ejercicio de lectura

El siguiente es el programa completo en Python presentado en la sección anterior. Dependiendo de la configuración del servidor en la que usted esté leyendo este texto, usted podría tener la opción de ejecutar y editar el programa.





<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
# Este programa está escrito en el archivo perimetro.py


def perimetro_triangulo(cateto1: float, cateto2: float) -> float:
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


def calcular_hip(cateto1: float, cateto2: float) -> float:
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
    suma_cuadrados = (cateto1**2) + (cateto2**2)

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
perimetro = perimetro_triangulo(3, 4)

# Mostrarle al usuario el resultado de la operación
print("El perímetro de un triángulo rectángulo que tenga catetos de longitud",
      cat_1, "y", cat_2, "es", perimetro)

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
Indique la longitud del primer cateto: 3
Indique la longitud del segundo cateto: 4
El perímetro de un triángulo rectángulo que tenga catetos de longitud 3.0 y 4.0 es 12.0
```
</div>
</div>
</div>

