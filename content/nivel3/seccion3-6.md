Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Más algorítmica

> El objetivo de esta sección es ...

> Complexity has and will maintain a strong fascination for many people. It is true that we live in a complex world and strive to solve inherently complex problems, which often do require complex mechanisms. However, this should not diminish our desire for elegant solutions, which convince by their clarity and effectiveness. Simple, elegant solutions are more effective, but they are harder to find than complex ones, and they require more time, which we too often believe to be unaffordable
> 
> Niklaus Wirth 

Introducción a la algorítmica:
 - Siempre hay varias opciones
 - Recetas
 - Arsenal propio


## Recorridos totales

while, for-in

sumar todos los elementos

cuántos hay que ....


## Recorridos parciales

while, no for-in

buscar un elemento

hay alguno que ...
Ej: hay una vocal mayúscula en esta cadena

```python
def hay__vocal_mayuscula(cadena: str) -> bool:
  hay_mayuscula = False
  i = 0
  while i < len(cadena) and not hay_mayuscula:
    letra_i = cadena[i]
    if letra_i in "AEIOU":
      hay_mayuscula = True
    else:
      i += 1
  
  return hay_mayuscula
```

Ej 2: en qué posición aparece la primera mayúscula



## Recorridos dobles

 totales
 parciales

hay repetidos
contar repetidos

Ej 2: en qué posiciones hay la vocales mayúsculas


## Recorridos con acumulaciones

promedio

mayor

histograma


## Soluciones recurrentes


### Contar

*Cuál es el problema base*

*Sólución típica*

*Problemas relacionados*

### Buscar

*Cuál es el problema base*
en qué posición está el primero que cumple

*Sólución típica*

*Problemas relacionados*
si hay
si todos cumplen
todos los que cumplen

### Encontrar el mayor / menor

*Cuál es el problema base*

*Sólución típica*

*Problemas relacionados*

### Contar apariciones (histograma)

*Cuál es el problema base*

*Sólución típica*

*Problemas relacionados*


### Filtrar

*Cuál es el problema base*

*Sólución típica*

*Problemas relacionados*


### Map

*Cuál es el problema base*

*Sólución típica*

*Problemas relacionados*






## Ejercicios ##

1. Buscar el segundo mayor

2. Hay dos seguidos tales que

3. Están ordenados

4. Hay dos que sumen al menos X

5. Hay tres que sumen exactamente X

6. Buscar mediana: contar cuántos menores que cada uno

7. Contar inversiones: distancia entre ...

8. Es anagrama

9. 


## Más allá de Python

Además de ...
 

#### Notas 

