Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Variables, expresiones y operadores

> El objetivo de esta sección es introducir y discutir los conceptos de *instrucción*, *valor*, *variable*, *asignación*, *expresión* y *operador*.


Para empezar, lea con cuidado el siguiente programa escrito con el lenguaje de programación Python. Aunque breve, ilustra los conceptos más básicos del lenguaje, empezando por el concepto de **instrucción**.

```python
v1 = 5
v2 = 1 + 2
v3 = v1 + v2
v4 = v3 / (4 + 1)
print("v4:", v4)
```

Este programa está compuesto por 5 instrucciones, cada una de las cuales se escribió en una línea aparte. Como veremos, cada una de estas instrucciones le da una orden al computador y esa orden se tiene que terminar de ejecutar antes de que se pueda pasar a la siguiente instrucción. Esto quiere decir que podemos estar seguros de que la última instrucción (```print(v4)```) se va a ejecutar después de que se hayan ejecutado las 4 instrucciones anteriores. ¡Aunque puede parecer simple, este concepto es extremadamente importante!


## Analizando la primera instrucción

Analicemos ahora la primea instrucción del programa:

```python
v1 = 5
```

Esta instrucción se puede dividir en dos partes dividas por el caracter ```=```. En la parte derecha, encontramos sólo el caracter ```5```, el cual expresa el **valor** que corresponde al número natural 5. 

En la parte izquierda encontramos sólo el texto ```v1```. Como sabemos, este texto no puede expresar ninguno de los tipos de datos que ya conocemos (*int*, *float*, *str*) así que ```v1``` no puede ser un valor. En este caso, ```v1```representa entonces el nombre de una **variable** definida por el programador.

Una **variable** es un espacio en la memoria del computador en el cual se puede almacenar un valor o del cual se puede leer un valor, mientras se ejecute el programa. Cuando un programador define una variable, le asigna un nombre o identificador para que sea fácil de recordar y utilizar en el resto del programa. En nuestro ejemplo, la variable tiene el nombre ```v1```.

**Nota:** Se debe procurar que los nombres de las variables sean lo más descriptivos posibles para que su objetivo sea claro. En el ejemplo la variable tiene un nombre que no es muy explícito pero en las siguientes líneas quedará claro por qué se seleccionó el nombre ```v1```. En el programa completo del inicio del capítulo, una de las variables se llamaba ```hipotenusa```: sería difícil encontrar un nombre que expresara con más claridad el objetivo de esa variable.

Finalmente, volvamos al caracter ```=``` que separa la *variable* que se encuentra a la izquierda del *valor* que se encuentra a la derecha. En Python, el caracter ```=``` se utiliza para especificar que en un programa se debe hacer una **asignación**. Es decir, cuando se ejecute una instrucción con una asignación, el programa debe tomar el valor que se encuentra a la **derecha** del caracter y lo debe almacenar en la variable que se encuentra a la **izquierda**.

La instrucción que estamos analizando entonces se encarga de crear una variable con el nombre ```v1``` y almacenar en ella el valor entero ```5```. En Python, el tipo de una variable depende del valor que esté almacenado en ella así que en este caso la variable será de tipo **int** [^tipos].

[^tipos]: Si usted ha trabajado con otros lenguajes de programación, notará que en Python no se deben declarar las variables antes de usarlas, ni se debe indicar explícitamente su tipo. Esto se debe a que Python utiliza *tipado dinámico*, es decir que el intérprete infiere los tipos de variables y parámetros durante la ejecución. Veremos más adelante que, aunque en las versiones actuales no se puede *especificar* los tipos de nada, sí se pueden dar *hints* que sirven como comentarios para que los programadores puedan hacerle un mejor seguimiento a los programas.


**Recuerde:** cuando se hace una asignación, el valor de la derecha se almacenará en la variable de la izquierda. Es un error bastante común entre principiantes escribir instrucciones como ```5 = v1 ```: esta instrucción no sería válida en Python y el intérprete mostraría un error similar al siguiente:

```python
SyntaxError: can't assign to literal
```

## Operadores y expresiones

Si analizamos ahora la segunda línea del programa, veremos que tiene varios de los elementos que acabamos de estudiar:

```python
v2 = 1 + 2
```

A la izquierda tenemos una variable llamada ```v2``` a la cual le vamos a asignar el valor que se encuentra a la derecha. La diferencia es que en este caso el valor no está definido usando un literal sino usando una **expresión**: ```1 + 2```.

En Python, una **expresión** es una combinación de valores, literales, variables, llamados y operadores, que al evaluarse produce un valor. Cuando escribimos una instrucción como la del ejemplo, le estamos indicando a Python que la expresión de la derecha debería evaluarse para producir un valor y que ese valor debería almacenarse en la variable. En nuestro ejemplo, el valor de la expresión de la derecha será ```3```, es decir el resultado de usar el **operador** + a los dos literales **1** y **2**.


## Instrucciones con variables

A continuación analizaremos las siguientes dos instrucciones del programa pero recordando un principio muy importante: para que estas instrucciones se ejecuten, se tienen que haber ejecutado antes las anteriores. Es decir, que cuando estas instrucciones se ejecuten ya se habrá creado la variable ```v1``` y se le habrá asignado el valor ```5``` y ya se habrá creado la variable ```v2``` y se le habrá asignado el valor ```3``` [^1].

[^1]: Cuando se resuelven ejercicios de matemáticas o física aparecen conceptos similares a los que estamos trabajando y es normal que se escriban expresiones muy parecidas (por ejemplo: ```distancia = velocidad * x```). Sin embargo, en esos contextos las expresiones no se escriben necesariamente siempre en un orden estricto, porque es un humano el que las va a interpretar. Además, porque más que asignaciones, se trata de ecuaciones que describen una equivalencia entre valores.


```python
v3 = v1 + v2
```

Esta instrucción es muy similar a la anterior: a la nueva variable ```v3``` se le debe asignar el valor resultado de evaluar la expresión de la derecha. La diferencia principal es que en este caso la expresión no está construída a partir de literales como 1 y 2, sino a partir de nombres de variables. Esto quiere decir que cuando llegue el momento de ejecutar la instrucción, Python tiene que evaluar la expresión de la derecha *antes* de poder hacer la asignación. 

Ahora bien, ¿cómo puede calcular Python la suma de dos cosas que no son literales? La respuesta es que también tiene que evaluar esas dos cosas para averiguar qué valor tienen. Como ```v1``` y ```v2``` son variables, la evaluación es muy sencilla porque sólo requiere consultar cuál es el valor almacenado en esas variables. Eso quiere decir que, después de evaluar el valor de esas variables, Python está listo para hacer la siguiente asignación:

```python
v3 = 5 + 3
```
En este punto volvimos a una situación idéntica a la de la instrucción anterior y ya sabemos que se va a resolver dejando el valor entero ```8``` en la variable ```v3```.

**Nota:** La evaluación de la instrucción anterior fue exitosa porque a las variables ```v1``` y ```v2``` ya se les había asignado un valor anteriormente. Si en lugar de ```v1``` hubiéramos escrito un nombre de variable inexistente, como ```vv```, habríamos encontrado un error como el siguiente:

```python
NameError: name 'vv' is not defined
```

## Paréntesis y tipos de datos

Antes de pasar a la siguiente instrucción, observemos lo que responde Python cuando le preguntamos por los tipos de las variables ```v1```, ```v2``` y ```v3```.

```python
>>> type(v1)
<class 'int'>
>>> type(v2)
<class 'int'>
>>> type(v3)
<class 'int'>
```

No es una sorpresa que ```v1``` sea de tipo int dado que la asignación se hizo con un literal. En el caso de ```v2``` y ```v3``` Python decidió que el tipo debía ser int dado que el valor se calculó a partir de la suma de valores de tipo int.

Pasemos ahora a la siguiente instrucción, en la que nuevamente tenemos una asignación y una expresión con operadores a la derecha.

```python
v4 = v3 / (4 + 1)
```

Lo primero que tenemos que notar es que en este caso se utilizaron paréntesis, los cuales tienen el mismo efecto que tendrían si estuviéramos resolviendo un ejercicio de matemáticas. En este caso los paréntesis son obligatorios porque en Python los operadores matemáticos siguen las reglas de precedencia tradicionales. Es decir que la expresión ```v3 / (4 + 1)``` tiene un valor diferente al de la expresión ```v3 / 4 + 1``` porque el operador de división (```/```) tiene mayor precedencia que el operador de suma (```+```). Debido a esto, lo primero que va a hacer Python cuando empiece a evaluar la expresión de la derecha es encontrar el valor para lo que estaba dentro de los paréntesis y reescribirá la instrucción como:

```python
v4 = v3 / 5
```

Ahora lo que Python tiene que hacer es evaluar la expresión de la derecha, pero para eso primero debe consultar el valor de la variable ```v3```. Después de hacer esto, la instrucción se reescribirá como:

```python
v4 = 8 / 5
```

Finalmente tenemos una instrucción que sólo tiene literales y el operador de división, así que la expresión de la derecha se puede obtener simplemente calculando la división entre 8 y 5, para luego asignárselo a la variable ```v4```.

Ahora bien, el operador de división en Python tiene la propiedad interesante de que su resultado es de tipo **float**. Es decir que independientemente del valor de v3, el valor de la variable ```v4``` va a ser un número decimal. Esto lo podemos comprobar si le preguntamos a Python por el tipo de la variable:

```python
>>> type(v4)
<class 'float'>
```


## Otro tipo de instrucciones

Si revisamos con cuidado las 4 instrucciones que hemos analizado, nos daremos cuenta que lo único la única orden que le hemos dado al programa es que almacene valores dentro de variables. Como vamos a ver a continuación, la última instrucción de nuestro programa es fundamentalmente diferente a las anteriores porque no hace ninguna asignación.

```python
print("v4:", v4)
```

En primer lugar, revisemos qué pasa cuando se ejecuta esta línea. Suponiendo, como siempre, que ya se habían ejecutado las líneas anteriores del programa, al ejecutar esta línea lo que debería ver el usuario en la consola es lo siguiente.

```python
v4: 0.6
```

Lo que hace nuestra instrucción es una invocación a una función básica de Python llamada ```print``` y le pasa dos parámetros ( ```"v4:"``` y ```v4```). Más adelante estudiaremos más a fondo la función ```print``` pero lo que nos interesa saber en este momento es que la función sirve para mostrarle al usuario los valores que hayamos usado como parámetros. Más adelante estudiaremos también cómo definir nuestras propias funciones.

En este caso la invocación a la función se está haciendo con dos parámetros que podemos identificar porque aparecen dentro de paréntesis y están separados por una coma. El primer parámetro (```"v4:"```) es un literal de tipo str (cadena de caracteres). El segundo parámetro (```v4```) es el nombre de la variable a la que se le asignó un valor en la instrucción anterior. Note que como estamos haciendo referencia a una variable, no se utilizan comillas sencillas ni dobles.

Al igual que una asignación necesita calcular el valor de la derecha para que se pueda almacenar el valor en la variable, para hacer una invocación a una función se necesitan los valores de los parámetros. En nuestro caso, el primer parámetro es un literal así que su valor ya es conocido; como el segundo parámetro es una variable, Python buscará el valor que se había almacenado en la variable y lo usará para hacer la invocación.

El último paso en la ejecución de nuestro programa no podemos verlo pero corresponde a la ejecución de las instrucciones que se encuentran dentro de la función ```print```, las cuales hacen que aparezcan los valores de los parámetros en la consola. Como esta es una función nativa del lenguaje, las instrucciones que la implementan son parte del código fuente del intérprete del lenguaje y no son fáciles de encontrar.


## Comentarios en Python

El siguiente programa es exactamente equivalente al que hemos estado estudiando, con la diferencia de que se han incluído *comentarios*.

```python
# Definir 4 variables (v1 hasta v4)
v1 = 5
v2 = 1 + 2
v3 = v1 + v2 # El valor de v3 es de tipo int porque es la suma de dos int
v4 = v3 / (4 + 1)  # El valor de v4 va a ser de tipo float
print("v4:", v4) # Mostrarle al usuario el valor de v4
```

Un comentario en un programa es una anotación que dejó el programador para que otros programadores, o él mismo, puedan entender con más facilidad el objetivo de un programa o de un bloque de código. En el caso de Python, la forma más común de incluir comentarios es utilizando el caracter ```#```: todos los caracteres que se encuentren a la derecha de este caracter serán ignorados por el intérprete.

En el caso de nuestro ejemplo, los comentarios se ha incluido un número relativamente grande de comentarios para un programa tan sencillo. Sin embargo, esto sirve para ilustrar un principio importante: ante la duda, es mejor tener más comentarios que menos comentarios en un programa.
 

## Más operadores en Python

En las secciones anteriores estudiamos sólo los operadores para sumar y dividir. A continuación describimos otras de las operaciones que es posible hacer en Python.

### Operadores para números

Los siguientes son los operadores disponibles para hacer operaciones con números. Es decir que estos operadores pueden aplicarse sólo sobre datos que sean de tipo **int** o **float**.

Operación | Operador | Aridad (1) | Precedencia (2) | Ejemplo | Valor |
----------|----------|--------|-------------|---------|-------|
Exponenciación |  **  | Binario | 1 | 10 ** 3 | 1000 |
Identidad |  +  | Unario | 2 | + 2 | +2 |
Cambio de signo | - | Unario | 2 | -(-2) | +2 |
Multiplicación | * | Binario | 3 | 10 * 3 | 30 |
División (3) | / | Binario | 3 | 10 / 3 | 3.3333 |
División entera (4) | // | Binario | 10 / 3 | 3 |
Módulo (5) | % | Binario | 3 | 10 % 3 | 1 |
Suma | + | Binario | 4 | 10 + 3 | 13 |
Resta | - | Binario | 4 | 10 - 3 | 7 |

(1) El término *aridad* hace referencia a la cantidad de operandos sobre los que se aplica el operador. Los operadores unarios sólo requieren un operador mientras que los binarios necesitan 2.

(2) La precedencia de un operador indica en qué orden se evaluarón varios operadores en caso de que no haya paréntesis que permitan resolver el orden. En Python, el primer operador que se evaluará es el operador de exponenciación. En caso de que la precedencia de dos operadores sea la misma, los operadores se aplicarán de izquierda a derecha. Por ejemplo, en el caso de la expresión ```70 // 2**3 / 4``` primero se evaluará la operación de exponenciación (la de mayor precedencia), luego se evaluará la división entera y finalmente la división.

(3) En Python, la división siempre produce un resultado de tipo float, el cual muchas veces se redondea automáticamente. En el caso del ejemplo, la división ```10/3``` tiene como resultado el número decimal ```3.3333333333333335```, que es la mejor aproximación que puede hacer Python del resultado real de la división. El valor de la expresión ```9/3```, aunque podría ser un número entero (int), es el número decimal (float) ```9.0```.

(4) Para valores positivos, la operación de *división entera* calcula la parte entera del resultado de la división y por ende siempre es un número entero. En el caso de la expresión ```10//3``` el valor es el número entero (int) ```3```. 

Para números negativos, el resultado es el mayor número entero menor o igual al resultado de la división. Es decir que para el valor de la expresión ```-10//3``` es el número entero ```-4```

(5) La operación módulo calcula el **residuo** de la división entera entre dos números. Por ejemplo, el valor de la expresión ```10%3``` es igual a ```1``` porque la división entera entre 10 y 3 tiene como resultado 3 con un residuo de 1 [^modneg].

La operación módulo es muy utilizada para avariguar la paridad de un número: el resultado de la expresión ```x%2``` será 0 sólo cuando ```x``` sea un número par y será 1 cuando ```x``` sea impar.


[^modneg]: Aunque también está definida para números negativos, no es muy recomendable aplicar la operación módulo sobre estos números debido a que no todos los lenguajes utilizan la misma definición. Esto podría dar lugar a errores graves y difíciles de detectar.


### Operadores para cadenas de caracteres

Python sólo ofrece dos operadores que se pueden aplicar sobre cadenas de caracteres.

Operación | Operador | Aridad (1) | Precedencia (2) | Ejemplo | Valor |
----------|----------|--------|-------------|---------|-------|
Concatenación |  +  | Binario | 1 | 'abc' + 'def' | 'abcdef' |
Repetición |  *  | Binario | 1 | 'ab' * 3 | 'ababab' |

El operador de concatenación se utiliza para unir dos cadenas de caracteres y convertirlas en una sola.

El operador de repetición se aplica sobre dos operandos de diferente tipo: una cadena de caracteres y un entero. El resultado será una cadena de caracteres que será el resultado de repetir la cadena tantas veces como indique el número.


### Expresiones con múltiples tipos de datos

En Python no es posible escribir expresiones que combinen valores de diferentes tipos a menos que se hagan conversiones explícitamente. Por ejemplo, para construir una cadena que combine caracteres y números se debe hacer una conversión como en el siguiente ejemplo:

```'El salón asignado es el ' + str(614) + ' del edificio ML'```

Por otro lado, para hacer operaciones numéricas con valores almacenados en una cadena se debe convertir esa cadena a un número como en el siguiente ejemplo:

```1 + float('2.3') + 3```

Finalmente, si se quieren hacer combinaciones de tipos se deben utilizar paréntesis que eliminen los posibles problemas.

```'El resultado es ' + str(2**3)```

En este siguiente ejemplo lo primero que se hace es evaluar la operación de exponenciación, luego se convierte el resultado a una cadena y finalmente se concatenan las dos cadenas.

## Ejercicios

1. ¿Cuáles de las siguientes líneas no son instrucciones válidas en Python? (suponga que las instrucciones se van ejecutando una después de la otra)

 * variable = 5
 * 5 = variable
 * var1 = var2 + 5
 * var1 = var1 + 5
 * var = var + 5

2. ¿Qué resultados se obtendan al evaluar las siguientes expresiones en Python? Verifique los resultados evaluando las expresiones en el intérprete de Python.

 * 2 + 3 + 1 + 2
 * 2 + 3 * 1 + 2
 * (2 + 3) * 1 + 2
 * (2 + 3) * (1 + 2)
 * +---6
 * -+-+6
 * -3 / 2 - 1
 * -3 // 2 - 1
 * 3 % 2 - 1


3. ¿Qué valor se mostrará en la pantalla después de ejecutar el siguiente código?

	```python
	z = 1
	z += 2
	z *= 2
	z //= 2
	z -= 2
	z %= 2
	z ** 2
	z /= 2
	print(z)
	```


4. ¿Qué resultado se obtendrá al evaluar la siguiente expresión en Python?

	```python
	'a' * 3 + '/*' * 5 + 2 * 'abc' + '+'
	```


5. ¿Qué resultado se obtendrá al evaluar las siguientes expresiones en Python?

	```python
	25 / 3 // 2
	25 / (3 // 2)
	(25 / 3) // 2
	25 // 3 / 2
	25 // (3 / 2)
	(25 // 3) / 2
	```



## Más allá de Python

Esta sección presentó en detalle los detalles más importantes de la sintaxis de Python. Sin embargo, los conceptos presentados son comunes a la mayoría de lenguajes de programación *imperativos* [^para]. Aunque puede parecer que las diferencias entre Python y otros lenguajes son muy grandes, en realidad los conceptos que se manejan son básicamente los mismos: todos los lenguajes tienen literales, tienen variables para almacenar temporalmente valores, tienen expresiones que se tienen que evaluar, y tienen mecanismos para invocar fragmentos de código definidos en algún otro lugar.

Si tenemos perfectamente claro todo lo expuesto en este capítulo, aplicar las mismas ideas a otros lenguajes debería ser muy sencillo.
 

[^para]: Python, C, C++ y Java son algunos ejemplos muy populares de lenguajes de programación **imperativos**. En estos lenguajes las instrucciones de un programa sirven para darle órdenes al computador (por ejemplo, sume estos dos números, guarde el resultado en esta posición de memoria). Hay otros lenguajes de programación que siguen *paradigmas* diferentes, como el paradigma **lógico** o el **funcional**. En esos lenguajes las instrucciones de un programa no son órdenes sino expresiones lógicas que el computador debe resolver, o definiciones de funciones que el computador debe evaluar, por ejemplo. Después de adquirir una cierta destreza con algún lenguaje de programación particular es muy recomendable estudiar algún lenguaje basado en un paradigma diferente: está demostrado que aprender a resolver los mismos problemas utilizando herramientas y métodos completamente diferentes es parte de lo que hace a un experto.


