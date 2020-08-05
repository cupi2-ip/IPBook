
# Paso de parámetros

```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```

```{admonition} Objetivo de la sección
El objetivo de esta sección es estudiar con un poco más de profundidad el mecanismo de paso de parámetros y presentar además algunas características que tiene el lenguaje Python pero no otros.
```

Hasta el momento hemos utilizado el mecanismo de paso de parámetros cada vez que hemos invocado una función, pero no hemos entrado en mucho detalle sobre lo que está pasando. En esta sección vamos a estudiar este proceso en más profundidad y vamos a diferenciar entre los dos mecanismos disponibles en Python: paso de parámetros *por valor* y paso de parámetros *por referencia*. 

Además, estudiaremos un par características adicionales que ofrece Python para manejar los parámetros de una función con mayor flexibilidad. 
Usar estas características es totalmente opcional y, como usualmente no están disponibles en otros lenguajes, no es recomendable acostumbrarse a usarlas siempre.



## Paso de parámetros por valor y por referencia

Para empezar, vamos a recoerdar la diferencia entre el operador `==` y el operador `is`: el primero lo podemos usar para comparar los valores de unas variables para ver si son iguales, mientras que el segundo nos sirve para saber sin son *el mismo*. Esto lo podemos ver en el siguiente ejemplo en el cual estamos construyendo dos diccionarios y luego los comparamos usando los dos operadores:

```{code-block} python
---
lineno-start: 1
---
>>> d1 = {"k1" : 1}
>>> d2 = {"k1" : 1}
>>> d1 == d2
True
>>> d1 is d2
False
```

* En el caso del operador `==`, el valor obtenido es `True` porque los dos diccionarios tienen las mismas llaves y los mismos valores asociados. Se dice entonces que `==` compara los **valores**.

* En el caso del operador `is`, el valor obtenido es `False` porque estamos hablando de dos diccionarios:  en la línea 1 se construye el primero y en la siguiente línea se construye el segundo. Es apenas una casualidad que las llaves y los valores sean los mismos: si revisáramos la memoria del computador, nos daríamos cuenta que cada diccionario ocupa un espacio diferente en la memoria. Se dice entonces que `is` compara las **referencias** (en este contexto, una referencia sería la dirección de memoria donde se encuentre un diccionario). 


```{important} Valores vs. referencias
:class: warning

El operador `==` se usa para comparar valores.

El operador `is` se usa para comparar referencias.
```

### Parámetros en una función

Veamos ahora lo que pasa cuando se tienen parámetros de diferentes tipos en una función. Para esto estudiemos el siguiente programa:

```{code-block} python
---
lineno-start: 1
---
def funcion(p1: str, p2: str, p3: dict, p4:dict) -> None:
    print("--> Valores recibidos:", p1, p2, p3, p4)
    print("--> Comparar las cadenas:", p1 == p2)
    print("--> Comparar los diccionarios:", p3 == p4, p3 is p4)
    
    p1 = "nueva cadena"
    p3["nuevo valor"] = 99
    print("--> Valores modificados:", p1, p2, p3, p4)
    p3 = {"ultimo": 1}
    print("--> Valores modificados de nuevo:", p3, p4)    
   
cadena = "cadena inicial"
diccionario = {"inicial": 0}

print("Antes de llamar a la función: ", cadena, diccionario)
funcion(cadena, cadena, diccionario, diccionario)
print("Después de llamar a la función: ", cadena, diccionario)
```

En las líneas 1 a 10 se define una nueva función que explicaremos más adelante. En las líneas 12 y 13 se definen dos variables: la primera es de tipo `str` y tiene como valor `"cadena inicial"`; la segunda es de tipo `dict` y tiene como valor un diccionario qué únicamente tiene una llave ("`inicial"`) con el valor `0` asociado.

En la 15 se imprime un mensaje en la consola que muestra el valor de las dos variables: `Antes de llamar a la función:  cadena inicial {'inicial': 0}`. En el bloque de código que se encuentra más abajo se puede ver todo lo que imprime el programa.

Luego, en la línea 16 se invoca a la función: la variable `cadena` se usa para los parámetros `p1` y `p2`; la variable `diccionario` se asigna a los parámetros `p3` y `p4`.

La función que definimos imprime los parámetros que recibimos (línea 1), imprime el resultado de comparar `p1` y `p2` (línea 3), e imprime el resultado de comparar `p3` y `p4` usando tanto `==` como `is`. Como es de esperarse, en todos los casos el resultado que se muestra en la consola es `True`.

A partir de la la siguiente línea empiezan a ocurrir cosas más interesantes. En la línea 6, se le asigna un nuevo valor a `p1` que, recordemos, es de tipo `str`. En la línea 7 se le asigna también un nuevo valor a la llave `"nuevo_valor"` dentro del diccionario `p3`. 

En la línea 8 se imprimen los valores modificados y se obtiene la siguiente cadena: `--> Valores modificados: nueva cadena cadena inicial {'inicial': 0, 'nuevo valor': 99} {'inicial': 0, 'nuevo valor': 99}`:

* En `p1` vemos el nuevo valor que le asignamos en la línea 6.
* En el parámetro `p2` vemos el valor inicial que tenía el parámetro. Esto se explica porque cuando hicimos la asignación Python creó una variable nueva,  local a la función, llamada `p1` y con valor inicial `99`. Es decir que `p1` y `p2` ahora van a ser dos elementos independientes.
* En `p3` vemos que tenemos ahora un diccionario que además del valor inicial tiene el nuevo valor que agregamos en la línea 7.
* En `p4` vemos que también tenemos el nuevo valor: en la línea 7 le agregamos una nueva llave al diccionario al que apuntaba la referencia `p3`, pero ese diccionario era *el mismo* al que apuntaba `p4`. Por eso cuando modificamos el diccionario `p3` también se modificó el diccionario que conocemos como `p4` (¡es el mismo!)

A continuación, la línea 9 hace una nueva asignación pero sobre `p3`: se construye un nuevo diccionario con la llave `"ultimo"` y se almacena en `p3`. En la siguiente línea volvemos a imprimir los diccionarios: `--> Valores modificados de nuevo: {'ultimo': 1} {'inicial': 0, 'nuevo valor': 99}`

* En `p3` ahora tenemos sólo el nuevo diccionario (el que tiene sólo la llave llamada `"ultimo"`.
* En `p4` tenemos el diccionario que teníamos en el paso anterior (el que tiene las llaves `"inicial"` y `"nuevo valor"`.

Esto concluye la ejecución de la invocación a la función así que el programa sigue adelante ejecutando la línea 17, en la cual imprime nuevamente las variables `cadena` y `diccionario`, con lo cual obtenemos el siguiente resultado: `Después de llamar a la función:  cadena inicial {'inicial': 0, 'nuevo valor': 99}`.

Este último resultado nos muestra lo siguiente:

* La variable `cadena` sigue teniendo el mismo valor asociado. A pesar de que la función modificó a `p1`, el valor de `cadena` no cambió. Esto pasa porque, para efectos prácticos, `p1` y `p2` eran *copias* de `cadena`.

* La variable `diccionario` muestra que la primera modificación al diccionario `p3` quedó registrada, pero no la segunda. Esto pasa porque el diccionario inicial se pasó como parámetro a la función y nunca se creó una copia de él. Cuando modificamos a `p3` en la línea 7 estábamos modificando el diccionario inicial. Luego, en la línea 9 se creó un nuevo diccionario y ese se asignó a la variable `p3`, pero eso no tiene por qué tener ningún efecto en el diccionario al que señalaba `p4` y mucho menos al que señalaba la variable `diccionario`.


El siguiente bloque muestra el resultado completo de ejecutar el programa.

```{code-block} python
---
lineno-start: 1
---
Antes de llamar a la función:  cadena inicial {'inicial': 0}
--> Valores recibidos: cadena inicial cadena inicial {'inicial': 0} {'inicial': 0}
--> Comparar las cadenas: True
--> Comparar los diccionarios: True True
--> Valores modificados: nueva cadena cadena inicial {'inicial': 0, 'nuevo valor': 99} {'inicial': 0, 'nuevo valor': 99}
--> Valores modificados de nuevo: {'ultimo': 1} {'inicial': 0, 'nuevo valor': 99}
Después de llamar a la función:  cadena inicial {'inicial': 0, 'nuevo valor': 99}
```


### Parámetros por valor y por referencia

Después de estudiar el ejemplo anterior, ya podemos explicar bien el significado de pasar parámetros por valor y por referencia cuando se invoca una función.

Un parámetro se pasa **por valor**, cuando el valor se copia para que se utilice dentro de la función. Esto es lo que ocurre con algunos tipos básicos como `int`, `float` y `bool`, y también con tipos inmutables como `str` y `tuple` (que estudiaremos más adelante).

Por otro lado, un parámetro se pasa **por referencia**, cuando lo que se hace es entregarle a la función una referencia al elemento, sin copiarlo. Esto quiere decir que si la función hace cambios al elemento, esos cambios los podrá ver quien haya invocado a la función. Esto va a ocurrir en Python con tipos de datos como los diccionarios (`dict` que ya estudiamos, y las listas `list` que estudiaremos en el siguiente nivel).

Veamos un último ejemplo para ilustrar ese punto:

```{code-block} python
---
lineno-start: 1
---
def limpiar_diccionario(el_diccionario: dict) -> None:
    el_diccionario.clear()
    
d = {"a":1, "b":2, "c": 3}
print(d)
limpiar_diccionario(d)
print(d)
```
En este programa se crea un diccionario con 3 elementos y luego se pasa **por referencia** a la función `limpiar_diccionario`, que llama el método `clear` sobre el diccionario que recibe por parámetro. Cuando imprimamos de nuevo el diccionario `d`, este va a estar vacío porque la función lo limpió. Si los diccionarios se pasaran por valor (es decir que se crearan copias en cada invocación), no veríamos ningún cambio sobre el diccionario después de la invocación.


### Paso por referencia al objeto

La realidad del paso de parámetros en Python es más complicada de lo presentada en las secciones anteriores. En Python, los parámetros se dice que pasan como *referencia a los objetos*. Esto quiere decir que, incluso los tipos que parece que se pasan por valor, se pasan como referencia. Esto tiene como consecuencias principales un minúsculo ahorro en el *uso de la memoria* y una mejora posiblemente imperceptible en el *desempeño* de los programas.

No ahondaremos en la explicación porque no vale la pena entrar en una exposición más compleja sobre la mecánica del paso de parámetros por referencia a objetos, ni sobre las estrategias que utiliza Python para representar datos en memoria, ni mucho menos sobre el hecho de que en Python todo es un *objeto*. La conclusión importante es que para efectos prácticos los valores inmutables se comportan como si se pasaran por valor y los mutables como si se pasaran por referencia.

```{important} Tenga claro cuáles valores son mutables y cuáles inmutables
:class: warning

Los tipos básicos como `int`, `float` y `bool`, y los inmutables como `str` y `tuple` se comportan como si se pasaran **por valor**.

Los tipos complejos y mutables como `dict` y `list` se comportan como si se pasaran **por referencia**.
```

### Ejercicios

Para cada uno de los ejercicios asegúrese de imprimir los valores que use para sus pruebas antes y después de hacer las invocaciones.

1. Vamos a representar a un estudiante usando un diccionario con 4 llaves: `"nombre"`, para almacenar su nombre; y `"matemáticas"`, `"lenguaje"` y `"ciencias"` para almacenar las notas en cada una de las 3 materias. Escriba una función que reciba un estudiante (un diccionario) y retorne su promedio.


2. Ahora escriba una función que reciba un estudiante (un diccionario), el nombre de una de las tres materias, y una nota, y le asigne al estudiante la nueva nota en esa materia.

3. Escriba una función que reciba tres estudiantes (tres diccionarios) y el nombre de una de las tres materias. La función debe aumentar la nota de cada estudiante en la materia en un 10% del promedio de los tres estudiantes en esa materia.



## Parámetros en Python



Estas características usualmente no están disponibles en otros lenguajes.



parámetros nombrados: orden vs. nombre
The Java version is more implicit. The Python version is more explicit. 

parámetros por defecto / Opcionales:
usados con los nombres



```{code-block} python
S.find(sub[, start[, end]]) -> int
S.count(sub[, start[, end]]) -> int


'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'
```



### Ejercicios


1. Construya una función que reciba dos números enteros como parámetros: si el primer número es par, la función debe retornar la suma de los dos números; de lo contrario, debe retornar la multiplicación de los dos números.

2. Invoque su función con varias parejas de números igual que como lo ha estado haciendo hasta el momento.

3. Invoque la función nuevamente, pero esta vez utilice los nombres de los parámetros: pruebe usando los parámetros en el orden en el que están definidos en la función y también en el orden opuesto. Compruebe que el resultado en cada caso es el que usted esperaría.

4. Invoque la función usando sólo un parámetro. Si no funciona, asegúrese de entender el error que reciba.

5. Modifique la función para que tenga valor por defecto **sólo para el segundo parámetro**.

6. Repita las invocaciones con uno y con dos parámetros, tanto con los nombres como sin ellos. ¿En qué casos se produjeron errores?

7. Modifique ahora la función para que tenga valor por defecto **sólo para el primer parámetro**. Vuelva a hacer las pruebas y revise en qué casos se producen errores.




## Más allá de Python

valor, referencia, referencia al objeto



Tradicionalmente, los valores con los que se invoca una función se asignan a los parámetros con base en la posición. Esto 

...
Named parameters: Scala, Kotlin, 
def printName(first: String, last: String): Unit = {
  println(first + " " + last)
}

printName("John", "Smith")  // Prints "John Smith"
printName(first = "John", last = "Smith")  // Prints "John Smith"
printName(last = "Smith", first = "John")  // Prints "John Smith"

The Java version is more implicit. The Python version is more explicit. 


Default:
C++ sí
Java no
JavaScript sí


