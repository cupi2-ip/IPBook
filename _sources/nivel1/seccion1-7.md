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

Las dos funciones anteriores hacen los mismos cálculos, pero la primera es claramente más explícita: no tenemos que hacer un gran esfuerzo para descubrir cuál es su objetivo. 


```{admonition} Use buenos nombres de variables
:class: tip
Para las variables, utilice nombres que indiquen con claridad qué es lo que va a guardar dentro de ellas. Evite nombres muy cortos a menos que no haya ninguna ambigüedad posible.
```


```{admonition} Use buenos nombres de funciones
:class: tip
Para las funciones, utilice nombres que indiquen qué es lo que hará la función. 
Incluya verbos en los nombres de funciones (ej. `guardar_resultado` ), a menos que se pueda sobreentender con facilidad (ej. `calcular_area_triangulo` vs. `area_triangulo`).
```


### Estándares

Más allá de los nombres y de lo que significan, en cada lenguaje también hay estándares para el uso de mayúsculas y minúsculas y la separación de palabras en los nombres de variables y funciones. Estos estándares pueden parecer arbitrarios (¡y lo son!) pero es importante respetarlos porque seguirlos consistentemente hace mucho más sencilla la lectura del código.

En Python, las reglas más importantes en este sentido son las siguientes:

1. Usar *snake_case*. Esto significa que las palabras de un identificador deberían separarse usando el caracter `'_'`. Por ejemplo, en Python se prefiere usar `calcular_area_triangulo` mientras que en Java se usaría `calcularAreaTriangulo`.

2. Usar *minúsculas* para los identificadores. Tanto funciones como variables y parámetros deberían nombrarse usando minúsculas.

3. Usar *Mayúscula Inicial* para los nombres de clases [^clases].  

4. Usar *MAYÚSCULAS SOSTENIDAS* para las constantes. Aunque estrictamente hablando en Python no existe el concepto de constante, se suelen usar mayúsculas sostenidas para indicar que el valor de una variable no debería cambiar su valor. Por ejemplo, `ROJO` o `IVA`. Desafortunadamente una de las constantes más útiles, `math.pi`, no sigue este estándar.

[^clases]: Esto no es realmente relevante para este libro, pero lo mencionamos por completitud.

```{admonition} Use el alfabeto inglés
:class: warning
Aunque en Python es posible utilizar en los identificadores caracteres que existen en el español pero no existen en inglés, como la `ñ` y las vocales acentuadas, es recomendable evitarlo para evitar problemas de codificación. Esto es especialmente importante si se va a usar el mismo código en máquinas Windows, Linux y Mac.
```


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

Ahora bien, a diferencia de otros lenguajes Python no especifica cómo deben describirse los detalles de una función: sólo nos da el espacio para que escribamos la documentación y nos da total libertad para que nosotros decidamos qué aspectos queremos documentar. Es nuestra responsabilidad decidir qué incluir y asegurarnos de que la documentación sea suficiente para que alguien más pueda usar nuestra función. También es nuestra responsabilidad definir cómo vamos a organizar la información para que esté organizada y sea fácil de encontrar y utilizar.

Toda esta libertad que da el lenguaje ha llevado a que existan varios estándares para documentar las funciones sin que ninguno sea claramente superior a los otros. Aunque le recomendamos que más adelante escoja uno de los estándares, por ahora le recomendamos utilizar la versión simplificada que se ilustra en el siguiente ejemplo:

```{code-block} python
---
lineno-start: 1
---
    """ Calcula el área de un triángulo a partir de su base y su altura.
    Parámetros:
        base (int): La medida de la base del triángulo.
                    Debe ser un número estrictamente positivo (mayor o igual a 1).
        altura (int): La medida de la altura del triángulo. 
                    Debe ser un número estrictamente positivo (mayor o igual a 1).      
    Retorno:
        (float): El valor del área del triángulo. Es siempre un número decimal.    
    """   
```

Esta documentación incluye los siguientes elementos:

1. **Descripción de la función**. Acá explicamos cuál es el objetivo de la función para que sea fácil saber si es la función que necesitamos usar. Además, si la función es muy complicada, explicamos qué es lo que hace la función por dentro. Esta descripción puede ocupar múltiples líneas: le recomendamos que no use líneas muy largas y que intente que el texto quede bien alineado a la izquierda.
2. **Parámetros**. Si la función tiene parámetros, especificamos el nombre y el tipo de cada uno, seguidos de una descripción. La idea es que quien vaya a utilizar la función se entere de qué representa el parámetro y de todas las reglas que deberían aplicarse.
3. **Retorno**. Acá explicamos qué es lo que retorna la función.

Para una función tan sencilla como la del ejemplo, puede parece que esta descripción tan grande es exagerada. Pronto estaremos trabajando con funciones mucho más complicadas en las que será muy importante que escribamos una documentación muy completa para que no nos confundamos nosotros mismos o confundamos a las personas con las que estemos trabajando.

```{admonition} Documente sus funciones
:class: tip
Documente siempre sus funciones utilizando un formato consistente que incluya una descripción general y la explicación detallada de los parámetros y el retorno.
```

### Ejercicios

1. Use la función `help` para consultar la documentación de algunas de las funciones nativas que ya ha estudiado.

2. Escriba la documentación de alguna función que haya desarrollado en un ejercicio previo. Revise en el intérprete de Python que pueda leer la documentación de la función usando la función `help`.


## Descomposición de funciones

Aunque no se puede generalizar, en lo posible deberíamos tener funciones sencillas que se compongan poco a poco para formar funciones más complicadas. Esto es preferible a tener funciones extremadamente complicadas que se tengan que leer con muchísima atención: al leer el código de una función debería ser claro cuál es su objetivo principal y cómo lo está logrando.

Para lograr una buena descomposición es necesario primero hacer abstracción de las funciones, separando la signatura de la implementación. Es decir, debemos pensar en qué se quiere lograr con una función independientemente de cómo se vaya a implementar. El proceso se debe repetir identificando funciones cada vez más sencillas que sirvan para explicar cómo se resuelven las funciones más grandes, pero sin entrar en detalles, hasta que lleguemos a funciones triviales. En una sección posterior estudiaremos en mucho más detalle este proceso que se conoce como *refinamiento a pasos*.

```{admonition} Simplifique sus funciones
:class: tip
Intente tener funciones que tengan un único objetivo y que sean fáciles de explicar. Si usted descubre que el objetivo o la implementación de una función son muy complicados de explicar, posiblemente sea una señal de que debe descomponerla en funciones más pequeñas.
```

El siguiente motivo por el cual tiene sentido descomponer las funciones es para evitar la repetición de código. En general, tener código repetido es mala idea porque  aumenta la posibilidad de tener errores y porque, en caso de querer corregir un error, será necesario hacerlo en muchos lugares. 

```{admonition} Use funciones para evitar repeticiones
:class: tip
Si está repitiendo el mismo código en varios lugares, considere construir una función que encapsule esa funcionalidad y que pueda llamar en todos los lugares donde lo requiera.
```


## Complejidad de las instrucciones

Una razón por la cual muchas veces el código es mucho más difícil de leer y entender de lo necesario es porque se hacen muchas acciones dentro de la misma instrucción. A manera de ejemplo a continuación presentamos dos funciones equivalentes que calculan el área de un polígono regular a partir de la longitud de un lado y de la cantidad de lados:

```{code-block} python
---
lineno-start: 1
---
import math

def area_poligono(lado: float, num_lados: int) -> float:
    return (num_lados * lado**2) / (4 * math.tan(math.pi / num_lados))
```

```{code-block} python
---
lineno-start: 1
---
import math

def area_poligono2(lado: float, num_lados: int) -> float:
    angulo_interno_radianes = math.pi / num_lados
    numerador = num_lados * lado**2
    denominador = 4 * math.tan(angulo_interno_radianes)
    return numerador / denominador
```

Aunque el primer ejemplo no es extremadamente complicado, la única instrucción que tiene es mucho más complicada que cualquiera de las instrucciones del segundo ejemplo. Esto significa que el segundo ejemplo será más fácil de leer y probablemente fue más fácil de construir que el primero.


```{admonition} Simplifique las instrucciones
:class: tip
Escriba instrucciones que sean lo más sencillas posibles. 

Idealmente, cada línea de código debería hacer una sola cosa.
```

```{tip} No sólo es por quien lee, sino también es por usted
: admonition: tip
La primera persona que tiene que leer un bloque de código es la persona que lo tiene que escribir. Si las instrucciones son fáciles de leer, serán fáciles de escribir; si las instrucciones terminan siendo difíciles de leer, es porque fueron difíciles de escribir.

Hágase un favor y planee su código para que sea fácil de leer.
```


## Tipado de funciones y parámetros

Si usted utiliza otros libros o si consulta en Internet, es muy posible que se encuentre con definiciones de funciones en las que no aparecen los tipos de los parámetros ni el tipo de los resultados. Esto se debe a que en Python el uso de estos elementos es opcional. De hecho, el nombre específico de estos elementos es *type-hints* y las herramientas (IDE, intérprete, compilador, etc.) los utilizan sólo como sugerencias.

En este libro vamos a usar *type-hints* en la definición de todas las funciones y esperamos que usted haga uso de ellos también. Por una parte, esto le facilitará aprender a usar otros lenguajes de programación como C, C++, Java, o TypeScript. Por otro lado, razonar sobre los tipos de datos debería ayudarlo a estructurar mejor sus programas, especialmente mientras adquiere una cierta destreza programando.


```{admonition} Utilice *type-hints*
:class: tip
Utilice los *type-hints* para todos los parámetros y los retornos de las funciones. No sólo harán que su código sea más legible y fácil de usar, sino que además lo prepararán a usted para utilizar otros lenguajes.
```

## Comentarios

Por último, hay un aspecto adicional que es muy sencillo pero tiende a mejorar la calidad del código: introducir comentarios dentro de las instrucciones. En los ejemplos que introducimos al principio de la sección eso no se estaba haciendo porque las funciones utilizadas eran muy sencillas, pero en funciones como las que estudiaremos a partir de la próxima sección esto será mucho más importante.

En general deberían incluirse comentarios dentro del código para explicar el funcionamiento de bloques de código que sean particularmente complicados. No existe ningún estándar sobre esos comentarios, pero a continuación le damos algunas recomendaciones:

1. No exagere con los comentarios. Así como la falta de comentarios es grave, el exceso de comentarios puede terminar en código muy difícil de leer.

2. Escriba comentarios que expliquen lo que hacen fragmentos significativos de código y/o su justificación, en lugar de hacer una traducción de Python a español de las instrucciones realizadas.

3. Identifique las instrucciones particularmente complicadas y documéntelas.

4. En funciones medianas o largas que no pueda o no quiera descomponer, enumere las grandes etapas usando comentarios.

```{annotation} Use comentarios dentro de su código
:class: tip
Incluya comentarios dentro del código que expliquen fragmentos particularmente complejos y sirvan para aclarar la estructura de la implementación de una función.
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

Comparado con otros lenguajes, el formato para la documentación de funciones en Python es relativamente pobre y desestructurado. En Java existe el formato *Javadoc* que es muy estructurado y permite generar automáticamente compendios con la documentación de un programa o una librería. Esquemas similares existen para otros lenguajes como JavaScript (*JSDoc*) y Scala (*Scaladoc*). Aunque no se puedan usar directamente en Python, vale la pena conocer un poco sobre las características de estos formatos (y las limitaciones que tienen) para mejorar la documentación que escribamos de las funciones Python.

La discusión sobre los *type-hints* tiene que ver con una discusión mucho más extensa sobre la conveniencia de tener *tipado dinámico* en los lenguajes de programación. Por un lado, cuando los lenguajes son fuertemente tipados se cometen menos errores o, al menos, las herramientas de edición capturan más errores de forma temprana. Por otro lado, cuando el tipado es dinámico los errores de tipo se capturan en tiempo de ejecución, pero el desarrollo de los programas es más rápido. En este momento hay fuertes discusiones sobre la conveniencia o no de cada sistema, pero hay un hecho que encontramos muy diciente: JavaScript, que tiene tipado dinámico, está incluyendo progresivamente más elementos para escribir programas fuertemente tipados (el crecimiento de TypeScript es evidencia indiscutible), mientras que Python está empezando a incluir elementos para poder incluir verificaciones de tipos.


