# Estilo de programación

```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```

```{admonition} Objetivo de la sección
El objetivo de esta sección es introducir algunos elementos que no son obligatorios al programar pero que hacen el código mucho más comprensible y fácil de mantener.
```

En las secciones anteriores hemos empezado a estudiar la *sintaxis* de Python, es decir las reglas que define el lenguaje y que deben respetarse en todos los programas que se escriban con él: si las reglas sintácticas no se cumplen, el intérprete de Python no podrá entender lo que quiere decir el programa y no podrá ejecutarlo. Sin embargo, la sintaxis no lo es todo en un lenguaje de programación. También es importante pensar en el *estilo*. 

Si bien las reglas de Python parecen muy estrictas, hay infinidad de formas diferentes en las que se puede escribir el mismo programa. Esto incluye desde cambios menores, como incluir líneas en blanco o comentarios adicionales, hasta cambiar la descomposición en funciones, pasando por cambios en los nombres de las variables y de las funciones. Es decir que dos personas que escriban el mismo programa Python pueden terminar escribiendo programas muy diferentes sólo por utilizar un *estilo* diferente.

El problema con esta gran libertad es que las decisiones que tomemos con respecto al *estilo* del código que escribamos hoy posiblemente nos van a acompañar durante mucho tiempo. La mayoría de los programas se escriben en un tiempo relativamente corto (días o semanas) y luego se utilizan, se corrigen y se actualizan durante meses o años. Si hoy tomamos decisiones que parecen fáciles (como utilizar nombres de variables cortísimos o no descomponer una función muy complicada), es posible que más adelante sea más difícil arreglar un problema porque no podremos entender con facilidad nuestro propio código. 


```{epigraph}
Any fool can write code that a computer can understand. Good programmers write code that humans can understand.

-- Martin Fowler
```



Para ilustrar este punto, revisemos el siguiente programa basado en las funciones que usamos en la sección anterior:


```{code-block} python
---
lineno-start: 1
---
def area_cuadrado(lado: int)-> int:
    """
       Calcula el área de un cuadrado dada la medida de su lado
    """
    return lado * lado


def area_triangulo(base: int, altura: int)-> float:
    """
        Calcula el área de un triángulo dada la medida de la base y de la altura.
    """   
    return (base * altura) / 2


def area_casa(frente: int, techo: int)-> float:
    """
        Calcula el área del dibujo de una casa que se forma con un cuadrado
        y un triángulo encima (el techo).
        El frente de la casa será igual al lado del cuadrado y a la base del triángulo.
        La altura del techo será la altura del triángulo.
    """
    cuadrado = area_cuadrado(frente)
    triangulo = area_triangulo(frente, techo)
    return cuadrado + triangulo

print(area_casa(10, 5))
```

Ahora revisemos un segundo programa:

```{code-block} python
---
lineno-start: 1
---
def f(b, c):
    v = (b * b) + (b * c)/2
    return v
    
print(f(10, 5))    
```

Aunque a primera vista no es evidente, los dos programas son equivalentes en el sentido de que al ejecutarlos el resultado será el mismo: imprimirán el valor `125.0` en la consola. Evidentemente el segundo programa es mucho más corto que el primero, pero esto no necesariamente es una ventaja. Particularmente, en este caso es difícil entender que la función `f` sirve para calcular el área del dibujo de la casa y requiere como parámetro las medidas del frente y del techo, en ese orden. 

Podemos decir que las diferencias entre los dos programas se reducen a los siguientes 5 aspectos:

1. Utilizar nombres claros para las variables, las funciones y los parámetros.
2. Documentar el objetivo de cada función
3. Descomponer las funciones para que cumplan objetivos precisos
4. Complejidad de las instrucciones
5. Indicar los tipos de los parámetros y retornos de las funciones

A continuación revisaremos cada uno de estos puntos con un poco más de detalle.

## Nombramiento de variables y funciones

Uno de los factores que más incide en la facilidad para comprender un programa es la selección de nombres para variables y funciones: si el nombre que utilizamos para una variable o una función es bueno, no tendremos que pensar mucho para recordar qué rol tiene dentro del programa y podremos concentrarnos en los aspectos importantes.

En el ejemplo que presentamos antes podemos ver esto claramente:

```{code-block} python
---
lineno-start: 1
emphasize-lines: 2, 5
---
def area_triangulo(base: int, altura: int)-> float:
    return (base * altura) / 2

def g(b, c):
    return (b * c)/2
```

Las dos funciones anteriores hacen los mismos cálculos, 



```{admonition} Tip
:class: tip
Para las variables, utilice nombres que indiquen con claridad qué es lo que va a guardar dentro de ellas. Evite nombres cortos a menos que no haya ninguna ambigüedad posible.
```

```{admonition} Tip
:class: tip
Para las funciones, utilice nombres que indiquen qué es lo que hará la función. 
Incluya verbos en los nombres de funciones (ej. `guardar_resultado` ), a menos que se pueda sobreentender con facilidad (ej. `calcular_area_triangulo` vs. `area_triangulo`).
```

estándares (snake_case, mayúsculas, minúsculas)


## Documentación de funciones

docstring

## Descomposición de funciones


## Complejidad de las instrucciones


## Tipado de funciones

Sobre los *type-hints*

Si usted utiliza otros libros o si consulta en Internet, es muy posible que se encuentre con definiciones de funciones en las que no aparecen los tipos de los parámetros ni el tipo de los resultados. Esto se debe a que en Python el uso de estos elementos es opcional. De hecho, el nombre específico de estos elementos es *type-hints* y las herramientas (IDE, intérprete, compilador, etc.) los utilizan sólo como sugerencias.

En este libro vamos a usar *type-hints* en la definición de todas las funciones y esperamos que usted haga uso de ellos también. Por una parte, esto le facilitará aprender a usar otros lenguajes de programación como C, C++, Java, o TypeScript. Por otro lado, razonar sobre los tipos de datos debería ayudarlo a estructurar mejor sus programas, especialmente mientras adquiere una cierta destreza programando.


## Ejercicios

1. Revise detenidamente la siguiente función para descubrir su objetivo. Reescríbalo aplicando las recomendaciones que se estudiaron en esta sección.

```{code-block} python
def vc(r, a) :
    b = 3.14159 * (r**2)
    return round(b * a,2)
```

2. Revise detenidamente la siguiente función para descubrir su objetivo. Reescríbalo aplicando las recomendaciones que se estudiaron en esta sección.

```{code-block} python
def v(d):
    vf = (2*9.8*d)**(1/2)
    return vf
```


## Más allá de Python

Estándares de documentación

La discusión sobre los *type-hints* tiene que ver con una discusión mucho más extensa sobre la conveniencia de tener *tipado dinámico* en los lenguajes de programación. Por un lado, cuando los lenguajes son fuertemente tipados se cometen menos errores o, al menos, las herramientas de edición capturan más errores de forma temprana. Por otro lado, cuando el tipado es dinámico los errores de tipo se capturan en tiempo de ejecución, pero el desarrollo de los programas es más rápido. En este momento hay fuertes discusiones sobre la conveniencia o no de cada sistema, pero hay un hecho que encontramos muy diciente: JavaScript, que tiene tipado dinámico, está incluyendo progresivamente más elementos para escribir programas fuertemente tipados (el crecimiento de TypeScript es evidencia indiscutible), mientras que Python está empezando a incluir elementos para poder incluir verificaciones de tipos.

PEP8

PEP8 -- Style Guide for Python Code: <https://www.python.org/dev/peps/pep-0008/>

