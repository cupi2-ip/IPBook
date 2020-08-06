
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

Estudiemos ahora, paso por paso, lo que hace el programa. En las líneas 1 a 10 se define una nueva función que no se ejecutará por ahora. En las líneas 12 y 13 se definen dos variables: la primera es de tipo `str` y tiene como valor `"cadena inicial"`; la segunda es de tipo `dict` y tiene como valor un diccionario qué únicamente tiene una llave ("`inicial"`) con el valor `0` asociado.

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



### Parámetros por valor y por referencia

Después de estudiar el ejemplo anterior, podemos explicar mejor el significado de pasar parámetros por valor y por referencia cuando se invoca una función.

Un parámetro se pasa **por valor**, cuando el valor se copia para que se utilice dentro de la función. Esto es lo que ocurre con algunos tipos básicos como `int`, `float` y `bool`, y también con tipos inmutables como `str` y `tuple` (que estudiaremos más adelante).

Por otro lado, un parámetro se pasa **por referencia**, cuando lo que se hace es entregarle a la función una referencia al elemento, sin copiarlo [^cpp] . Esto quiere decir que si la función hace cambios al elemento, esos cambios los podrá ver quien haya invocado a la función. Esto va a ocurrir en Python con tipos de datos como los diccionarios (`dict` que ya estudiamos, y las listas `list` que estudiaremos en el siguiente nivel).

[^cpp]: En un lenguaje como C o C++, que tienen acceso de bajo nivel a la memoria, el paso por referencia se basa en el paso de apuntadores. Esto hace posible modificar los apuntadores desde adentro de la función (método), lo cual no es posible en Python. Para no complicar más la explicación, hemos ajustado la definición de paso por referencia a lo que tendría sentido para Python.
 

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


### Paso por "referencia al objeto"

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

A continuación estudiaremos dos características adicionales de Python que permiten manejar con un poco más de flexibilidad los parámetros de las funciones que se definan y se invoquen. Estas características usualmente no están disponibles en otros lenguajes.

### Parámetros nombrados

La primera característica para estudiar tiene que ver con la forma de hacer referencia a los parámetros de una función en el momento de la invocación. Hasta ahora, siempre hemos utilizado el mecanismo basado en la posición: el primer valor en la invocación corresponde al primer parámetro, el segundo valor en la invocación corresponde al segundo parámetro, y así sucesivamente. Sin embargo, en Python es posible hacer explícito el nombre de los parámetros en el momento de la invocación de tal forma que se puedan invocar en un orden diferente al que se tiene en la declaración.

Veamos un ejemplo:

```{code-block} python
def imprimir_nombre(nombre: str, apellido: str) -> None:
    print(nombre + " " + apellido)

imprimir_nombre("Juan", "Perez")  # Imprime "Juan Perez"
imprimir_nombre(nombre = "Juan", apellido = "Perez")  # Imprime "Juan Perez"
imprimir_nombre(apellido = "Perez", nombre = "Juan")  # Imprime "Juan Perez"
```

En este ejemplo hacemos tres invocaciones a la función:

1. En la primera no se usan los nombres de los parámetros, así que la invocación se hace por posición.

2. En la segunda se usan los nombres de los parámetros, en el mismo orden en el que están definidos.

3. En la tercera también se usan los nombres pero un orden diferente al de la definición. En este caso el resultado es el esperado porque gracias al nombre la función puede reconocer a qué parámetro corresponde cada valor.

Veamos ahora unos ejemplos en los que no se utilicen los nombres de todos los parámetros:

```{code-block} python
imprimir_nombre(apellido = "Perez", "Juan")  # Falla
imprimir_nombre("Perez", nombre="Juan")  # Falla
imprimir_nombre("Juan", apellido = "Perez")  # Imprime "Juan Perez"
```

1. En el primer caso, se presentará el error `SyntaxError: positional argument follows keyword argument`. Este error nos indica que los valores *sin nombre* no deberían ir después de valores con nombre.

2. En el segundo caso, se presentará el error `imprimir_nombre() got multiple values for argument 'nombre'`. Este error nos indica que Python intentó asignarle el primer valor al primer parámetro (`nombre`) y luego le intentó asignar el valor nombrado al mismo parámetro. Como resultado, el parámetro `nombre` recibió múltiples valores mientras que `apellido` no recibió ninguno.

3. El tercer caso es exitoso: el primer valor se asigna al primer parámetro y el segundo valor se asigna al parámetro `apellido`. El resultado es que todos los parámetros de la función reciben un valor y por ende se puede hacer la invocación.

El uso de parámetros nombrados no es obligatorio, pero puede ayudar a hacer más legible el código, especialmente cuando no hay un orden en los parámetros que sea fácil de predecir. Por ejemplo, si tuviéramos una función para evaluar un polinomio de la forma $a \cdot x^{2} + b \cdot x + c$, la función se invocaría como `evaluar_polinomio(3, 5, 7)` o como evaluar_polinomio(7, 5, 3)? Para evitar la confusión se podría hacer uso de los nombres de los parámetros: `evaluar_polinomio(a=3, b=5, c=7)`.


### Parámetros por defecto / opcionales

La segunda característica que queremos que usted conozca es la posibilidad de definir valores por defecto para los parámetros. Esto hace posible hacer llamados a funciones utilizando sólo algunos de los parámetros y, en conjunto con los parámetros nombrados, puede hacer que el código de un programa sea mucho más sencillo.

Por ejemplo, veamos la definición de la función `count` de `str` que nos permite contar cuántas veces aparece una subcadena en otra:

```{code-block} python
>>> help(str.count)
S.count(sub[, start[, end]]) -> int
```

Lo que esta definición nos dice es que el parámetro `sub` es obligatorio, y puede estar seguido de un segundo parámetro (`start`), el cual podría estar seguido de un tercer parámetro (`end`). Aunque no lo podemos ver, en esta función `start` y  `end` tienen valores por defecto: `start` tiene el valor 0 mientras que `end` tiene un valor igual a la longitud de la cadena. De esta forma, si no se especifica un inicio se empezará desde el primer caracter, y si se especifica un inicio pero no un fin, se irá hasta el final de la cadena.

Veamos ahora un pequeño ejemplo para ilustrar la sintaxis:

```{code-block} python
def replicar (cadena: str, cantidad: int = 2) -> str:
  return cadena * cantidad
```

En este caso, estamos definiendo una función con dos parámetros: el primero es obligatorio, pero el segundo puede hacerse explícito o no. Si no se incluye al hacer una invocación, su valor por defecto será 2. Note que para parámetro `cantidad` se ha indicado primero el tipo (`int`) y luego el valor por defecto.


```{warning} Parámetros por defecto
:class: warning

Use valores por defecto para los parámetros únicamente cuando 
sea evidente cuál debería ser el valor por defecto del parámetro.
Si el que invoque la función tiene que pensar mucho sobre el valor
por defecto del parámetro, posiblemente haya sido un error ponerle
un valor por defecto.
```

```{tip} Simplificar con parámetros por defecto
:class: tip

Use parámetros por defecto para simplificar el llamado a funciones que tengan una gran flexibilidad a través de un gran número de parámetros. Por ejemplo, hay librerías con funciones que esperan más de 10 parámetros pero el hecho de que todos tengan valores por defecto hace que cualquier invocación pueda concentrarse en los parámetros que realmente valgan la pena.
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

A lo largo de los años, diferentes lenguajes han experimentado con diversas mecanismos para el paso de parámetros. Aunque puede parecer un asunto sencillo, escoger un método particular puede tener un impacto muy importante en el desempeño de una aplicación. Por ejemplo, en el caso de Java en todos los llamados los parámetros se pasan por valor: esto quiere decir que siempre se hacen copias, aunque cuando se trata de objetos (tipos no simples) se hacen copias de las refencias a los objetos. Esto le permite a Java tener un mecanismo homogéneo de invocación y paso de parámetros, simplificar el manejo de la pila de ejecución y aumentar la seguridad del lenguaje a través de la protección de los apuntadores.

Tradicionalmente, los valores con los que se invoca una función (o método) se asignan a los parámetros con base en la posición. Esto es algo que viene del cálculo: si tenemos definida la función $f(x, y)$, cuando evaluemos la función (por ejemplo $f(2,3)$), estamos acostumbrados a que el valor 2 se use para $x$ y el valor 3 se use para $y$. Sin embargo, el uso de parámetros nombrados ha empezado a hacerse más popular y es una característica de varios lenguajes *modernos* como Scala o Kotlin.

```{code-block} scala
def imprimirNombre(nombre: String, apellido: String): Unit = {
  println(nombre + " " + apellido)
}

imprimirNombre("Juan", "Perez")  // Imprime "Juan Perez"
imprimirNombre(nombre = "Juan", apellido = "Perez")  // Imprime "Juan Perez"
imprimirNombre(apellido = "Perez", nombre = "Juan")  // Imprime "Juan Perez"
```

Finalmente, tenemos a continuación un pequeño ejemplo de **Smalltalk**, un lenguaje diseñado hace cerca de 40 años. En Smalltalk todos los parámetros son nombrados porque hacen parte del nombre mismo de los métodos. En el siguiente bloque mostramos la definición del método `imprimirNombre:apellido:`, que recibe dos parámetros y luego los imprime como en el ejemplo anterior en Scala.

```{code-block} Smalltalk
imprimirNombre: elNombre apellido: elApellido

Transcript show: elNombre, ' ', elApellido
```

Con respecto a los valores por defecto para los parámetros, encontramos que es posible asignar valores por defecto en lenguajes como C++ o JavaScript, pero no en Java. Al igual que en Python, se debe tener cuidado de asignarle valores por defecto a los últimos parámetros de una función para que esos parámetros sean realmente opcionales.


