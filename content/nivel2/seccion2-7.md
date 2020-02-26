Versión borrador / preliminar |
:-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Diccionarios

> El objetivo de esta sección es introducir el concepto de diccionario, que en Python se implementa con el tipo de dato `dict`, y mostrar cómo puede ser de utilidad para construir programas mucho más complejos.

En las secciones anteriores hemos trabajado exclusivamente con los tipos de datos básicos de Python (`int`, `bool`, `str`, `float`). Aunque estos tipos son suficientes para muchas cosas, tienen también un problema grave: si los problemas son medianamente complejos se necesitan muchas variables y parámetros. Esto nos obliga a tener mucho cuidado para no olvidar ni confundir variables. También hace necesario ser creativo y organizado con los nombres que utilicemos.

Por ejemplo, si quisiéramos hacer una función que compare tres celulares con base en la velocidad del procesador, la cantidad de memoria, la calidad de la cámara, la tecnología de la pantalla, el tamaño de la pantalla, la capacidad de la pila, el sistema operativo y su versión, necesitaríamos 27 parámetros![^pantalla] Además de que sería *incómodo* declarar e implementar esta función, también sería incómodo[^incomodo] invocarla: sería muy fácil olvidar un parámetro y más aún intercambiar el orden de dos parámetros, llevando a erorres difíciles de diagnosticar.

En esta sección vamos a introducir un nuevo concepto que nos permitirá simplificar un poco el problema anterior: en lugar de requerir 27 parámetros usaremos sólo 3. Este concepto, que en Python se llama **diccionario** y que en otros lenguajes se conoce como **mapa**, es parte básica del lenguaje y, como no requiere de librerías adicionales, se usa de manera extremadamente frecuente.


[^pantalla]: Para el tamaño de la pantalla necesitamos el ancho y el alto.

[^incomodo]: Nos referimos a *incómodo* para indicar que, aunque no sería difícil, requeriría un nivel de atención mucho mayor del necesario. Es lo mismo que pasa cuando se usan nombres de variables y parámetros que no corresponden con su significado: no es que sean imposibles de utilizar, pero hacen necesario concentrar la atención en los nombres en lugar de concentrarla en los problemas reales que se están intentando resolver.


## El concepto de diccionario

Un **diccionario** es una **estructura de datos** que contiene muchos **valores**, identificados cada uno con una **llave** que es única. 

El término **estructura de datos** hace referencia a una forma de organizar datos para poder almacenarlos, modificarlos y consultarlos. Técnicamente, las variables que hemos venido utilizando son estructuras de datos pero, como sólo tienen un valor, raramente se les aplica el término a estas.

Un diccionario es entonces una estructura de datos (una forma de organizar datos), donde a cada valor que queramos almacenar se le asigna una llave (una llave es también un valor, pero además es único dentro del diccionario). Un buen ejemplo de esto es el diccionario de un lenguaje como el Español: a cada palabra (una llave) le corresponde una definición (un valor). Otro ejemplo es una red social como Twitter: a cada nombre de usuario (una llave) le corresponde un usuario (un valor) con toda su información.

Hay básicamente dos usos que nosotros le damos a un diccionario en la vida diaria. El primero es para buscar la definición de una palabra: si nosotros conocemos la palabra (la llave), podemos obtener la definición asociada a esta (el valor). El segundo uso de un diccionario es descubrir si una palabra existe o no: si no encontramos una palabra entre las llaves del diccionario, significa que la palabra no existe y que no tiene una definición. Note que un diccionario está construido pensando en que el criterio de búsqueda es la palabra y no la definición. Sería muy extraño que alguien intentara buscar la palabra en Español que corresponde a la definición *"Clase o condición a la cual está sujeta la vida de cada uno"*. 

En las siguientes secciones mostraremos cómo usar este concepto en Python y mostraremos también cómo podemos construir y modificar nuestros propios diccionarios.


## El tipo `dict` en Python

En Python los diccionarios son un elemento básico del lenguaje que, así como las cadenas, está perfectamente integrado dentro de la sintaxis del lenguaje. Para crear un diccionario basta con indicar que se quiere crear un diccionario (usando los caracteres `{}`) y separar las parejas `llave:valor` usando comas. Tomemos como ejemplo el siguiente fragmento, en el cual se han incluido cambios de línea para facilitar la lectura:

```python
palabras = { 'imagen' : 'Figura, representación, semejanza y apariencia de algo',
             'figura' : 'Forma exterior de alguien o de algo', 
             'baraja' : 'Conjunto completo de cartas empleado para juegos de azar',
             'posibilidad' : 'Aptitud, potencia u ocasión para ser o existir algo' }
```

![Representación gráfica del diccionario palabras](./images/diccionarios_figura1.png)

Este fragmento crea una nueva variable con el nombre `palabras`. A diferencia de variables más sencillas que sólo tienen un valor, esta nueva variable es un diccionario y contiene 4 parejas llave-valor. También habríamos podido crear un diccionario vacío con la expresión `palabras = {}`. Observe lo que pasa si aplicamos las funciones `type()` y `len()` a nuestra nueva variable:

```
>>> type(palabras)
<class 'dict'>
>>> len(palabras)
4
```

Con `type()`, vemos que Python utiliza el término `dict` para referirse al tipo de datos de los diccionarios. Con `len()`, vemos que Python cuenta la cantidad de parejas que hay en el diccionario.

Veamos ahora cómo hacemos para consultar el contenido del diccionario:

```python
>>> definicion_imagen = palabras['imagen']
>>> print(definicion_imagen)
Figura, representación, semejanza y apariencia de algo
```

En este fragmento estamos consultando el valor asociado a la cadena `'imagen'` dentro del diccionario `palabras`. Para esto usamos el nombre de la variable seguido del nombre de la llave entre paréntesis cuadrados. Note que el nombre de la llave tiene que ser idéntico al que usamos cuando creamos el diccionario. No funcionaría si usáramos `'Imagen'` o `'IMAGEN'`). Si intentamos extraer un valor usando una llave que no existe, el resultado es un error:

```python
>>> definicion = palabras['IMAGEN']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'IMAGEN'
```

Para evitar este problema es posible utilizar el operador `in` que permite consultar si una llave hace parte de un diccionario o no.

```python
llave = 'IMAGEN'
# Preguntar si la llave está en el diccionario antes de consultar
if llave in palabras:
  definicion = palabras[llave]
else:
  definicion = "La palabra '" + llave + "' no se encuentra en el diccionario"
```

A diferencia del ejemplo pasado, en este no se va a producir un error porque sólo consultamos el valor de la llave si estamos seguros de que se encuentra dentro del diccionario.


### Nombres y valores de variables vs. nombres de llave

En la sección mostramos el uso básico de los diccionarios y la forma en la que se extrae un valor. En esta sección vamos a explorar uno de los errores más comunes que ocurren al utilizar diccionarios: confundir el nombre de una variable, con el valor de una variable y con el nombre de una llave.

En primer lugar, estudie con atención el siguiente fragmento de código y escriba los valores que debería imprimir. Si se produce algún error en alguna parte, explíquelo.

```python
diccionario = {"llave":"valor", "palabra":"definición"}
llave = "llave"
print(1, diccionario["llave"])
print(2, diccionario[llave])
llave = "palabra"
print(3, diccionario[llave])
print(4, diccionario["palabra"])
print(5, diccionario[palabra])
```

Gráficamente, el diccionario que se construye con el código anterior se ve como en la siguiente figura.

![Representación gráfica del diccionario del ejemplo](./images/diccionarios_figura2.png)

A continuación explicamos qué imprime cada llamado a la función `print` pero lo invitamos a intentar resolverlo usted antes de mirar la solución.

#### 1. diccionario\["llave"\]

En el primer caso, se imprime en la consola lo siguiente: `1 valor`.

Esto no debería ser una sorpresa porque se está utilizando explícitamente el nombre de la llave que está almacenada en el diccionario.

#### 2. diccionario\[llave\]

En el segundo caso, se imprime en la consola lo siguiente: `2 valor`.

En este caso, se está usando la variable `llave` para indicar cuál es la llave que nos interesa en el diccionario. El punto importante acá es que **no nos interesa el nombre de la variable**. Lo que es importante es el valor que tiene la variable. En este caso, el valor de la variable es la cadena `'llave'` y por eso el valor que se imprime es la cadena `'valor'`.

#### 3. diccionario\[llave\] (segunda parte)

En el tercer caso, se imprime en la consola lo siguiente: `3 definición`.

Este caso refuerza lo que dijimos en el punto anterior: aunque la variable se llama `llave`,  el nombre no es importante sino el valor almacenado en ella. En este caso, la variable almacena la cadena `'palabra'`, así que lo que sacamos del diccionario es el valor asociado a la llave `'palabra'`.

#### 4. diccionario\["palabra"\]

En el cuarto caso, se imprime en la consola lo siguiente: `4 definición`.

Esta es la versión equivalente del primer caso: usamos una cadena que es idéntica a una cadena que se encuentra dentro del diccionario.

#### 5. diccionario\[palabra\]

En el quinto caso, no se imprime nada en la consola porque se produce un error.

Fíjese que hasta el momento no hemos definido ninguna variable con el nombre `palabra`, así que cuando se intenta consultar el valor de esta variable, se produce un error.



### Tipos de llaves y valores

En Python, las llaves y valores en un diccionario pueden ser prácticamente de cualquier tipo. Podemos tener diccionarios cuyas llaves y valores son cadenas, como en el caso de nuestro ejemplo de las palabras en Español. Podemos tener también diccionarios cuyas llaves son cadenas y sus valores son números, como en el caso de las notas que obtuvieron los estudiantes de algún curso (los nombres son las llaves y las notas son los valores). Aunque es menos usual, las llaves de un diccionario también pueden ser números, como en el caso de un diccionario que represente un edificio (las llaves son los números de los apartamentos y los valores son los nombres de quienes viven en esos apartamentos). Finalmente, los tipos de los valores pueden combinarse: más adelante exploraremos ejemplos donde las llaves son cadenas y los valores son de varios tipos diferentes.

**¡Cuidado!** 
Aunque no está prohibido en el lenguaje, es recomendable evitar tener llaves de diferentes tipos en el mismo diccionario (algunas numéricas, otras cadenas, otras booleanas, etc.).

## El método get

Como ya vimos, cuando se intenta consultar un diccionario usando una llave que no existe se produce un error. Una forma de evitar esto es consultar primero si la llave existe usando el operador `in`. Otra alternativa, muy usada porque reduce el tamaño del código, es usar el *método*[^metodos] `get`. Este método, que se aplica sobre un diccionario, recibe como parámetros una llave y el valor que se debería retornar si la llave no existe en el diccionario.

```python
llave = 'IMAGEN'
definicion = palabras.get(llave, "La palabra '" + llave + "' no se encuentra en el diccionario")
```

El fragmento anterior es equivalente al que usamos en la sección pasada: si la palabra existe en el diccionario, en la variable `definicion` queda el valor contenido en el diccionario; de lo contrario, en la variable `definicion` queda un mensaje anunciando que la palabra no existía.

[^metodos]: Recordemos que los métodos se invocan usando el operador `.` entre el destinatario del método y el nombre del método.

### El valor None

El valor `None`, que se puede traducir como `ninguno`, es un valor que se usa en Python para denotar la "ausencia de un valor". El tipo de `None` es `NoneType` y es ese nombre el que se menciona cuando se hace una operación con este valor:

```python
>>> None + 1
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

Nosotros ya hemos utilizado `None` para describir el tipo de retorno de una función que no se espera que retorne nada. Ahora vamos a utilizar `None` como un valor y no como un tipo. Este valor es de mucha utilidad cuando el resultado de una operación puede no existir. Considere por ejemplo el caso de las soluciones reales de una ecuación cuadrática: la ecuación puede tener dos soluciones diferentes, dos soluciones iguales, o ninguna solución [^tuple]. Lo normal sería que, en este último caso, se usara `None` como valor para las soluciones. 

[^tuple]: El tipo de dato `tuple` sirve para representar secuencias de números, como por ejemplo coordenadas. Lo estudiaremos en más detalle en el nivel 4.

```python
import math
def solucionar_cuadratica(a: int, b: int, c:int) -> tuple:
    """ Encuentra las soluciones reales de una ecuación cuadrática de la forma
        y = ax^2 + bx + c
    Parámetros:
      a (int): El coeficiente del término de orden 2
      b (int): El coeficiente del término de orden 1
      c (int): El coeficiente del término de orden 0
    Retorna:
      (tuple): Una tupla con las soluciones reales de la ecuación.
               Retorna None si la ecuación no tiene solución real.
    """
    soluciones = None
    determinante = (b**2) - (4*a*c)
    if determinante >= 0:
        sol1 = -b + (math.sqrt(determinante))
        sol2 = -b - (math.sqrt(determinante))
        soluciones = (sol1, sol2)
    return soluciones

def imprimir_soluciones(soluciones: tuple) -> None:
    """ Imprime las soluciones de una ecuación cuadrática o imprime
        un mensaje indicando que no había soluciones.
    Parámetros:
      soluciones (tuple): Una tupla con dos elementos que son las soluciones de la ecuación.
                          Si no hay soluciones reales, 'soluciones' debe tener el valor None.
    """
    if soluciones is None:
        print("La ecuación no tenía soluciones reales")
    else:
        print("Las soluciones son", soluciones[0], "y", soluciones[1])

# Calcular e imprimir las soluciones de una ecuación sin soluciones reales
soluciones = solucionar_cuadratica(1,1,1)
imprimir_soluciones(soluciones)

# Calcular e imprimir las soluciones de una ecuación con dos soluciones reales diferentes
soluciones = solucionar_cuadratica(1,0,-1)
imprimir_soluciones(soluciones)
```

En este fragmento tenemos una función llamada `solucionar_cuadratica` que recibe los coeficientes de una ecuación cuadrática y calcula una *tupla* con una pareja de soluciones. Por ahora no se preocupe por la tupla sino por el hecho de que, si la ecuación no tiene soluciones, la función retorna el valor `None`.

La segunda función, `imprimir_soluciones` espera una tupla con dos soluciones en una tupla o el valor `None`. Para saber qué mensaje imprimir, la función usa la condición `soluciones is None`. En general `x is None` es la expresión preferida en Python para saber si alguna variable tiene el valor `None`.

Veamos ahora el resultado de correr el programa anterior:

```
La ecuación no tenía soluciones reales
Las soluciones son 2.0 y -2.0
```

### El método get y el valor None

La explicación anterior sobre el valor `None` es relevante porque se usa muy frecuentemente con el método `get`: si una llave no se encuentra en un diccionario, usar `None` como valor por defecto es lo más natural en muchos casos y es mucho mejor que usar cosas como cadenas vacías o sólo con espacios. Observemos el uso de `get` y `None` en un ejemplo:

```python
def imprimir_definicion(diccionario: dict, palabra: str) -> None:
    """ Imprime la definición de una palabra o, si la palabra no existe,
        un mensaje indicando el problema.
    Parámetros:
      diccionario (dict): Un diccionario con las palabras y sus definiciones
      palabra (str): La palabra para la que se quiere la definición
    """
    definicion = palabras.get(palabra, None)
    if definicion is not None:
         print("La definición de", palabra, "es:", definicion)
    else:
         print("La palabra '" + llave + "' no se encuentra en el diccionario")
```

## Modificación de diccionarios

Ya vimos cómo implementar en Python los dos usos que usualmente le damos al diccionario de un idioma como el Español. Veamos ahora cómo harían los miembros de la RAE para modificar el diccionario agregando nuevos términos y definiciones y eliminando términos en desuso.

Para explicar cómo se modifica un diccionario, y mostrar de paso que un diccionario se utiliza igual que cualquier otra variable, vamos a crear una nueva función que agrega definiciones al diccionario. Empezaremos con una versión sencilla y la iremos volviendo progresivamente más compleja.

### Agregar una definición: primera versión

```python
def agregar_definicion(diccionario: dict, palabra: str, definicion: str)-> None:
  diccionario[palabra] = definicion
```
Esta primera versión de la función muestra cómo se modifica un diccionario: usando la misma convención que para consultar (paréntesis cuadrados alrededor del nombre de la llave), le *asignamos* una definición a la palabra. Veamos ahora cómo invocar la nueva función:

```python
palabras = {}
agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
agregar_definicion(palabras, 'figura', 'Forma exterior de alguien o de algo')
```
Después de ejecutar estas 3 instrucciones, vamos a tener un nuevo diccionario llamado `palabras` que va a tener las definiciones de `imagen` y `figura`. 

![Representación gráfica del diccionario palabras](./images/diccionarios_figura3.png)

La pregunta que debería surgir en este punto es: ¿Por qué se modifica el diccionario palabras si la función no retorna nada? La respuesta a esta pregunta la revisaremos en una sección posterior en la que entraremos en detalle sobre la **mutabilidad** de los diccionarios.

### Agregar una definición: segunda versión

Para la segunda versión de la función, vamos a cambiar la signatura para que nuestra función retorne un valor de verdad indicando si se pudo agregar la definición o no. Si la palabra ya existía en el diccionario, no debería agregarse y la función debería retornar el valor `False`. De lo contrario, debería agregarse y el resultado debería ser `True`.

```python
def agregar_definicion(diccionario: dict, palabra: str, definicion: str)-> bool:
  definicion_agregada = False
  if palabra not in diccionario:
      diccionario[palabra] = definicion
      definicion_agregada = True
  return definicion_agregada
```
Observe 3 cosas interesantes en esta función:

1. La variable `definicion_agregada` se inicializa en `False`.
2. El valor de la variable `definicion_agregada` sólo se cambia por `True` si la palabra se pudo agregar.
3. Usamos el operador `not in` para consultar si la llave **no estaba** en el diccionario.

```python
palabras = {}
res1 = agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
res2 = agregar_definicion(palabras, 'figura', 'Forma exterior de alguien o de algo')
res3 = agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
print(res1, res2, res3)
```

En este fragmento usamos la nueva función y guardamos el resultado de cada invocación en una variable. Cuando imprimimos las tres variables el resultado que vemos en la consola es `True True False`. Esto nos indica que las dos primeras invocaciones fueron exitosas y que la tercera falló.

### Agregar una definición: tercera versión

En la tercera y última versión vamos a ofrecer la posibilidad de tener varias definiciones para una palabra. Para lograr esto vamos a concatenar las definiciones a medida que las vayamos agregando, pero sólo si no habíamos almacenado antes esa misma definición. Para verificar este último punto usaremos la operación `not in` aplicada sobre un `str` (la definición que ya teníamos almacenada).

```python
def agregar_definicion(diccionario: dict, palabra: str, definicion: str)-> bool:
  definicion_agregada = False
  # La palabra es nueva en el diccionario
  if palabra not in diccionario:
      diccionario[palabra] = definicion
      definicion_agregada = True
  # La palabra no es nueva pero la definición sí es nueva
  elif definicion not in diccionario[palabra]:
      diccionario[palabra] += '\n' + definicion
      definicion_agregada = True
  return definicion_agregada
```

En esta nueva función tenemos una primera posibilidad y es que la palabra no estuviera en el diccionario. En este caso, la palabra se agrega igual que en el caso anterior.

La segunda posibilidad es que la palabra ya estuviera en el diccionario. En este caso, lo que hacemos es revisar si la definición que queremos agregar es parte de la definición que tenemos en el diccionario. Esto lo hacemos aplicando el operador `not in` sobre la definición que sacamos del diccionario: este operador retornará `True` sólo si la nueva definición no está contenida en la definición que estaba guardada en el diccionario. Note que:

* En la condición del bloque `elif` no es necesario incluir la expresión `palabra in diccionario` porque solamente vamos a evaluar el bloque cuando la condición del `if` sea falsa. 
* Como sabemos que la palabra sí está en el diccionario, podemos consultarla en la condición del `elif` sin temor a que se genere un error.

Finalmente, en el cuerpo del bloque `elif` se modifica la definición almacenada en el diccionario. Fíjese que estamos usando el operador `+=` para modificar el valor del diccionario de la misma forma en que lo usaríamos para modificar el valor de una variable.


```python
palabras = {}
res1 = agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
res2 = agregar_definicion(palabras, 'imagen', 'Estatua, efigie o pintura de una divinidad o de un personaje sagrado.')
res3 = agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
print(res1, res2, res3)
```

Si ejecutamos este último fragmento usando la nueva definición de la función encontraremos que el resultado que se imprime en la consola es `True True False`. Esto significa que las dos primeras definiciones se pudieron agregar, mientras que la tercera fue rechazada porque estaba repetida.


### Eliminar una definición

La última operación para estudiar es la que nos permite eliminar definiciones de un diccionario. Esto se puede lograr de dos formas: con el operador `del` o con el método `pop`. Tenga en cuenta que en ambos casos es necesario verificar que la llave exista en el diccionario antes de intentar eliminarla. De lo contrario se producirá un error.

#### Uso del operador `del` para eliminar un valor

En la siguiente función se usa el operador `del` para eliminar una palabra del diccionario. Tenga en cuenta que esto eliminará tanto la palabra como su definición. Para evitar que se produzca un error, el llamado a `del` ocurre dentro del cuerpo de un condicional que se asegura que la palabra sí exista en el diccionario.

```python
def eliminar_palabra(diccionario: dict, palabra: str)-> bool:
    palabra_eliminada = False
    if palabra in diccionario:
        del diccionario[palabra]
        palabra_eliminada = True
    return palabra_eliminada
```

En el siguiente fragmento se pone en uso la función para eliminar una palabra que no se encuentre en nuestro diccionario y una que sí lo esté [^toballa].

```python
palabras = {}
agregar_definicion(palabras, 'imagen', 'Figura, representación, semejanza y apariencia de algo')
agregar_definicion(palabras, 'toballa', 'Toalla')
agregar_definicion(palabras, 'toballa', 'Pieza de felpa')
res1 = eliminar_palabra(palabras, 'caracter')
res2 = eliminar_palabra(palabras, 'toballa')
print(res1, res2)
```

[^toballa]: Para sorpresa de muchos, 'toballa' es una palabra que oficialmente hace parte del Español, aunque tal vez debería eliminarse.


#### Uso del método `pop` para eliminar un valor

En la segunda versión de la función se remplazó el operador `del` por un llamado al método `pop`. Al igual que antes, es necesario verificar que la llave efectivamente exista dentro del diccionario antes de hacer el llamado para que no se produzca ningún error.

```python
def eliminar_palabra(diccionario: dict, palabra: str)-> bool:
    palabra_eliminada = False
    if palabra in diccionario:
        diccionario.pop(palabra)
        palabra_eliminada = True
    return palabra_eliminada
```

El método `pop` tiene además un interesante resultado y es que retorna el valor eliminado. La siguiente sería una nueva versión de la función aprovechando esta característica.

```python
def eliminar_palabra(diccionario: dict, palabra: str)-> bool:
    palabra_eliminada = False
    if palabra in diccionario:
        definicion_eliminada = diccionario.pop(palabra)
        print("Se eliminó la llave", palabra, "que tenía la definición", definicion_eliminada)
        palabra_eliminada = True
    return palabra_eliminada
```

**Nota**: recuerde que no es recomendable mezclar las instrucciones de interacción (inputs y prints) con las instrucciones de su programa que manejan la información, hacen cálculos, etc.


### Eliminar todas las definiciones

Finalmente, Python ofrece una manera para eliminar con facilidad todos los elementos de un diccionario: el método `clear`. Por ejemplo, si queremos eliminar todos los elementos del diccionario `palabras` sólo debemos ejecutar la siguiente instrucción:

```python
palabras.clear()
```

## Usos de los diccionarios

Ya estudiamos todos los mecanismos para construir diccionarios, consultar y modificar valores, agregar nuevos valores y eliminar valores. Ahora vamos a estudiar algunos usos interesantes de los diccionarios.

### Histogramas basados en diccionarios

Una problemática relativamente común es la de contar cuántas veces aparecen ciertos valores dentro de algo más grande. Por ejemplo, cuántas veces aparece cada uno de los dígitos entre 0 y 9 dentro de un número entero, cuántas veces aparece cada letra dentro de una palabra, o cuántas veces aparece cada palabra dentro de un texto. Un problema relacionado es el de contar cuántos elementos de un conjunto caen dentro de unas ciertas categorías (ej. cuántas personas de un grupo nacieron en cada uno de los meses del año, cuántos estudiantes aprobaron un curso, cuántos reprobaron, etc.).

Matemáticamente, un histograma le asigna un número a cada uno de los valores posibles de un grupo: el número indica cuántas veces apareció el valor que estábamos contando (dígitos, letras, palabras, meses, etc.). Gráficamente, un histograma se representa con un gráfico de barras en el cual el tamaño de cada barra es proporcional a la cantidad de veces en que apareció cada uno de los valores.

![Ejemplo gráfico de histograma](./images/diccionarios_figura4.png)

Los diccionarios se prestan perfectamente para construir histogramas: las llaves serán los valores que queremos contar y los valores del diccionario indicarán la cantidad de veces que apareció cada uno. La siguiente función ilustra esto:

```python
def contar_vocales(texto: str) -> dict:
    """ Cuenta la cantidad de veces que aparece cada vocal dentro de un texto
    Parámetros:
      texto (str): El texto en el que van a contarse las vocales
    Retorno:
      (dict): Un diccionario donde las llaves son las vocales minúsculas y los valores
              son la cantidad de veces que aparece la vocal dentro del texto.
    """
    histograma = {}
    histograma['a'] = texto.lower().count('a')
    histograma['e'] = texto.lower().count('e')
    histograma['i'] = texto.lower().count('i')
    histograma['o'] = texto.lower().count('o')
    histograma['u'] = texto.lower().count('u')                
    return histograma
```
Esta función primero crea un histograma vacío y luego agrega una nueva llave para cada una de las vocales. El valor asociado a cada llave es el resultado de llamar al método `count()` de `str`, usando como parámetros la vocal correspondiente.

En el siguiente fragmento de código puede apreciarse el resultado de invocar la función usando como parámetro un texto en español bien conocido por ser un pangrama: una frase que usa todas las letras del alfabeto.

```python
>>> pangrama = 'Jovencillo emponzoñado de whisky, ¡qué figurota exhibe!'
>>> vocales = contar_vocales(pangrama)
>>> print(vocales)
{'a': 2, 'e': 5, 'i': 4, 'o': 6, 'u': 2}
```

![Diccionario con el histograma y representación gráfica](./images/diccionarios_figura5.png)

### Diccionarios como conjuntos

Un segundo uso posible de los diccionarios es representar conjuntos [^sets]. En un conjunto, cada valor puede aparecer máximo una vez y la pregunta más interesante es si un valor pertenece o no pertenece al conjunto. Cuando un conjunto se representa usando un diccionario, sólo nos interesan las llaves y no los valores.

[^sets]: En Python existe también el tipo de dato `set`, que se comporta de forma similar a una lista sin repeticiones. Más adelante se hablará un poco más de este tipo. Por ahora los diccionarios son suficientes para modelar conjuntos.

El siguiente ejemplo ilustrará este punto usando números como llaves en un diccionario y el valor booleano `True` como único valor del diccionario. 

```python
import random
def lanzar_dado(resultados: dict) -> None:
    """ Lanza un dado calculando aleatoriamente un número entre 1 y 6.
        Registra en el diccionario 'resultados' el valor que se obtuvo, asignándole
        el valor True a la llave que corresponde al valor.
    Parámetros:
      resultados (dict): Un diccionario que representa el conjunto de valores diferentes
                         que se han obtenido en los lanzamientos pasados.
    """
    valor = random.randint(1,6)
    resultados[valor] = True

# Lanzar el dado 6 veces y registrar los resultados obtenidos
def lanzar_6_dados()-> dict:
    """ Lanza el dado 6 veces y retorna un diccionario con los valores que se obtuvieron
    Resultado:
      (dict): Un diccionario donde sólo aparecen como llaves los valores que se
              obtuvieron en el lanzamiento del dado.
    """
    resultados = {}
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    lanzar_dado(resultados)
    return resultados

def contar_resultados_diferentes(resultados: dict) -> int:
    """ Cuenta cuántos resultados diferentes hubo
    Parámetros:
      resultados (dict): El conjunto de los resultados obtenidos representado
                         utilizando un diccionario. Si un valor aparece como
                         llave en el diccionario, significa que el valor se
                         obtuvo en el lanzamiento de los dados.
    Retorno:
      (int): La cantidad de resultados diferentes que hubo
    """
    diferentes = 0
    if 1 in resultados:
        diferentes += 1   
    if 2 in resultados:
        diferentes += 1
    if 3 in resultados:
        diferentes += 1
    if 4 in resultados:
        diferentes += 1
    if 5 in resultados:
        diferentes += 1
    if 6 in resultados:
        diferentes += 1
    return diferentes

# Lanzar el dado 6 veces y registrar los resultados obtenidos
resultados = lanzar_6_dados()
# Contar cuántos valores diferentes se obtuvieron
diferentes = contar_resultados_diferentes(resultados)
print("En 6 lanzamientos del dado se obtuvieron", diferentes, "valores diferentes")
```

El centro del programa es la función `lanzar_dado` la cual calcula aleatoriamente un valor entero entre 1 y 6. Este valor se almacena en el conjunto `resultados`, el cual está representado por un diccionario: cada vez que se lanza el dado, se agrega el valor obtenido al conjunto creando una nueva llave con el valor asociado True. Note que si el mismo valor aparece varias veces, en el diccionario sólo aparecerá una vez, puesto que no puede haber dos llaves iguales. 

La función `lanzar_6_dados` crea un conjunto vacío (un diccionario) y llama 6 veces a la función `lanzar_dado`, logrando que en el conjunto `resultado` queden todos los valores que salieron al menos una vez. Como el diccionario inicialmente estaba vacío, los valores que no hayan salido en el dado no aparecerán en el diccionario.

La función `contar_resultados_diferentes` revisa cuáles de los números entre 1 y 6 aparecen en el diccionario usando el operador `in` y retorna la cantidad. Por fuera de las funciones se llama a las últimas dos funciones y finalmente se imprime un mensaje informando cuántos valores diferentes se encontraron. Note que la tercera función podría haberse implementado fácilmente aplicando la función `len` sobre el conjunto para saber cuántos valores diferentes quedaron en este.


### Diccionarios como estructuras

Un tercer uso posible de los diccionarios es modelar elementos de la realidad que tienen estructuras complejas y que además deben tener la misma estructura. Por ejemplo, al principio del capítulo hablamos de celulares que se describen con la velocidad del procesador, cantidad de memoria, calidad de la cámara, tecnología de la pantalla, tamaño de la pantalla, capacidad de la pila, sistema operativo y versión del sistema operativo. Si queremos manejar la información de muchos celulares, tiene sentido organizar la información de cada uno dentro de un diccionario. Con esto nuestros programas quedarán mejor organizados, necesitaremos menos variables, y nos podremos asegurar de que no nos haga falta ningún atributo para un celular.

Para empezar a modelar nuestros celulares, listaremos sus características y le daremos un nombre sencillo a cada una:

* procesador: velocidad del procesador en GHz.
* memoria: cantidad de memoria en GB.
* camara: calidad de la cámara en mega-pixeles.
* pantalla: tecnología de la pantalla.
* ancho: ancho de la pantalla en pixeles.
* alto: alto de la pantalla en pixeles.
* pila: capacidad de la pila en miliamperios (mAh).
* sistema: nombre del sistema operativo.
* version: versión del sistema operativo.

A continuación, crearemos una función capaz de crear consistentemente diccionarios con estas llaves:

```python
def crear_celular(procesador: float, memoria: float, camara: float, 
                  pantalla: str, ancho: int, alto: int, pila: float, 
                  sistema: str, version: str)->dict:
  nuevo_celular = {}
  nuevo_celular['procesador'] = procesador
  nuevo_celular['memoria'] = memoria
  nuevo_celular['camara'] = camara
  nuevo_celular['pantalla'] = pantalla
  nuevo_celular['ancho'] = ancho
  nuevo_celular['alto'] = alto
  nuevo_celular['pila'] = pila
  nuevo_celular['sistema'] = sistema
  nuevo_celular['version'] = version
  return nuevo_celular
```

Esta función en realidad no tiene nada que no hayamos estudiado antes en esta sección: crea un nuevo diccionario y guarda los valores recibidos en las posiciones correspondientes del diccionario. En el siguiente fragmento usamos esta función para crear con facilidad cuatro celulares que se almacenan en diccionarios usando la misma estructura.

```python
cel1 = crear_celular(2.4, 64, 48, 'OLED', 1080, 2400, 5000, 'Android', '10')
cel2 = crear_celular(2.2, 64, 32, 'OLED', 768, 1080, 3500, 'Android', '8.1')
cel3 = crear_celular(2.0, 32, 18, 'Retina', 375, 812, 4200, 'iOS', '9.0')
cel4 = crear_celular(1.8, 16, 6, 'Retina', 375, 667, 4150, 'iOS', '8.1.4')
```

![Representación gráfica de los 4 diccionarios para representar celulares](./images/diccionarios_figura6.png)

Ahora bien, lo realmente interesante es que ahora podemos construir funciones que conozcan la estructura de estos diccionarios y hagan operaciones sobre los celulares aprovechandose de esta información. Por ejemplo, la siguiente función nos permite comparar los dos celulares para saber cuál tiene la mejor cámara:

```python
def mejor_camara(celular1: dict, celular2: dict)-> int:
    """ Busca cuál de los dos celulares tiene la mejor cámara (más mega-pixeles).
    Para que se pueda usar la función, los celulares deben representarse con 
    diccionarios que tengan una llave llamada 'camara' que indique la cantidad
    de mega-pixeles de la cámara del celular.    
    Parámetros:
      celular1 (dict): Es un diccionario que representa al primer celular. 
      celular2 (dict): Es un diccionario que representa al segundo celular.
    Retorno:
      (int): Retorna 1 si el primer celular tiene la mejor cámara.
             Retorna 2 si el segundo celular tiene la mejor cámara.
             Retorna 0 si las cámaras de los dos celulares son iguales.
    """
    mejor = 0
    camara1 = celular1['camara']
    camara2 = celular2['camara']    
    if camara1 > camara2:
        mejor = 1
    elif camara1 < camara2:
        mejor = 2
    return mejor
```
Teniendo en cuenta que ya creamos cuatro celulares usando nuestra función constructora (`cel1`, `cel2`, `cel3` y `cel4`) y que esa función nos garantiza la estructura de los diccionarios, podemos usar la nueva función como en el siguiente fragmento:

```python
>>> mejor_camara(cel1, cel2)
1
>>> mejor_camara(cel1, cel1)
0
>>> mejor_camara(cel3, cel2)
2
```

A continuación, construiremos una función que es capaz de identificar si alguno de los cuatro celulares tiene una versión determinada de un sistema operativo:

```python
def hay_celular_version_so(cel1: dict, cel2: dict, cel3: dict, cel4: dict, so: str, version: str) -> bool:
    """ Esta función indica si hay algún celular con la versión del sistema operativo
        indicada en los parámetros 'so' y 'version'.
        La función espera que los diccionarios de los celulares tengan una llave llamada
        'sistema' con el nombre del sistema operativo y una llave llamada 'version' con
        la versión del sistema.
    Parámetros:
      cel1 (dict): El diccionario que representa el primer celular
      cel2 (dict): El diccionario que representa el segundo celular
      cel3 (dict): El diccionario que representa el tercer celular
      cel4 (dict): El diccionario que representa el cuarto celular
    Retorno:
      (bool) : Retorna True si algún celular tiene exactamente el mismo sistema operativo
               en la misma versión que se pide en los parámetros 'so' y 'version'.
               Retorna False de lo contrario.
    """
    hay_celular_buscado = False
    if cel1['sistema'] == so and cel1['version'] == version:
        hay_celular_buscado = True
    elif cel2['sistema'] == so and cel2['version'] == version:
        hay_celular_buscado = True
    elif cel3['sistema'] == so and cel3['version'] == version:
        hay_celular_buscado = True
    elif cel4['sistema'] == so and cel4['version'] == version:
        hay_celular_buscado = True    
    return hay_celular_buscado
```
Observe que en esta función hemos usado un solo `if` seguido de varios `elif`. Esto ocurre porque una vez se encuentra un celular con el sistema operativo indicado, no es necesario seguir revisando los siguientes. Esto cambiaría si, en lugar de consultar si hay algún celular con las características descritas, quisiéramos contar cuántos celulares tienen las características descritas.

```python
def contar_celulares_version_so(cel1: dict, cel2: dict, cel3: dict, cel4: dict, so: str, version: str) -> int:
    """ Esta función cuenta cuántos celulares tienen la versión del sistema operativo
        indicada en los parámetros 'so' y 'version'.
        La función espera que los diccionarios de los celulares tengan una llave llamada
        'sistema' con el nombre del sistema operativo y una llave llamada 'version' con
        la versión del sistema.
    Parámetros:
      cel1 (dict): El diccionario que representa el primer celular
      cel2 (dict): El diccionario que representa el segundo celular
      cel3 (dict): El diccionario que representa el tercer celular
      cel4 (dict): El diccionario que representa el cuarto celular
    Retorno:
      (bool) : Retorna la cantidad de celulares que tienen exactamente el mismo 
               sistema operativo en la misma versión que se pide en los 
               parámetros 'so' y 'version'.
    """
    cantidad_celulares = 0
    if cel1['sistema'] == so and cel1['version'] == version:
        cantidad_celulares += 1
    if cel2['sistema'] == so and cel2['version'] == version:
        cantidad_celulares += 1
    if cel3['sistema'] == so and cel3['version'] == version:
        cantidad_celulares += 1
    if cel4['sistema'] == so and cel4['version'] == version:
        cantidad_celulares += 1
    return cantidad_celulares
```


### Diccionarios de diccionarios

Por último, vamos a describir un uso de los diccionarios que empieza a mostrar el verdadero poder de estas estructuras de datos. Hasta el momento, los valores que hemos introducido dentro de los diccionarios han sido tipos simples: `int`, `str`, `float` y `bool`. Ahora vamos a introducir también *diccionarios* dentro de los *diccionarios*.

Para ilustrar este punto vamos a continuar con el ejemplo de los celulares y construir un diccionario que va a contener todos los celulares que queremos comparar. En este diccionario las *llaves* serán los *nombres de los celulares* y los *valores* serán los *diccionarios con el resto de características*.

Suponiendo que ya tenemos nuestros cuatro celulares (`cel1`, `cel2`, `cel3` y `cel4`), podemos armar nuestro diccionario de celulares usando las siguientes instrucciones:

```python
celulares = {}
celulares['AmazingCel'] = cel1
celulares['BoringCel'] = cel2
celulares['CheapCel'] = cel3
celulares['DumbCel'] = cel4
```

La siguiente imagen muestra gráficamente el resultado de esta ejecución. En la parte superior podemos ver las cuatro variables anteriores apuntando a cada uno de los diccionarios que representan celulares. En la parte inferior podemos ver que los valores en el nuevo diccionario `celulares` *apuntan* a los mismos diccionarios que identificamos con las variables.

![Representación gráfica del diccionario de celulares](./images/diccionarios_figura7.png)


Observe ahora lo que pasa si intentamos extraer un valor del diccionario `celulares` usando el nombre de un celular (los cambios de línea los agregamos para facilitar la lectura):

```python
>>> print(celulares['AmazingCel'])
{'procesador': 2.4, 'memoria': 64, 'camara': 48, 
'pantalla': 'OLED', 'ancho': 1080, 'alto': 2400, 
'pila': 5000, 'sistema': 'Android', 'version': '10'}
```

Más interesante aún es lo que pasa si encadenamos los llamados para extraer una propiedad del celular:

```python
>>> print(celulares['AmazingCel']['procesador'])
2.4
```

Vamos a construir ahora una función similar a la que construimos antes para comparar dos celulares. La principal diferencia es que ahora usaremos nuestro nuevo diccionario de celulares y los nombres de los celulares que queremos comparar.

```python
def mejor_camara_con_nombres(celulares: dict, nombre1: str, nombre2: dict)-> str:
    """ Busca cuál de los dos celulares tiene la mejor cámara
    Parámetros:
      celulares (dict): Un diccionario donde las llaves son los nombres de los celulares
                        y los valores son diccionarios que representan celulares
      nombre1 (str): El nombre del primer celular que se quiere comparar
      nombre2 (str): El nombre del segundo celular que se quiere comparar
    Retorno:
      (str): Retorna el nombre del celular que tiene la mejor cámara o "Empate" si
             las cámaras de los dos celulares son iguales.
             Si sólo uno de los nombres corresponde al de un celular, retorna ese nombre.
             Si ningún nombre corresponde al de un celular, retorna "Nombres inválidos".
    """
    # Extraer los celulares del diccionario usando su nombre
    celular1 = celulares.get(nombre1, None)
    celular2 = celulares.get(nombre2, None)
    # Ninguno de los dos nombres era correcto
    if celular1 is None and celular2 is None:
        nombre_mejor = "Nombres inválidos"
    # Sólo el segundo nombre era correcto
    elif celular1 is None and celular2 is not None:
        nombre_mejor = nombre2
    # Sólo el primer nombre era correcto
    elif celular1 is not None and celular2 is None:
        nombre_mejor = nombre1
    # Los dos nombres eran correctos así que hay que comparar los celulares
    else:
        nombre_mejor = "Empate"
        numero_mejor = mejor_camara(celular1, celular2)
        if numero_mejor == 1:
            nombre_mejor = nombre1
        elif numero_mejor == 2:
            nombre_mejor = nombre2
    return nombre_mejor
```

La nueva función recibe el diccionario con todos los celulares y el nombre de los dos celulares que se quieren comparar. Lo primero que hace es intentar extraer los diccionarios que representan a cada uno de los celulares, usando sus nombres. Para esto se utiliza el llamado `celulares.get(nombre1, None)`: si `nombre1` no coincide con el nombre de ningún celular, el resultado retornado es el valor nulo `None`. Si ninguno de los dos nombres era correcto, `celular1` y `celular2` tendrán el valor `None` y la función retornará la cadena "Nombres inválidos". Si sólo uno de los dos nombres es válido, entonces se retornará el celular al que corresponda el nombre válido. Finalmente, si los dos nombres son válidos, se usará la función `mejor_camara` para calcular cuál de los dos celulares es mejor.

Veamos ahora cómo se usaría esta función:

```python
>>> print(mejor_camara_con_nombres(celulares, 'DumbCel', 'BoringCel'))
BoringCel
>>> print(mejor_camara_con_nombres(celulares, 'DumbCel', 'FalseCel'))
DumbCel
>>> print(mejor_camara_con_nombres(celulares, 'FalsestCel', 'FalseCel'))
Nombres inválidos
>>> print(mejor_camara_con_nombres(celulares, 'CheapCel', 'CheapCel'))
Empate
```

Por ahora no vamos a ahondar más en el tema de los diccionarios dentro de otros diccionarios. Para poder explotar al máximo el poder que ofrecen tenemos que esperar a introducir los conceptos principales de recorrido de estructuras de datos (Nivel 3). Cuando hayamos pasado ese punto, retomaremos la discusión.


**¡Atención!:** Los diccionarios sólo pueden usarse como valores dentro de otros diccionarios. **NO** pueden usarse como llaves.


## Mutabilidad en diccionarios

Para cerrar este capítulo sobre diccionarios vamos a volver a la discusión que habíamos iniciado sobre la *mutabilidad* de los diccionarios. A diferencia de otros tipos de datos, los diccionarios pueden cambiar. Esto significa que, cuando se agrega, se modifica o se elimina una llave de un diccionario, el diccionario se modifica pero sigue siendo *el mismo diccionario*. 

Esta característica es muy importante y hay que tenerla muy en cuenta cuando se utilizan diccionarios en los parámetros de una función. En síntesis, el hecho de que los diccionarios sean mutables hace que todos los cambios que se hacen a un diccionario que llegue a una función como un parámetro, se vean reflejados también fuera de la función.

Veamos esto con un ejemplo sencillo:

```python
def agregar_definicion(diccionario: dict, palabra: str, definicion: str)-> None:
  diccionario[palabra] = definicion
```

Esta función ya la habíamos estudiado y lo único que hace es agregar (o reemplazar) una llave dentro del diccionario. Ahora veamos lo que sucede cuando se invoca esta función y se imprime su contenido:

```python
>>> palabras = {}
>>> agregar_definicion(palabras, 'palabra1', 'definicion1')
>>> print(palabras)
{'palabra1': 'definicion1'}
>>> agregar_definicion(palabras, 'palabra2', 'definicion2')
>>> print(palabras)
{'palabra1': 'definicion1', 'palabra2': 'definicion2'}
```
El punto central acá es que en todo el ejemplo sólo hay un diccionario. Cuando se invoca la función `agregar_definicion` y se pasa el diccionario `palabras` como parámetro, es exactamente el mismo diccionario el que se recibe y se modifica. Este comportamiento es propio de los diccionarios (y de otros tipos de datos que estudiaremos más adelante), se conoce como paso de parámetros **por referencia**.

Esto no ocurre con tipos como `int` o `str`, en los cuales el paso de parámetros se hace **por valor**. Es decir, el valor que se recibe dentro de la función es idéntico al que se usó como parámetro, pero no es el mismo (es una copia, no una referencia). Esto se muestra en el siguiente ejemplo:

```python
def modificar(entero: int, cadena: str)->bool:
    entero += 100
    cadena += '!!!!'
    print(entero, cadena)
    return True
numero = 1
texto = "Hola Mundo"
resultado = modificar(numero, texto)
print(numero, texto)
```

En este caso, se ha definido una función que modifica los parámetros que recibe e imprime los valores modificados. Por fuera de la función, se crean dos variables que luego se usan para invocar a la función. Finalmente, se imprimen las variables que se usaron para invocar la función. El resultado de la ejecución son las siguientes dos líneas:

```
101 Hola Mundo!!!!
1 Hola Mundo
```

La primera línea se imprime desde adentro de la función y demuestra que los parámetros `entero` y `cadena` se modificaron dentro de la función. La segunda línea muestra que las variables con las que se invocó la función, `numero` y `texto`, no sufrieron ningún cambio. 


### Copias de diccionarios ###

Finalmente, vamos a desarrollar una función en la que no queremos que se modifique el diccionario original, sino que queremos que se construya uno nuevo. La nueva función `agregar_definicion_con_copia` logra este resultado y retorna un diccionario con todos los elementos que tenía el diccionario original y también con el elemento adicional que se está agregando.

```python
def agregar_definicion_con_copia(diccionario: dict, palabra: str, definicion: str)-> dict:
  copia = diccionario.copy()
  copia[palabra] = definicion
  return copia
```

El punto importante dentro de este ejemplo es el uso del método `copy()`, el cual realiza una copia completa del diccionario cuando es invocado. De esta manera, el diccionario que se modifica no es el que llegó como parámetro, sino una copia de este. Esto se ve claramente al ejecutar la nueva función:

```python
>>> palabras = {'palabra1': 'definicion1', 'palabra2': 'definicion2'}
>>> copia_palabras = agregar_definicion_con_copia(palabras, 'p99', 'def99')
>>> palabras
{'palabra1': 'definicion1', 'palabra2': 'definicion2'}
>>> copia_palabras
{'palabra1': 'definicion1', 'palabra2': 'definicion2', 'p99': 'def99'}
```


**¡Atención!:** El método `copy()` hace sólo una copia *superficial* del diccionario en lugar de una copia profunda. Esto significa que dentro del nuevo diccionario habrá copias de todos los elementos inmutables, pero habrá referencias a los mismos elementos mutables. En particular, si se hace una copia de un diccionario con diccionarios por dentro, el nuevo diccionario tendrá los mismos diccionarios en lugar de copias también de esos diccionarios.  


## Ejercicios

1. Construya un diccionario con las alturas sobre el nivel del mar de las capitales de los países suramericanos. Use los nombres de las ciudades, usando mayúsculas al principio de las palabras, como llaves y las alturas como valores. Es decir, las llaves deben ser 'Bogotá', 'Buenos Aires'. etc.

2. Escriba una función que reciba el diccionario con las alturas de las ciudades y los nombres de dos ciudades y que retorne el nombre de la ciudad que esté ubicada a una mayor altura. La función debe ser capaz de funcionar incluso si en el nombre de las ciudades se usan mayúsculas y minúsculas de forma diferente a como están en el diccionario (por ejemplo, 'BoGoTá' y 'BUENOS aires'). Si alguno de los dos nombres no corresponde a una ciudad, la función debe retornar el valor `None`.

3. Escriba una función que reciba un número entero y calcule un diccionario en el que cada llave es un dígito y los valores asociados son la cantidad de veces que aparece el dígito en el número entero. Si un dígito no aparece en el número, no debe aparecer en el diccionario.

4. Escriba una función que reciba un número entero y retorne el dígito que aparece más veces dentro del número.

5. Con base en el ejemplo del diccionario de celulares, construya una función que reciba los diccionarios de 4 celulares y cuente cuántos de estos celulares tienen más de 16 GB de memoria.

6. Con base en el ejemplo del diccionario de celulares, construya una función que reciba los diccionarios de 4 celulares y diga cuál es el celular que tiene la mayor cantidad de pixeles en la pantalla.

7. Con base en el ejemplo del diccionario de celulares, construya una función que reciba los diccionarios de 4 celulares y los modifique para duplicar la capacidad de la pila de todos.

8. Modifique el programa que calcula cuáles valores salieron en los lanzamientos de 6 dados para que ahora calcule un histograma en el que se pueda saber cuántas veces salió cada número.




#### Notas 

