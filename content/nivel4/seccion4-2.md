Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Tuplas

> El objetivo de esta sección es presentar el tipo de dato *tupla* y explicar cuáles son las ventajas que trae su uso en casos muy particulares.

Al inicio de este libro presentamos los tipos **str**, **int**, **float** y **bool**. Todos estos son tipos en los cuales hay un único valor que nos interese. Luego estudiamos los tipos **dict** y **list**, que sirven para representar valores múltiples con muchísima libertad: una lista puede tener cualquier cantidad de elementos, así como un diccionario puede tener cualquier cantidad de llaves. Todos estos tipos son de utilidad en muchísimos casos, pero tienen una limitación: no nos sirven en casos en los que se quiera tener un conjunto limitado de valores.

Par ilustrar el problema, tomemos el caso de una coordenada cartesiana *(x,y)*. Si queremos representar esta coordenada, podríamos utilizar dos variables de tipo **float**, o podríamos utilizar una lista con dos números flotantes. En el primer caso, el problema es que estaríamos usando dos valores para representar una sola coordenada. Así, consturir una función que retornara una coordenada sería un problema porque una función sólo puede retornar un valor. En el segundo caso, tendríamos una sola lista con los dos valores así que el problema del retorno no se presentaría. El problema acá sería que no habría ninguna garantía de que la lista retornada tenga exactamente 2 posiciones: podría tener 1, 2, 3, más de 3 o incluso podría ser una lista vacía. Aunque nosotros podríamos verificar el tamaño, sería mucho más conveniente tener un tipo de dato que nos permita agrupar múltiples valores y al mismo tiempo nos dé un poco más de garantía con respecto a la cantidad y a su orden.

En Python, esto lo vamos a lograr con el tipo de dato **tuple**, llamado *tupla* en español, el cual sirve para representar una secuencia inmutable de valores. A continuación estudiaremos este tipo de datos e ilustraremos su uso con varios ejemplos.


## El tipo tuple en Python

Para ilustrar el uso del tipo **tuple**, usaremos el ejemplo de las coordenadas cartesianas que introducimos más arriba.

En primer lugar, veamos que la construcción de una nueva tupla requiere que se especifique desde el inicio cuáles van a ser sus valores:

```python
>>> coordenada = (3, 4.5)
>>> print(type(coordenada))
<class 'tuple'>
```
Como se ve en este ejemplo, una tupla se crea usando paréntesis redondos, a diferencia de los cuadrados que se usan para las listas, y las llaves que se usan para los diccionarios. Los valores que irán dentro de la tupla se separan siempre usando comas y, al igual que en las listas, se organizan dentro de la tupla en el orden en que se especifican iniciando con la posición 0.

Si queremos consultar los valores dentro de una tupla tenemos que usar la posición al igual que como se hace en una lista:

```python
>>> print(coordenada[0], "-", coordenada[1])
3 - 4.5
```

Las tuplas también se pueden recorrer exactamente igual a como se recorrería una lista:

```python
>>> for valor in coordenada:
...   print(valor)
3
4.5
>>> for pos in range(len(coordenada)):
...   print(pos, "-", coordenada[pos])
...
0 - 3
1 - 4.5
```

La gran diferencia entre las tuplas y las listas es que las tuplas son **inmutables**. Esto quiere decir que después de que una tupla se haya creado, es imposible modificar los valores que contiene. Esto quiere decir que no existen métodos equivalentes a ```append``` e ```insert```, y que no es posible hacer una asignación a una tupla ya creada.

```python
>>> coordenada[0] = -1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

## Empaquetado y desempaquetado

Una característica muy útil de las tuplas en Python es que permiten hacer lo que denomina *empaquetado* y *desempaquetado* de valores. *Empaquetado* hace referencia a lo que ya vimos: tomar varios valores y agruparlos en una única tupla. El *desempaquetado* es el proceso inverso de tomar los valores contenidos en una tupla y dejarlos en variables separadas. Lo que hace esto  interesante es que, en lugar de requerir varias instrucciones con asignaciones, se puede hacer en una sola instrucción. 

El siguiente fragmento muestra cómo se podrían desempaquetar los valores de una coordenada sin tener que acceder a cada una de las posiciones en la tupla:

```python
x, y = coordenada
```

Si no se usara la capacidad de desempaquetar, el código habría tenido que ser el siguiente.

```python
x = coordenada[0]
y = coordenada[1]
```



## Uso de tuplas

Las tuplas en Python pueden utilizarse en muchas situaciones diferente en las que también podrían utilizarse listas. Sin embargo, es recomendable que se usen cuando se requieran las siguientes características:

* Agrupar varios valores, asegurando la cantidad de valores
* Inmutabilidad

Como ya vimos antes, un uso muy común para las tuplas es servir para agrupar y organizar valores retornados por una función. En este caso, el uso de tuplas nos ayuda a garantizar que los valores retornados por la función estén siempre en el orden que se espera y que no sean modificados más adelante.

Otro uso muy común es agrupar valores que siempre deberían estar juntos. Por ejemplo, si se está trabajando con coordenadas cartesianas las tuplas servirán para agrupar los valores para cada uno de los ejes.


Veamos a continuación otros ejemplos de uso de tuplas.

### Creación de rectángulos

En este caso tenemos una función que recibe las coordenadas *(x,y)* de dos puntos y encuentra el rectángulo delimitado por esos puntos. Para esto, la función busca la esquina del rectángulo con menor coordenadas *x* y *y*, y calcula el ancho y alto del rectángulo.

```python
def crear_rectangulo(punto1: tuple, punto2: tuple) -> tuple:
  x1, y1 = punto1
  x2, y2 = punto2
  ancho = abs(x1 - x2)
  alto = abs(y1 - y2)
  x = min(x1, x2)
  y = min(y1, y2)
  return (x, y, ancho, alto)
```

A continuación vemos cómo se puede utilizar el mecanismo de desempaquetado para llamar a la función y almacenar el resultado en cuatro variables.

```python
x, y, ancho, alto = crear_rectangulo(50, 180, 120, 30)
```

### Estadísticas de una lista

En este caso tenemos una función que calcula 3 estadísticas sobre una lista: el menor valor, el mayor valor y el valor promedio. Esta función recibe la lista de valores y retorna una tupla con los tres números calculados. Lo interesante de este ejemplo es que normalmente se habrían necesitado 3 funciones, cada una con su propio recorrido sobre la lista, para calular los tres valores. En este caso estamos aprovechando para calcular todo lo que necesitamos con un único recorrido.

```python
def estadisticas(valores: list) -> tuple:
  mayor = valores[0]
  menor = valores[0]
  total = 0
  for valor in valores:
    total += valor
    if valor > mayor:
      mayor = valor
    elif valor < menor:
      menor = valor
  promedio = total / len(valores)
  return (menor, mayor, promedio)
```

A continuación vemos cómo se puede utilizar el mecanismo de desempaquetado para llamar a la función y almacenar el resultado en tres variables.

```python
menor, mayor, promedio = estadisticas(valores)
```



## Ejercicios ##

1. Construya una función que reciba dos vectores y retorne un nuevo vector que sea la suma de los dos vectores recibidos. Cada vector debe recibirse como una tupla con dos valores flotantes.

2. Construya una función que reciba una cadena de caracteres y retorne una lista de parejas (tuplas) donde la primera posición corresponda a una palabra que aparezca en la cadena y la segunda posición corresponda a la cantidad de veces que aparece la palabra en la cadena. La lista retornada tiene que tener tatas parejas como palabras *diferentes* haya en la cadena original.

3. En este ejercicio vamos a construir un rudimentario algoritmo de compresión que nos va a servir para reducir cadenas de ceros y unos. Lo que va a hacer el algoritmo es encontrar las posiciones en las que haya secuencias de uno o más unos y retornar una lista con la posición y tamaño de cada secuencia. Usted tiene que construir entonces una función llamada ```comprimir``` que reciba una cadena de caracteres (que podemos asumir que va a tener sólo los caracteres `'0'` o `'1'`) y que retorne una tupla con dos elementos: el primer elemento, será la longitud original de la cadena; el segundo elemento será una lista de tuplas, donde cada tupla tiene primero el valor de una posición en la que había un `'1'` en la cadena original y luego tiene la cantidad de unos seguidos que había a partir de esa posición. Por ejemplo, si la cadena de entrada fuera `'101101111000110'`, el resultado debería ser `(15, [(0, 1), (2, 2), (5, 4), (12, 2)])` porque la cadena original tenía 15 caracteres y porque había 4 secuencias de unos.

4. En este ejercicio usted debe construir la función llamada `descomprimir`, que debe ser capaz de tomar el resultado de la función `comprimir` y producir la cadena original. Es decir, si la función `descomprimir` recibe la tupla `(15, [(0, 1), (2, 2), (5, 4), (12, 2)])`, el resultado debería ser la cadena `'101101111000110'`.

5. Una universidad tiene información sobre la cantidad de estudiantes inscritos en cada curso y sobre los salones (edificio y código de salón) donde se deben dictar las clases. Dada esta información, el departamento de seguridad de la Universidad está interesado en saber cuántos estudiantes debería haber dentro de cada edificio en caso de que se tenga que realizar una evacuación. Usted debe crear una función llamada `contar_estudiantes` que reciba la información de los cursos y un horario y retorne la cantidad de estudiantes por edificio. Las entradas de la función serán las siguientes: 1) un diccionario donde las llaves serán los nombres de los cursos y los valores serán también diccionarios con tres llaves: `'inscritos'` para indicar el número de estudiantes inscritos en el curso, `'horario'` para indicar el horario en el que se dicta el curso, y `'ubicacion'` para indicar el salón donde se dicta el curso. El horario de un curso se representa con una tupla que tiene en la primera posición el día de la semana ('lunes', 'martes', etc. ) y en la segunda posición tiene una cadena con la franja horaria ('10:00 - 11:30', '11:30 - 13:00', etc.). La ubicación de un curso se representa también con una tupla que tiene en la primera posición el nombre de un edificio y en la segunda posición el código del salón (ambos son cadenas de caracteres). 2) El segundo parámetro de la función será el horario en el que se quieren contar los estudiantes (también se expresa con una tupla de número de día y franja horaria). Se puede asumir que las franjas horarias en las que se va a hacer la consulta son las mismas franjas horarias de los cursos. La función debe retornar una lista de tuplas donde cada tupla tendrá en la primera posición el nombre de un edificio y en la segunda posición la cantidad de estudiantes que deberían estar dentro del edificio en el horario consultado.



## Más allá de Python

No es usual que los lenguajes de programación ofrezcan un tipo básico para manejar tuplas, así que aprender a utilizar este nuevo tipo no necesariamente será de utilidad en otros lenguajes. Sin embargo, muchas librerías de Python utilizan tuplas de forma frecuente, así que es conveniente adquirir destreza en  su uso.

#### Notas 

