

# Errores frecuentes

```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```

En esta sección presentamos algunos de los errores que encontramos frecuentemente en los programas de muchos estudiantes. Revíselos con cuidado y asegúrese de entenderlos para no cometer esos mismos errores.

##  Errores con variables y asignaciones

### Confundir una variable con una cadena

Cuando se empieza a programa, es habitual confundir el nombre de una variable con el valor de una cadena. Recuerde que el nombre de una variable nunca lleva comillas mientras que cualquier cosa entre comillas será un literal.

Considere el siguiente programa. Es más complicado, pero ha sido construido buscando para reflejar la confusión común.

```{code-block} python
---
lineno-start: 1
---
variable = 'cadena'
cadena = 'variable'
lenguaje = 'python'
print(cadena * 3)
print('cadena' * 3)
print(python * 5)
```

* En la línea 1, se crea una variable que se llama `variable`, es de tipo cadena (`str`) y tiene el valor `'cadena'`.
* En la línea 2, se crea una variable llamada `cadena`, es de tipo cadena (`str`) y tiene el valor `'variable'`.
* En la línea 3, se crea una variable llamada `lenguaje`, es de tipo cadena (`str`) y tiene el valor `'python'`.
* En la línea 4 se calcula el valor de repetir la variable `cadena` tres veces y se imprime. El programa imprime `variablevariablevariable`.
* En la línea 5 se calcula el valor de repetir la cadena `'cadena'` tres veces y se imprime. El programa imprime `cadenacadenacadena`. Note que en este caso no estamos haciendo referencia a la variable `cadena` sino a la cadena de caracteres `'cadena'`.
* Al intentar ejecutar la línea 6 se produce un error porque no existe ninguna variable con el nombre `python`.

### Utilizar el valor de una variable a la que no se le ha asignado un valor

Para poder utilizar el valor contenido en una variable, se le debe haber asignado antes un valor. En este contexto, *utilizar* hace referencia a cualquier operación que dependa del valor que tenga una variable. Por ejemplo, en el siguiente programa las dos primeras instrucciones producirían un error mientras que la tercera no tendría ningún problema (suponiendo que antes de ejecutar el programa no exista la variable `v`).

```{code-block} python
---
lineno-start: 1
---
v += 10
n = v * 10
v = 55
```

En el caso de las dos primeras instrucciones, el error que se presentaría sería similar al siguiente:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'v' is not defined
```

### Suponer que una asignación es también una ecuación

En un ejercicio de cálculo o de física es común que se usen ecuaciones para expresar el valor de una variable. Por ejemplo, la siguiente ecuación expresa el valor de la posición $y$ en términos de la posición inicial $y_{0}$, la velocidad inicial $v_{0y}$, la aceleración $a_{y}$ y el tiempo transcurrido: 

$$
y = y_{0} + v_{0y} \cdot t + \frac{1}{2} \cdot a_{y} \cdot t^{2}
$$

La relación que describe la ecuación entre las variables mencionadas vale en todo momento, antes y después de que nosotros hayamos escrito la ecuación. El hecho de que nosotros la escribamos no cambia absolutamente nada.

Por el contrario, cuando nostros escribimos una asignación en Python estamos indicando cuál va a ser el valor que tendrá una variable *después de que se ejecute la instrucción*. Considere el siguiente programa:

```{code-block} python
---
lineno-start: 1
---
x = 27
x = y ** 3
```

Si interpretáramos el programa como si fuera un conjunto de ecuaciones, llegaríamos a la conclusión de que tiene que existir alguna variable `y` con el valor `3` para que `x` pueda valer `27` y también pueda valer `y ** 3`.

Si lo interpretamos como lo que es, un programa escrito en Python, la situación es muy diferente. Después de ejecutar la línea 1, la variable `x` asume el valor `27`. Luego ejecutamos la línea 2 y le asignamos a `x` un valor que dependerá del valor de `y`. Si `y` tenía el valor `5`, entonces el nuevo valor de `x` será 125 y el valor anterior se habrá perdido.


### Intentar hacer una asignación de izquierda a derecha

Las asignaciones en Python se hacen de derecha a izquierda: el valor que se encuentre a la derecha del símbolo `=` se almacenará en la variable que se encuentre a la izquierda del símbolo. Si lo que hay a la izquierda no es una variable, se producirá un error. Si lo que hay a la derecha es una expresión, entonces se hará la evaluación de la expresión antes de almacenar el valor en la variable.


## Errores definiendo funciones

### No respetar la indentación 

Python es estricto con respecto a la indentación y exige consistencia: si en una función las instrucciones se indentan de forma diferente se producirá un error como el siguiente:

```python
IndentationError: unexpected indent
```

### Usar tabs en lugar de espacios

Una forma común (y fácil) de introducir el error de intentación es usar un caracter de tabulación en lugar de espacios. En este caso, Python nos anunciará algo similar a lo siguiente:

```python
TabError: inconsistent use of tabs and spaces in indentation
```

Este error se introduce con facilidad al presionar la tecla **tab** pero no se detecta fácilmente porque para nuestros ojos una tabulación se ve igual que 4 u 8 espacios. Afortunadamente hoy en día muchos editores de código remplazan automáticamente las tabulaciones por 4 espacios, así que este error se presenta cada vez menos frecuentemente.


### Usar en una función una variable definida en otra función

Considere el siguiente programa donde se definen dos funciones:

```{code-block} python
---
lineno-start: 1
emphasize-lines: 6,6
---
def fun1(a: int) -> int:
    doble = a * 2
    return doble

def fun2(b: int) -> int:
    resultado = b + doble
    return resultado       
```

En la línea 6 hay un error porque se está intentando leer el valor de una  variable llamada `doble`. Sin embargo, en el *alcance* de esta definición (es decir el espacio de las variables que se podrían leer) no hay ninguna variable con ese nombre. La única variable con ese nombre que vemos en el programa está definida dentro de la función `fun1` pero debemos recordar que las variables que se definen dentro de una función son locales a esa función. Es decir que sólo existen dentro del contexto de esa función.

Si corremos el programa e invocamos a la función `fun2` nos encontraremos con un error como el siguiente:

```python
NameError: name 'doble' is not defined
```


### Usar en una función una variable definida por fuera de la función

A continuación presentamos algo que técnicamente no es un error pero es generalmente considerado una mala práctica de programación porque es fácil que lleve a errores muy difíciles de encontrar y resolver.

Considere el siguiente programa:

```{code-block} python
---
lineno-start: 1
emphasize-lines: 4, 7, 9
---
externo = 2

def fun1(a: int) -> int:
    valor = a * externo
    return valor
    
print(fun1(5))
externo = 3
print(fun1(5))
```

Teniendo en cuenta todo lo que hemos dicho hasta ahora, el programa debería fallar cuando se invoque a la función `fun1` porque dentro de la definición de la función no existe una variable o un parámetro llamado `externo`. Sin embargo, el programa anterior funciona porque dado que no se encuentra el valor `externo` dentro del alcance de `fun1`, Python pasa al siguiente alcance (al del módulo que contiene la definición de la función). Como en este alcance, sí hay un valor para la variable `externo`, se usa este valor y no se produce el error al invocar a `fun1`.

Ahora bien, el hecho de que esto funcione no quiere decir que sea una buena idea aprovechar esta posibilidad para no tener que usar parámetros en las funciones. Como dijimos en la sección correspondiente, los parámetros de una función indican qué información es necesaria para ejecutar la función y calcular su resultado. En el programa de ejemplo esto es falso, puesto que el valor `externo` es absolutamente necesario para calcular `fun1`.

También dijimos que, si invocamos una función usando los mismos parámetros, es de esperarse que el resultado sea siempre el mismo. En este caso esto tampoco es cierto: el resultado de `fun1` es diferente en las dos invocaciones debido al cambio en el valor de la variable `externo`.

Aunque no son los únicos argumentos posibles, por ahora deberían ser suficientes para mostrar que escribir funciones que dependan de valores definidos por fuera de la función es una mala idea (salvo casos muy especiales).


### Ponerle a una variable el mismo nombre de una función

Es un reflejo común usar el nombre de una función para una variable en la que se almacene el resultado de la función, como en este ejemplo:

```{code-block} python
---
lineno-start: 1
emphasize-lines: 5, 5
---
def sumatoria(a: int, b: int, c: int) -> int:
    return a + b + c
    
sumatoria = sumatoria(1, 2, 3)
sumatoria = sumatoria(4, 5, 6)
```

En este caso, el programa va a funcionar hasta la línea 4 y va a fallar en la línea 5 con un error como el siguiente:

```python
TypeError: 'int' object is not callable
```

Sin embargo, el eror se introdujo realmente en la línea anterior. Analicemos con cuidado lo que ocurre en esta línea:

1. Se hace una invocación a la función `sumatoria` usando los parámetros `1`,  `2` y `3`.
2. El resultado de la invocación (el entero `6`) se almacena en la variable `sumatoria` - que no existía antes de este momento.

En la siguiente línea se intenta hacer una invocación a `sumatoria`, pero Python lo último que vio con ese nombre no era una función sino una variable de tipo `int`, por lo cual genera el error diciendo que no es posible hacer una invocación sobre un entero.


### Redefinir funcions nativas

A menos que haya alguna necesidad muy especial, nunca se deberían redefinir las funciones nativas de Python, tales como float, int, str, min, max y abs, entre otras. Sin embargo, en Python esto es realmente muy fácil de hacer y por lo tanto ocurre con frecuencia cuando se está empezando a programar.

Considere el siguiente ejemplo:

```{code-block} python
---
lineno-start: 1
emphasize-lines: 4, 5
---
def menor(a: int, b: int, c: int) -> int:
    return min(min(a, b), c)
    
min = menor(5,7,3)
verificacion = min(5, 7, 3)
print(min, verificacion)
```

En esta función se define la función `menor` que busca el menor de 3 números aplicando la función `min` entre los dos primeros y luego la función `min` entre el tercero y el menor entre los dos primeros números. En la línea 4 se invoca a la función `menor` usando los valores 5, 7 y 3 y se almacena el resultado en la variable `min`. En la línea 5, se usa la función `min` con 3 parámetros para ver si el resultado es el mismo que con nuestra nueva función `menor`. Al ejecutar la línea 5 se produce el error y no se puede hacer la invoación:

```python
TypeError: 'int' object is not callable
```

Esto ocurre porque en la línea 4 creamos una variable llamada `min` de tipo entero y ahora Python no puede encontrar la función nativa `min`. El error en este caso es sencillo de corregir, pero también es fácil de introducir más adelante.


## Errores con el retorno

### Incluir una instrucción return en una función de tipo None
Si en la signatira de una función se declara que la función es de tipo `None`, no debería haber una instrucción `return` dentro de la función.

### No retornar en una función
Fuera de las funciones que declaren en la signatura que son de tipo `None`, todas las funciones deberían incluir una instrucción `return`. Es recomendable, aunque no obligatorio, que sólo haya una instrucción `return` al final de la función.

### Escribir instrucciones después del retorno
Las instrucciones que se escriban después de la instrucción `return` no se ejecutarán en un programa
escribir instrucciones después del retorno

## Otros errores

### Olvidar el operador de multiplicación

Considere el siguiente programa:

```{code-block} python
---
lineno-start: 1
---
a = m(m+1)/2
b = n*(n+1)/2
```

Probablemente el que escribió la primera línea quería realizar el mismo cálculo que en la línea 2 pero se le olvidó incluir el operador de multiplicación. Eso quiere decir que en la primera línea Python va a intentar invocar a la función `m` pasándole como parámetro el valor de `m+1`. Muy posiblemente esto no va a funcionar.

### Confundir la concatenación de cadenas con la creación de tuplas

Más adelante en este libro estudiaremos un tipo de datos llamado tupla. Por ahora es suficiente decir que las tuplas son el tipo que uno usaría para representar cosas como coordenadas en un plano cartesiano (que tienen varias partes). En el siguiente código, en la primera línea se define una coordenada usando una tupla: note el uso de los paréntesis y de la coma para separar los valores 3 y 5.

```{code-block} python
---
lineno-start: 1
---
coordenada_2D = (3, 5)
nombre_1 = 'Alberto' + ',' + 'García'  # nombre_1 es un str
nombre_2 = 'Alberto' , 'García'        # nombre_2 es una tupla
```

La segunda línea del programa crea una variable de tipo `str` con el valor `"Alberto,García"`. Esto ocurre porque utilizamos el operador `+` entre cadenas de caracteres (concatenación) y concatenamos una cadena que tenía una coma (`","`) entre el nombre y el apellido.

En la tercera línea del programa no utilizamos el operador de concatenación, pero pusimos una coma entre el nombre y el apellido. En muchos lenguajes de programación se marcaría como un error de sintaxis, pero en Python esto corresponde a la creación de una tupla: la diferencia con la línea 1 es que en este caso no se utilizaron los paréntesis, que son opcionales cuando se crea una tupla, y que la nueva tupla tiene dos cadenas por dentro en lugar de dos números.

No se preocupe si no entiende lo que es una tupla en este momento. El punto importante es que no confunda una tupla con una cadena donde las partes estén separadas con comas.


# Para no olvidar

* **Cada línea en programa debería tener una instrucción**. Es más fácil de leer, entender, mantener y corregir un programa que tenga varias instrucciones sencillas, en lugar de uno donde cada línea intenta hacer varias cosas a la vez.

* **Las instrucciones de un mismo bloque se ejecutan una por una**. Un bloque hace referencia a las instrucciones que están contenidas dentro del mismo módulo o de la misma función y que tienen el mismo nivel de indentación. Las instrucciones de un bloque se ejecutan desde la primera línea hasta la última, una por una. No son ecuaciones que tengan que ser ciertas todas a la vez.

* **Definir una función no es invocarla**. A pesar de que se haya definido en la parte de arriba de un módulo, una función no necesariamente se va a ejecutar primero.

* **En la parte izquierda de una asignación siempre va una variable**. No puede haber literales, ni expresiones, ni invocaciones de funciones en la parte izquierda de una asignación.

* **En una asignación, lo primero que se hace es evaluar el valor que está en la parte derecha**. Sólo cuando ya se tiene un valor se asigna en la variable de la izquierda.

* **Es mejor usar nombres de variables explícitos y que sugieran su tipo**. Por ejemplo, para guardar el teléfono de una persona es mejor utilizar una variable que se llame `telefono` a una variable que se llame `numero`. Esta última sería problemática si usáramos una cadena de caracteres, lo cual es muy usual dado que muchos teléfonos tienen otros caracteres además de los dígitos (como en `+57 3394949 ext 2860`).

* **Las funciones se invocan con su nombre y los valores para los parámetros dentro de paréntesis**. Si una función no recibe parámetros, de todas formas es necesario incluir los paréntesis.

* **Los valores de los parámetros no tienen que llamarse igual que las variables que se usan al invocar la función**. Por ejemplo, si tenemos la función con signatura ```{python} def f(a: int, b: float)-> float```, no es necesario que tengamos variables llamadas `a` y `b` para hacer la invocación. En el siguiente programa todas las invocaciones serían correctas:

```{code-block} python
---
lineno-start: 1
---
a = 1
b = 4.5
c = 7
r1 = f(a, b)
r2 = f(c, b)
r3 = f(c, 9.9)
```

* **Es una buena práctica usar comentarios**. Si tiene dudas sobre si debería incluir un comentario en un cierto punto, mejor inclúyalo. Sea breve pero preciso en sus comentarios.

