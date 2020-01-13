 Versión borrador / preliminar |
------------------- |
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores |


# Valores de verdad en Python

> El objetivo de esta sección es mostrar cómo se representan y operan valores de verdad dentro de un lenguaje de programación. Los conceptos que se estudian en esta sección son aplicables directamente a la mayoría de lenguajes de programación.

En la sección pasada trabajamos con valores de verdad y con proposiciones. En esta sección veremos que Python tiene un tipo de datos específico para este tipo de valores (bool) y que permite también la construcción de expresiones lógicas usando conjunciones, disyunciones y negaciones. También aprenderemos a escribir expresiones lógicas usando operadores relacionales sobre valores de todos los tipos que conocemos hasta el momento (números, cadenas y valores de verdad). En la próxima sección usaremos todos estos conceptos para construir expresiones condicionales.


## El tipo bool en Python

En el nivel 1 nos encontramos ya con los tipos que Python utiliza para manejar valores numéricos (```int``` y ```float```) y cadenas de caracteres (```str```). Ahora vamos a introducir el tipo ```bool```, que se utiliza para representar valores de verdad y puede utilizarse en variables, parámetros, llamados de funciones y otras expresiones.

En comparación con los tipos que ya conocíamos, ```bool``` es mucho más sencillo puesto que sólo hay dos literales: ```True```, que se utiliza para expresar un valor verdadero, y ```False```, que se usa para expresar un valor falso. Ponga atención al uso de minúsculas y mayúsculas, puesto que los dos literales se deben escribir exactamente así. 

También note que no es lo mismo ```'True'``` que ```True```. El primer valor es una cadena de caracteres, mientras que el segundo es un valor de verdad:

```python
>>> type('True')
<class 'str'>
>>> type(True)
<class 'bool'>
```

### Conversiones

Al igual que con los otros tipos, existe la función ```bool``` que permite convertir de otros tipos a booleano. Sin embargo, no es muy recomendable utilizar esta función puesto que su uso muchas veces lleva a resultados inesperados.

Por ejemplo, las siguientes expresiones tienen valor equivalente a ```True```:

* ```bool('True')```
* ```bool('true')```
* ```bool('cadena')```
* ```bool(5)```
* ```bool(-5)```

También tienen valor equivalente a ```True``` las siguientes expresiones, aunque naturalmente se podría esperar lo contario:

* ```bool('False')```
* ```bool('false')```
* ```bool(' ')```

Por otro lado, las siguientes expresiones tienen todas valor equivalente a ```False```:

* ```bool(0)```
* ```bool(-0)```
* ```bool('')```

Como dijimos antes, es mejor limitarse a usar los literales ```True``` y ```False``` que aprenderse todas las reglas que explican estas conversiones. Todo lo que puede hacerse usando esas conversiones puede hacerse también sin tener que recurrir a ellas [^conv].

[^conv]: Acá hemos incluido sólo algunos ejemplos de las conversiones que se pueden hacer. Hizo falta incluir ejemplos basados en números complejos, valores nulos (None), listas, diccionarios, conjuntos y en general todos los tipos de secuencias y colecciones.

### Funciones que retornan valores de verdad

El tipo ```bool``` también puede usarse para expresar el tipo de retorno de una función. Por ejemplo, las siguientes son dos funciones que retornan un valor de tipo bool: siempre que la primera función sea invocada, el resultado será un valor verdadero, mientras que para la segunda función el valor siempre será falso.

```python
def f(x: int)->bool:
    print('f:', x)
    return True

def g(x: int)->bool:
    print('g:', x)
    return False
```

Estas dos funciones no parecen muy interesantes porque siempre retornan el mismo valor, pero más adelante en este capítulo las utilizaremos para una importante demostración.


## Operadores Booleanos

A continuación, estudiaremos los operadores que Python ofrece para realizar las operaciones Booleanas de conjunción, disyunción y negación. 

Algo importante que se debe tener en cuenta es que, aunque las operaciones son conmutativas, el orden en que se escriban los operandos tiene un efecto sobre la forma en la que se evalúan las expresiones. Para cada operador explicaremos esto más en detalle.

### Conjunción (and)

La operación lógica de conjunción se expresa en Python usando la palabra reservada ```and```. Cuando se tiene en un programa Python una expresión de la forma ```p and q``` se sabe entonces que tendrá un valor verdadero sólo si la expresión ```p``` y la expresión ```q``` tienen simultáneamente un valor verdadero. Además, el operador ```and``` es asociativo, así que se pueden escribir expresiones como ```w and x and y and z``` sin tener que usar paréntesis y sin riesgos de que cambie el resultado.

Ahora bien, hay una pequeña pero muy significativa diferencia entre el operador ```and``` y la operación lógica de conjunción. Para estudiarla, tomemos como ejemplo la expresión  ```w and x and y and z```. Si se tratara de una expresión lógica, la podríamos haber escrito en cualquier orden y el resultado sería siempre el mismo debido a la conmutatividad de la conjunción. Es decir que para nosotros sería exactamente lo mismo escribir ```z and x and w and y```.

En el caso de la expresión Python entran a jugar también consideraciones prácticas. Por ejemplo, suponga que ```x``` es un valor de verdad extremadamente difícil de calcular [^lento] y suponga también que sabemos que ```w``` es una expresión falsa. No tendría sentido buscar el valor de ```x``` puesto que sabríamos de antemano que la expresión completa sería falsa.

La diferencia entonces entre el operador ```and``` de Python y la operación de conjunción es que Python se aprovecha de las propiedades de identidad y dominancia de la conjunción ( *p&and;Verdadero=p* y *p&or;Falso=Falso) para evitar calcular más términos de los necesarios.

Esto quiere decir que cuando se tiene una operación de conjunción primero se evalúa sólo el primer término: si su valor es falso, se sabe que toda la expresión será falsa y no tiene sentido seguir avanzando. Pero si el valor del término es verdadero, entonces se puede concluir que el valor de la expresión será igual al valor de la parte restante de la expresión.

Apliquemos esto a nuestro ejemplo ```w and x and y and z```:

* Python primero revisará el valor de ```w```. Si es falso, Python inmediatamente dirá que la expresión completa es falsa. De lo contrario, el valor de la expresión completa será el valor de la expresión ```x and y and z```.

* Si no hemos terminado, Python revisará el valor de ```x```. Si es falso, Python inmediatamente dirá que la expresión completa es falsa. De lo contrario, el valor de la expresión completa será el valor de la expresión ```y and z```.

* Si no hemos terminado, Python revisará el valor de ```y```. Si es falso, Python inmediatamente dirá que la expresión completa es falsa. De lo contrario, el valor de la expresión completa será el valor de la expresión ```z```.

* Si no hemos terminado, Python revisará el valor de ```z``` y como no hay más operaciones le asignará a la expresión el valor de ```z```.


Veamos ahora esto mismo con un ejemplo un poco más elaborado en el que vamos a tener nuestras dos funciones que siempre retornan el mismo valor: la función ```f``` siempre retornará el valor ```True``` mientras que la función ```g``` siempre retornará el valor ```False```. Además, cada función dejará una traza en la consola para que podamos ver en qué orden fueron llamadas.

```python
def f(x: int)->bool:
    print('f:', x)
    return True

def g(x: int)->bool:
    print('g:', x)
    return False

print("Caso 1 - f and f and f :")
print(f(1) and f(2) and f(3))

print("Caso 2 - f and f and g :")
print(f(1) and f(2) and g(3))

print("Caso 3 - f and g and g :")
print(f(1) and g(2) and g(3))

print("Caso 4 - g and g and g :")
print(g(1) and g(2) and g(3))
```

Las instrucciones que se encuentran al final del programa se encargarán de evaluar una expresión basada en invocaciones a ```f``` y ```g``` e imprimirán el resultado. Veamos ahora el resultado de ejecutar el programa:

```
Caso 1 - f and f and f :
f: 1
f: 2
f: 3
True
Caso 2 - f and f and g :
f: 1
f: 2
g: 3
False
Caso 3 - f and g and g :
f: 1
g: 2
False
Caso 4 - g and g and g :
g: 1
False
```
Lo que vemos en el caso 1 es que la función ```f``` se invoca tres veces y deja traza de las tres invocaciones (podemos ver que se llamó a la función ```f``` y el valor que se le asignó al parámetro ```x```). También vemos que el resultado que se imprime es ```True``` y corresponde al valor de la operación de conjunción.

En el caso 2 lo que vemos es que se invocó dos veces la función ```f``` y luego se invocó la función ```g```. El resultado de esta expresión es ```False```.

El tercer caso es mucho más interesante: podemos ver que la función ```f``` se invocó una vez, pero la función ```g``` sólo se invocó una vez en lugar de dos veces. Esto se debe a que, una vez se encontró el valor ```False``` que retornó la función ```g```, ya se conocía el valor de la expresión completa y no tenía sentido continuar evaluando los otros términos.

En el cuarto caso nos encontramos el mismo comportamiento: sólo se evaluó el primer término y, como tenía valor falso, hizo que toda la expresión fuera falsa sin tener que evaluar el resto de los términos.

### Disyunción (or)

La operación lógica de disyunción se expresa en Python usando la palabra reservada ```or```. Cuando se tiene en un programa Python una expresión de la forma ```p or q``` se sabe entonces que tendrá un valor falso sólo si la expresión ```p``` y la expresión ```q``` tienen simultáneamente un valor falso. Además, el operador ```or``` es asociativo, así que se pueden escribir expresiones como ```w or x or y or z``` sin tener que usar paréntesis y sin riesgos de que cambie el resultado.

Al igual que con la operación ```and```, Python también busca eficiencias en la evaluación de expresiones que usen en este operador. Esto se logra identificando inmediatamente que el resultado de una operación ```or``` entre el valor verdadero y cualquier valor, siempre será verdadero. Es decir que, si el primer operando de una operación que use el operador ```or``` es verdadero, entonces el valor de la operación será verdadero y no será necesario evaluar los otros términos.

Veamos esto agregándole unas instrucciones adicionales a nuestro programa anterior:


```python
print("Caso 1 - f or f or f :")
print(f(1) or f(2) or f(3))

print("Caso 2 - f or f or g :")
print(f(1) or f(2) or g(3))

print("Caso 3 - g or f or g :")
print(g(1) or f(2) or g(3))

print("Caso 4 - g or g or g :")
print(g(1) or g(2) or g(3))
```

Ahora se evaluarán expresiones basadas en disyunciones y tendremos un comportamiento muy diferente al del caso anterior:

```
Caso 1 - f or f or f :
f: 1
True
Caso 2 - f or f or g :
f: 1
True
Caso 3 - g or f or g :
g: 1
f: 2
True
Caso 4 - g or g or g :
g: 1
g: 2
g: 3
False
```

En el primer caso, vemos que Python inmediatamente idéntica que el primer término tiene valor verdadero. Esto implica que la expresión completa tendrá valor verdadero y la evaluación termina sin tener que evaluar los otros términos.

En el segundo caso pasa algo exactamente igual: a pesar de que los otros términos tienen valores diferentes, es suficiente con evaluar el primer término para saber cuál será el valor de toda la expresión.

En el tercer caso lo que vemos es que se evalúa el primer término que, como sabemos por la definición de la función, es falso. Python tiene entonces que recurrir al segundo término, que en este caso es verdadero. Esto hace que la expresión completa sea verdadera y no sea necesario seguir con el resto de la evaluación.

Sólo en el cuarto caso se evalúan los tres términos: el primero es falso, obligando a la evaluación del segundo, que también es falso. Finalmente se evalúa el tercer término y, como también es falso se concluye que la expresión completa era falsa.

### Negación (not)

El tercer operador lógico en Python es la negación, la cual se expresa con la palabra reservada ```not```. Como se trata de un operador unario se debe anteponer al operando. Es decir que se usa igual que como se usa el signo ```-``` para convertir a un número en su negativo (por ejemplo, ```5```, ```-5``` y ```-(-5))```).

El operador ```not``` no tiene ninguna diferencia con la operación lógica de negación y tiene una precedencia que es mayor a la de la conjunción y a la de la disyunción. Es decir que ```not a and b``` siempre será equivalente a ```(not a) and b``` y que ```a and not b``` siempre será equivalente a ```a and (not b)```.

Veamos esto en un ejemplo:

```python
print("Caso 1:", not f(1) and f(2))
print(not f(1) and f(2))
print("Caso 2:", not g(1) and f(2))
print(not g(1) and f(2))
```

El resultado de la ejecución de este programa se muestra a continuación:

```
Caso 1: not f(1) and f(2)
f: 1
False
Caso 2: not g(1) and f(2)
g: 1
f: 2
True
```

En el primer caso vemos que se evaluó la función ```f``` y se obtuvo necesariamente el valor ```True```. A continuación, se aplicó el operador de negación y se obtuvo el valor ```False```. En ese punto Python pudo descubrir que la expresión completa iba a tener valor ```False``` y la evaluación terminó con ese resultado.

En el segundo caso vemos que, por el contrario, el primer término de la conjunción tiene valor ```True``` porque primero se evaluó ```g``` y luego se aplicó la negación. Después de esto se hizo la evaluación del segundo término y se llegó al valor final: ```True```.

Note que en ambos casos la evaluación de la operación de negación se hizo **antes** de la evaluación de la operación de conjunción.


[^lento]: Más adelante en este libro veremos muchos ejemplos de funciones y valores que toman tiempos largos para ser calculados.

[^ sobre]: En realidad, en Python se pueden usar otros literales para expresar valores verdaderos y falsos, pero en general es mucho más claro cuando se usan los literales True y False. Por ejemplo, las siguientes dos expresiones tienen valores que podríamos llamar *desconcertantes*: 1. ```not -66 and 'a'``` 2. ```not -66 and 'a'```. La primera expresión tiene valor ```False```, mientras que la segunda tiene valor ```'a'```. Aunque esos resultados no son un error y están perfectamente justificados en la especificación de Python, debería ser mucho más fácil deducir el valor de una expresión sin tener que conocer detalles de implementación relativamente oscuros.


#### Ejercicios

1. ¿Cuál es el valor de las siguientes expresiones Python basadas en conjunciones? ¿Cuáles de las reglas y propiedades que se estudiaron en la sección anterior se aplican en cada caso?

  * ```False and p```
  * ```True and p```
  * ```p and True```
  * ```p and False```
  * ```p and q and r```

2. ¿Cuál es el valor de las siguientes expresiones Python basadas en disyunciones? ¿Cuáles de las reglas y propiedades que se estudiaron en la sección anterior se aplican en cada caso?

  * ```False or p```
  * ```True or p```
  * ```p or True```
  * ```p or False```
  * ```p or q or r```

3. ¿Cuál es el valor de las siguientes expresiones Python basadas en negaciones? 

  * ```not True```
  * ```not not True```
  * ```not not not False```

4. ¿Cuáles de las reglas y propiedades que se estudiaron en la sección anterior se podrían aplicar en cada una de las siguientes expresiones?

  * ```not p and not q```
  * ```(p and q) or (q and r)```
  * ```p and (q or r)```
  * ```p or (q and r)```



## Operadores relacionales

Hasta este momento todas las operaciones que hemos visto cuyo resultado es un valor de verdad han utilizado otros valores de verdad como operandos. Los operadores relacionales que veremos a continuación nos permitirán hacer comparaciones entre diferentes valores con el fin de obtener un valor de verdad.

La siguiente tabla resume los operadores disponibles en Python para hacer comparaciones entre valores. Estos operadores pueden aplicarse a  cualquier tipo de valor, aunque no necesariamente el resultado tendrá un sentido muy evidente. Por ejemplo, la expresión ```True < False``` es falsa, pero no es fácil imaginarse una razón para comparar dos valores booleanos usando ese operador.

Operador | Significado | Ejemplo | Resultado |
:---------:|:-------------|:---------:|:-----------|
<        | Es menor que ... | 4 < 7 | True
<=       | Es menor o igual que ... | "Ab" <= "ab" | True 
\>       | Es mayor que ... | 4.5 > 7.1 | False 
\>=      | Es mayor o igual que ... | '1A' >= 'A1' | False 
==       | Es igual a ... | "abc" == "ab" + "c" | True 
!=       | Es diferente de ... | 4 != 7 | True 
is       | Dos *objetos* son el mismo | 4 is 7 | False 
is not   | Dos *objetos* no son el mismo  | 4 is not 7 | True 


### Operadores de orden

Los primeros cuatro operadores tienen un comportamiento intuitivo cuando se aplican sobre valores numéricos (```int``` y ```float```). Cuando se aplican sobre cadenas de caracteres, la comparación se hace de forma lexicográfica (como se organizarían las palabras en un diccionario). De esta manera, la cadena ```"hola"``` debería ser *menor* que la cadena ```mundo```. Sin embargo, en este sistema las mayúsculas siempre son *menores* que las minúsculas, así que la expresión ```'Z' < 'a'``` siempre será verdadera. Por su parte, los números son *menores* que las mayúsculas, y algunos símbolos son menores que los números [^lexi]. Si se quiere hacer una comparación más sencilla se pueden convertir las cadenas a letras minúsculas o mayúsculas usando uno de los mecanismos que veremos en una de las siguientes secciones.

Si se intentan usar estos 4 operadores entre valores de tipos diferentes se presentará un error similar al siguiente:

```
TypeError: '<' not supported between instances of 'int' and 'str'
```

Las siguientes funciones nos servirán para ilustrar algunas de las ideas que acabamos de presentar.

```python
def es_positivo(x: int)->bool:
    positivo = x > 0
    return positivo

def es_negativo(x: int)->bool:
    negativo = x < 0
    return negativo
    
def es_cero(x: int)->bool:
    positivo = es_positivo(x)
    negativo = es_negativo(x)
    return not positivo and not negativo
    
def ordenadas(antes: str, despues: str)->bool:
    """ 
    Revisa si dos cadenas en un diccionario están ordenadas lexicográficamente
    Parámetros:
        antes (str): una cadena que está antes que la otra en un diccionario
        despues (str): una cadena que está después que la otra en un diccionario
    Retorno:
        (bool): Indica si las cadenas estaban ordenadas.
                El resultado será verdadero si la cadena 'antes' tiene que ir 
                antes que la cadena 'despues' en orden lexicográfico.
                El resultado será falso de lo contrario.   
    """
    estan_ordenadas = antes < despues
    return estan_ordenadas
```

La primera función revisa si el valor que se pasa en el parámetro `x` es mayor que 0. En caso de que esto sea cierto, en la variable `positivo` debería quedar el valor `True` y este valor sería retornado por la función. En caso contrario (es decir, si ```x <= 0```), la función retorna ```False```.

La segunda función hace algo análogo, pero para ver si el valor que se pasa como parámetro es negativo.

La tercera función combina las dos funciones anteriores para ver si el valor `x` es cero: si el número *no* es positivo y *no* es negativo, entonces tiene que ser el valor `0`.

La cuarta función utiliza las comparaciones lexicográficas para ver si dos palabras extraídas de un diccionario estaban correctamente ordenadas. En la variable `estan_ordenadas` queda el resultado de comparar las palabras lexicográficamente, y este valor posteriormente se retorna.


### Operadores de igualdad

Los siguientes operadores (```==``` y ```!=```) sirven para establecer si dos valores son iguales o no. 

**Atención**: no confunda el operador ```==``` con la instrucción de asignación `=`. En el primer caso el resultado será un valor de verdad mientras que en el segundo caso se modificará el valor de una variable.

En el ejemplo de la tabla se puede apreciar un caso muy interesante: a la derecha del operador ```==``` tenemos la cadena ```"abc"```, mientras que a la derecha tenemos la expresión ```"ab" + "c"```. Por lo que aprendimos en el capítulo anterior, sabemos que  el valor de la parte de la derecha será la concatenación de las dos cadenas, así que será ```abc```. Como las dos cadenas son iguales (tienen los mismos caracteres, en el mismo orden), el valor de la expresión será verdadero.

Por otro lado, el operador ```!=``` sirve para comparar dos valores y saber si son diferentes. Esto es equivalente a utilizar el operador de igualdad y luego negar el resultado.

A continuación, presentamos la definición de 3 funciones que nos servirán para ilustrar el uso de los operadores que acabamos de introducir.

```python
def es_par(x: int)->bool:
    # En la siguiente línea sobran los paréntesis, 
    # pero si incluyeron para hacer más claro el código
    residuo_cero = (x % 2 == 0)
    return residuo_cero

def no_es_7_v1(x: int)->bool:
    # En la siguiente línea sobran los paréntesis, 
    # pero si incluyeron para hacer más claro el código
    x_es_7 = (x == 7)   
    return not x_es_7
    
def no_es_7_v2(x: int)->bool:
    return x != 7    
```

La primera función verifica si un número es par. Para eso, calcula el residuo del número módulo 2 y lo compara con 0: si son iguales, significa que el número era par y la función retorna el valor `True`; si son diferentes, la función retorna el valor `False`.

La siguiente función es muy parecida, aunque en este caso lo que se retorna es la negación de la variable ```x_es_7```. En este caso queríamos mostrar que es posible negar un valor justo antes de retornarlo.

La tercera función hace lo mismo que la segunda (dice si un número NO es 7), pero lo hace en la misma línea en la cual hace el retorno. Si analizamos con detenimiento esta función, veremos que lo primero que se hace es comparar el valor del parámetro ```x``` con el número ```7``` para ver si son diferentes (verdadero si son diferentes, falso si son iguales). El resultado de esta comparación es inmediatamente retornado y la función termina su ejecución.


**Atención**: Tenga mucho cuidado cuando haga comparaciones con números decimales. Mientras que las comparaciones de enteros usualmente no tienen problemas, las comparaciones entre decimales pueden tener inconvenientes por culpa de errores en la precisión de los cálculos en Python [^float]. Por ejemplo, el valor de evaluar la expresión ```0.2 == 1.2 - 1.0``` es, sorprendentemente, ```False```. Para entender por qué, se puede evaluar la parte derecha en el intérprete de Python, obteniendo el valor ```0.19999999999999996``` que, aunque es muy cercano a ```0.2```, no es idéntico. 

Para evitar este problema, la recomendación general es que, cuando se vayan a comparar valores numéricos con decimales se defina una precisión y se revisen los intervalos, como en el siguiente ejemplo:

```python
epsilon = 0.005
iguales = (0.2 > (1.2 - 1.0) - epsilon) and (0.2 < (1.2 - 1.0) + epsilon)
```
En este caso, en lugar de comparar ```0.2``` con el resultado de la resta ```1.2 - 1.0``` estamos mirando que esté dentro del intervalo que va desde 1.2 - 1.0 - epsilon hasta 1.2 - 1.0 + epsilon. El valor de epsilon se puede definir tan grande o tan pequeño como sea conveniente para el problema que se esté resolviendo.


### Operadores de identidad

Finalmente, los operadores ```is``` y ```is not``` sirven para revisar que dos valores no sólo sean iguales, sino que también sean el mismo. Como en este libro no vamos a ocuparnos mucho de objetos, no ahondaremos en la distinción entre ```==``` e ```is```.

Más adelante explicaremos en qué casos tiene sentido utilizar el operador ```is not``` en el contexto de la expresión ```is not None```.


[^lexi]: Para entender bien el orden lexicográfico se debe revisar la tabla ASCII que se discutió en el nivel 1 y entender que lo que el resultado de la comparación es el resultado de comparar los números de cada caracter en la tabla ASCII. De esta forma, el caracter 'k' (#107) va después del 'R' (#82), que va después del ';' (#59), que va después del '4' (#52), que va después del '&' (#38).

[^float]: Este problema no es exclusivo de Python. Casi todos los lenguajes sacrifican precisión en los cálculos para ganar un poco de eficiencia y mejorar el uso de la memoria.


## Ejercicios [^cond]

1. Escriba una función que dada la edad de una persona indique si puede manejar (tiene que tener al menos 16 años)

2. Escriba una función que dada la altura en metros y el peso en kilogramos de un adulto diga si está dentro de los rangos típicamente considerados saludables. Para esto debe usar el Índice de Masa Corporal (BMI), que se calcula como *peso/altura<sup>2</sup>*. Un adulto se considera que tiene sobrepeso cuando su BMI es mayor o igual a 25. Un adulto se considera que está bajo de peso cuando su BMI es menor a 18.5.

3. Escriba una función que dados dos números diga si el primero es divisible por el segundo.

4. Queremos saber si una persona tiene el dinero suficiente para pagar la cuenta en un restaurante dados los siguientes parámetros: la cantidad de dinero que tiene la persona, el valor de la cuenta, si la persona va a dejar propina o no. La propina corresponde al 10% del valor de la cuenta.


[^cond]: Si usted ha programado antes o si ya leyó las siguientes secciones podría pensar que es necesario usar condicionales para resolverlos. La realidad es que todos estos ejercicios pueden resolverse usando sólo lo que se estudió en este capítulo.


## Más allá de Python


Al igual que Python, muchos lenguajes utilizan tipos especiales para representar valores de verdad, pero incluyen también convenciones tales como usar 0 para falso y cualquier otro número para verdadero. Por ejemplo, en PHP existen los literales 'true' y 'false' (escritos sin importar el uso de mayúsculas o minúsculas), pero también tienen un valor falso los números 0, 0.0, -0 y -0.0, las cadenas vacías, la cadena "0", un arreglo sin elementos, y el tipo NULL. Algo similar sucede en C y C++. Por el contrario, en Java los únicos literales para valores booleanos son 'true' y 'false'. Como se dijo en la nota sobre el caso de Python, en general es mucho mejor que el código sea claro y se usen los valores booleanos de forma explícita en lugar de depender de conversiones.

La explicación que se presentó sobre el orden en el que se evalúan los términos de una conjunción o una disyunción en general aplica para todos los lenguajes de programación. C, C++, Java, PHP y JavaScript, entre muchos otros, implementan ideas similares.

La distinción entre *son iguales* y *son el mismo* es sutil y se presta para confusiones en diferentes lenguajes. Por ejemplo, en JavaScript existen los operadores ```==``` y ```===``` para diferenciar entre los todos tipos de comparación, mientras que en Java el operador ```==``` representa uno o el otro dependiendo de qué se esté comparando. Más aún, en Java los objetos de tipo String se manejan de forma diferente dependiendo de en qué momento se les asigne su valor, haciendo que a veces dos cadenas iguales sean también la misma y a veces no lo sean. Entender con absoluta claridad este punto para el lenguaje de programación que esté usando le evitará muchísimos dolores de cabeza.


#### Notas 

