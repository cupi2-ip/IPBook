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
    """ Calcula el área de un cuadrado dada la medida de su lado
    Parámetros:
        lado (int): La medida del cuadrado
    Retorno:
        (int): El valor del área del cuadrado. Es siempre un número entero.
    """
    return lado * lado


def area_triangulo(base: int, altura: int)-> float:
    """ Calcula el área de un triángulo.
    Parámetros:
        base (int): La medida de la base del triángulo.
        altura (int): La medida de la altura del triángulo.        
    Retorno:
        (float): El valor del área del triángulo. Es siempre un número decimal.    
    """   
    return (base * altura) / 2


def area_casa(frente: int, techo: int)-> float:
    """ Calcula el área del dibujo de una casa que se forma con un cuadrado
        y un triángulo encima (el techo).
        El frente de la casa será igual al lado del cuadrado y a la base del triángulo.
        La altura del techo será la altura del triángulo.
    Parámetros:
        frente (int): La medida del frente de la casa.
        techo (int): La medida de la altura del techo de la casa.        
    Retorno:
        (float): El valor del área del dibujo de la casa.        
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

Aunque a primera vista no es evidente, los dos programas son equivalentes en el sentido de que al ejecutarlos el resultado será el mismo: imprimirán el valor `125.0` en la consola. Evidentemente el segundo programa es mucho más corto que el primero, pero esto no necesariamente es una ventaja. En este caso es difícil entender que la función `f` sirve para calcular el área del dibujo de la casa y requiere como parámetro las medidas del frente y del techo, en ese orden. 

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

Un segundo aspecto para facilitar el uso de nuestro código es documentar las funciones con un comentario que le sirva a potenciales usuarios o a nosotros mismos. De esta forma no será necesario estudiar con detenimiento el cuerpo de la función para saber qué hace.

Para cada función usualmente queremos saber 4 cosas:

1. cuál es su objetivo
2. cómo se debe usar
3. qué pasará cuando se use
4. cómo deben usarse y qué representan los parámetros

En Python el comentario con múltiples líneas que se encuentre justo después de la signatura de una función es considerado la documentación de la función. Esto usualmente se conoce como el `docstring` de una función y tiene una característica muy importante: cuando busquemos ayuda sobre una función, usando la función nativa `help`, recibiremos el `docstring`. Veamos un ejemplo en el que primero definiremos una nueva función y especificaremos su `docstring`.

```{code-block} python
---
lineno-start: 1
---
def area_triangulo(base: int, altura: int)-> float:
    """ Calcula el área de un triángulo a partir de su base y su altura.
        Tanto la base como la altura deben ser números enteros.
        El resultado es un número decimal aunque los parámetros sean enteros.
    """
    return (base * altura) / 2
```

Si después de definir nuestra función invocamos la función nativa `help` usando nuestra función como parámetro, obtendremos la documentación que especificamos.

```
>>> help(area_triangulo)
Help on function area_triangulo in module __main__:

area_triangulo(base: int, altura: int) -> float
    Calcula el área de un triángulo a partir de su base y su altura.
    Tanto la base como la altura deben ser números enteros.
    El resultado es un número decimal aunque los parámetros sean enteros.
```

Ahora bien, a diferencia de otros lenguajes Python no especifica cómo deben especificarse los detalles de una función: sólo nos da el espacio para que escribamos la documentación y nos da total libertad para que nosotros decidamos qué aspectos queremos documentar. Es nuestra responsabilidad decidir qué incluir y asegurarnos de que la documentación sea suficiente para que alguien más pueda usar nuestra función. También es nuestra responsabilidad definir cómo vamos a organizar la información para que esté organizada y sea fácil de encontrar y utilizar.

Toda esta libertad que da el lenguaje ha llevado a que existan varios estándares para documentar las funciones sin que ninguno sea claramente superior a los otros. Aunque le recomendamos que más adelante escoja uno de los estándares, por ahora le recomendamos utilizar la versión simplificada que se ilustra en el siguiente ejemplo:

```{code-block} python
---
lineno-start: 1
---
    """ Calcula el área de un triángulo a partir de su base y su altura.
    Parámetros:
        base (int): La medida de la base del triángulo. Debe ser un número estrictamente positivo (mayor o igual a 1).
        altura (int): La medida de la altura del triángulo. Debe ser un número estrictamente positivo (mayor o igual a 1).      
    Retorno:
        (float): El valor del área del triángulo. Es siempre un número decimal.    
    """   
    return (base * altura) / 2
```

Esta documentación incluye los siguientes elementos:

1. **Descripción de la función**. Acá explicamos cuál es el objetivo de la función para que sea fácil saber si es la función que necesitamos usar. Además, si la función es muy complicada, explicamos qué es lo que hace la función por dentro. Esta descripción puede ocupar múltiples líneas: le recomendamos que no use líneas muy largas y que intente que el texto quede bien alineado a la izquierda.
2. **Parámetros**. Si la función tiene parámetros, especificamos el nombre y el tipo de cada uno, seguidos de una descripción. La idea es que quien vaya a utilizar la función se entere de qué representa el parámetro y de todas las reglas que deberían aplicarse.
3. **Retorno**. Acá explicamos qué es lo que retorna la función.

Para una función tan sencilla como la del ejemplo, puede parece que esta descripción tan grande es exagerada. Pronto estaremos trabajando con funciones mucho más complicadas en las que será muy importante que escribamos una documentación muy completa para que no nos confundamos nosotros mismos o confundamos a las personas con las que estemos trabajando.

```{tip} Documente sus funciones
Documente siempre sus funciones utilizando un formato consistente que incluya una descripción general y la explicación detallada de los parámetros y el retorno.
```

### Ejercicios

1. Use la función `help` para consultar la documentación de algunas de las funciones nativas que ya ha estudiado.


## Descomposición de funciones


## Complejidad de las instrucciones


```{tip} Simplifique las instrucciones
Escriba instrucciones que sean lo más sencillas posibles. Idealmente, cada línea de código debería hacer una sola cosa.
```


## Tipado de funciones

Sobre los *type-hints*

Si usted utiliza otros libros o si consulta en Internet, es muy posible que se encuentre con definiciones de funciones en las que no aparecen los tipos de los parámetros ni el tipo de los resultados. Esto se debe a que en Python el uso de estos elementos es opcional. De hecho, el nombre específico de estos elementos es *type-hints* y las herramientas (IDE, intérprete, compilador, etc.) los utilizan sólo como sugerencias.

En este libro vamos a usar *type-hints* en la definición de todas las funciones y esperamos que usted haga uso de ellos también. Por una parte, esto le facilitará aprender a usar otros lenguajes de programación como C, C++, Java, o TypeScript. Por otro lado, razonar sobre los tipos de datos debería ayudarlo a estructurar mejor sus programas, especialmente mientras adquiere una cierta destreza programando.


```{tip} Utilice *type-hints*
Utilice los *type-hints* para todos los parámetros y los retornos de las funciones. No sólo harán que su código sea más legible y fácil de usar, sino que además lo prepararán a usted para utilizar otros lenguajes.
```


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

Comparado con otros lenguajes, el formato para la documentación de funciones en Python es relativamente pobre y desestructurado. Por el contrario, en Java existe el formato *Javadoc* que es muy estructurado y permite generar automáticamente compendios con la documentación de un programa o una librería. Esquemas similares existen para otros lenguajes como JavaScript (*JSDoc*) y Scala (*Scaladoc*). Aunque no se puedan usar directamente en Python, vale la pena conocer un poco sobre las características de estos formatos (y las limitaciones que tienen) para mejorar la documentación que escribamos de las funciones Python.

La discusión sobre los *type-hints* tiene que ver con una discusión mucho más extensa sobre la conveniencia de tener *tipado dinámico* en los lenguajes de programación. Por un lado, cuando los lenguajes son fuertemente tipados se cometen menos errores o, al menos, las herramientas de edición capturan más errores de forma temprana. Por otro lado, cuando el tipado es dinámico los errores de tipo se capturan en tiempo de ejecución, pero el desarrollo de los programas es más rápido. En este momento hay fuertes discusiones sobre la conveniencia o no de cada sistema, pero hay un hecho que encontramos muy diciente: JavaScript, que tiene tipado dinámico, está incluyendo progresivamente más elementos para escribir programas fuertemente tipados (el crecimiento de TypeScript es evidencia indiscutible), mientras que Python está empezando a incluir elementos para poder incluir verificaciones de tipos.


