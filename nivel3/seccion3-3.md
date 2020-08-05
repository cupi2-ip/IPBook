```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```



# Listas

```{admonition} Objetivo de la sección
El objetivo de esta sección es ...
```

Intro: un tipo de secuencia, mutable


## El tipo list en Python

crear: list() + append, [], list(range), *

indexar: [i]

```python
def imprimir_elementos(lista: list) -> None:
  i = 0
  while i < len(lista):
	print(i, "->", lista[i])
	i += 1  
```

ejemplo: calcular el promedio de los elementos de una lista


## Modificar listas

append
insert
eliminar: remove, del
copy

OJO: mutabilidad!
Referencias vs valores



## Funciones, métodos y operadores interesantes

len
min
max

in

==
<
>

count
index
sort
reverse


## Split & Join

## Listas complejas

### Listas de listas
una lista de estudiantes, donde cada uno es una lista que tiene un nombre y una nota

### Listas de diccionarios
Una lista de actividades, donde cada actividad es un diccionario con tres llaves: actividad, curso y nota

### Diccionario con listas

Un diccionario donde las llaves son actividades y los valores son listas con las notas de los estudiantes en esa actividad. Podemos tener también una lista con los nombres de las actividades para no tener que recorrer el diccionario



## Ejercicios ##

1. Crear una lista sólo con números pares

2. Crear una lista con los números invertidos
3. Crear una lista con números aleatorios
4. Usar split para contar las palabras en mayúscula de una frase
5. En cuántas palabras aparece una determinada cadena
6. Insertar un elemento dentro de una lista que esté ordenada
7. Calcular el promedio de las notas de un estudiante
8. Encontrar la actividad con mayor nota promedio
9. Eliminar los elementos del principio y el final hasta que la suma del primero y del último tenga una cierta propiedad


## Más allá de Python

Además de ...
 


