Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Funciones

> El objetivo de esta sección es introducir y discutir los conceptos de *función* y *parámetro*, e ilustrarlos con las funciones básicas más importantes del lenguaje.


En esta sección estudiaremos el concepto de **función**, que en Python es el principal mecanismo para estructurar un programa: en lugar de escribir todas las instrucciones de un programa una después de la otra en un mismo archivo, usando funciones es posible organizar las instrucciones en bloques de código que tengan un objetivo preciso y que puedan ser reutilizados.

Por ahora introduciremos los conceptos principales y los ilustraremos usando funciones que son parte de Python. La siguiente sección mostrará como definir nuevas funciones.


## El concepto de función

En términos matemáticos, una función es una relación entre valores de tal forma que para cada combinación de los valores *de entrada* haya sólo un valor *de salida*. Además, las funciones se suelen describir usando una fórmula, de tal forma que dados unos valores de entrada sea sencillo calcular el valor de salida.

A manera de ejemplo, consideremos la siguiente definición de una función:

<math display="block">
    <mi>f(x, y)</mi>
    <mo>=</mo>
    <msup><mi>x</mi> <mi>y</mi> </msup>
</math>

Esta definición expresa que existe una función llamada *f* y cuyo valor depende de dos parámetros llamados *x* y *y*: cuando se evalua la función, asignándole valores específicos a *x* y a *y*, el valor de *f* será igual al valor de calcular *x elevado a la y*. Por ejemplo, si evaluamos la función con los valores *x=2* y *y=3* el resultado será el número *8*. También sabemos que si el valor de *y* es 0, entonces el valor de evaluar la función siempre será *1* independiemente del valor de *x*. Finalmente es importante notar que el resultado de evaluar *f(x,y)* será siempre el mismo para cada combinación de valores de *x* y *y*: no es posible que *f(2,3)* algunas veces tenga el valor *8* y en otras ocasiones tenga un valor diferente.

Una función tiene entonces un nombre, que en el ejemplo anterior era *f*, y un conjunto de parámetros[^param] a los que se les daben dar valores cuando se quiera evaluar la función. En lo posible, los nombres de las funciones y sus parámetros deberían ayudar a aclarar el objetivo de una función. Por ejemplo, la función anterior podría reescribirse de la siguiente manera y sería mucho más legible:

 <math display="block">
    <mi>potencia(base, exponente)</mi>
    <mo>=</mo>
    <msup><mi>base</mi> <mi>exponente</mi> </msup>
</math>

[^param]: Usamos acá el término *parámetro* para evitar confusiones que podrían aparecer si usaramos el término *variable*.



## Funciones en Python

El concepto matemático de función presentado en la sección anterior fue adoptado por Python, pero con unas pequeñas modificaciones que explicaremos en la siguiente sección. Por ahora, lo importante es que en Python es posible definir funciones dándoles un nombre, especificando sus parámetros, y explicando cómo se debe calcular un valor específico a partir de los parámetros. Como veremos en esta sección, Python cuenta con un gran número de funciones pre-definidas que podemos utilizar en nuestros programas. En la próxima sección estudiaremos cómo podemos hacer para definir nuestras propias funciones.

La acción más interesante que podemos hacer sobre una función es *invocarla*. Esto es lo mismo que *evaluarla* para poder saber cuál es sería su valor dados valores específicos para sus parámetros. Por ejemplo, en el siguiente fragmento de código vamos a invocar la función pre-definida llamada ```pow``` pasándole los valores 2 y 3 como *argumentos*.

```python
>>> pow(2, 3)
8
```
El fragmento nos muestra que el resultado de evaluar la función es el entero 8. 
El siguiente fragmento es similar al anterior, pero en este caso se inicia con una asignación: a la variable ```var``` se quiere dejar el valor de la expresión de la derecha. Como ya vimos, esto require que se *evalue* la parte derecha y, como en este caso tenemos una función, requiere la evaluación de la función con los parámetros dados. Al finalizar esta evaluación, en la variable ```var``` quedará el valor 8.

```python
>>> var = pow(2, 3)
>>> var
8
```

Finalmente, el siguiente fragmento muestra dos ideas muy importantes sobre el uso y la evaluación de funciones. La primera, es que en Python es posible hacer composición de funciones: estamos llamando la función ```pow``` usando como segundo argumento el resultado de evaluar esa función usando los valores 2 y 2. 

```python
>>> var = pow(2, pow(2,1+1) )
>>> var
16
```
La segunda idea es que en Python se deben conocer los valores de los parámetros de una función *antes* de que se pueda evaluar la función. Esto significa que el intérprete Python realizará las siguientes acciones para ejecutar la primera instrucción del fragmento:

1. Evaluar la expresión `1+1`. El resultado (2) se almacena temporalmente para usarse en el siguiente paso.
2. Evaluar la función ```pow``` con los argumentos 2 y 2. El resultado (4) se almacena temporalmente para usarse en el siguiente paso.
3. Evaluar la función ```pow``` con los argumentos 2 y 4. El resultado (16) se almacena temporalmente para usarse en el siguiente paso.
4. Asignar el valor 16 a la variable ```var```.


Una anotación muy importante para hacer en este punto es que el orden de los parámetros es extremadamente importante y se debe respetar. Así como en el ejemplo *matemático* el valor de *f(2,3)* es diferente al valor de *f(3,2)*, en Python también pasa lo mismo. Por eso es absolutamente fundamental saber en qué orden fueron definidos los parámetros cuando se creó la función.

Si no se tiene acceso al código fuente, un mecanismo para consultar cuáles son los parámetros de una función es usar la función ```help```. Esta es otra función básica de Python y permite consultar la documentación de cualquier otra función. Por ejemplo, en el siguiente fragmento se usará la función ```help``` para consultar la documentación de la función ```pow```.

```
>>> help(pow)
pow(x, y, z=None, /)
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.
```


### Funciones de conversión

En esta y las siguientes subsecciones describiremos varias funciones que son parte del lenguaje mismo y que sirven para resolver problemas que aparecen recurrentemente. Es una muy recomendable conocer estas funciones para poderlas utilizar cada vez que sea necesario, en lugar de estar repitiendo una y otra vez código que ya los responsables del lenguaje hicieron por nosotros.

La documentación completa y oficial de estas funciones se puede consultar en el siguiente link: <https://docs.python.org/3/library/functions.html>. Le recomendamos su consulta especialmente para que se familiarice con la estructura y el lenguaje de la documentación de Python.

Empezaremos discutiremos las 3 funciones para convertir entre tipos de datos que se presentaron brevemente en una sección anterior.

#### int(x)

La función[^funcion] ```int(x)``` convierte un valor ```x``` en un valor de tipo entero. La función ```int``` intenta ser tan versátil como sea posible y no requiere que ```x``` sea de un sólo tipo específico. Por eso es posible llamar a la función utilizando valores de tipo ```float``` o ```str```, entre otros, y se puede suponer que la función aplicará la conversión adecuada para cada caso[^base].

* Si el parámetro ```x``` es de tipo ```float```, el resultado de aplicarle la función  ```int``` es la *parte entera* del valor. Es decir que el resultado de evaluar la expresión ```int(3.4)``` es ```3```, mientras que el resultado de evaluar la expresión ```int(-3.4)``` es ```-3```. La función ```int``` *no hace* una aproximación matemática, sino que *trunca* los decimales.

* Si el parámetro ```x``` es de tipo ```str```, el resultado de aplicarle la función  ```int``` es el valor entero representado en la cadena de caracteres. Por ejemplo, si se evalua la expresión ```int('-3')``` el valor resultante será  el entero ```-3```. En algunos casos, la función intentará hacer la conversión ajustando la cadena (por ejemplo si se evalúa la expresión ```int('  -3 ')``` que tiene espacios adicionales), pero fallará si la cadena no representa un número entero. Por ejemplo, los siguientes casos producirán un error:
  *  int('3.2')
  *  int(' - 3')
  *  int('3+2')

  El error que se mostrará Python en estos casos será similar al siguiente:
  
  ```  
  ValueError: invalid literal for int() with base 10: ' 3.2'
  ```
  
* Finalmente, si el parámetro ```x``` es de tipo ```int``` el resultado de aplicarle la función ```int``` es el mismo valor de ```x```.


[^funcion]: En realidad ```int```, ```float``` y ```str``` son más que simples funciones. Sin embargo, para poder explicar todos sus detalles tendríamos que discutir antes lo que significa programación orientada a objetos y los conceptos de clase y constructor (que no se estudiarán en este libro). Para efectos prácticos, podemos suponer que se trata de 3 funciones y podemos utilizarlas como tal sin ningún problema.

[^base]: La función ```int``` también puede invocarse con un parámetro nombrado llamado ```base``` que tiene por defecto el valor ```10```. Este parámetro adicional sirve para indicar la base en la que está expresado el número, de tal forma que podamos hacer con facilidad conversiones de números. Más adelante estudiaremos los conceptos de parámetros nombrados y de parámetros con valor por defecto.

#### float(x)

La función[^funcion] ```float(x)``` convierte un valor ```x``` en un valor de tipo decimal. Esta función se puede llamar utilizando valores de tipo ```int``` o ```str```, entre otros, y se puede suponer que la función aplicará la conversión adecuada para cada caso.

* Si el parámetro ```x``` es de tipo ```int```, el resultado de aplicarle la función  ```float``` es el mismo número, pero representado como un número decimal. Es decir que el resultado de evaluar la expresión ```float(3)``` es ```3.0```, y que el resultado de evaluar la expresión ```float(-3)``` es ```-3.0```.

* Si el parámetro ```x``` es de tipo ```str```, el resultado de aplicarle la función  ```float``` es el valor decimal representado en la cadena de caracteres. Por ejemplo, si se evalua la expresión ```float('-3.33')``` el valor resultante será  el número ```-3.33```. En algunos casos, la función intentará hacer la conversión ajustando la cadena (por ejemplo si se evalúa la expresión ```float('  -4 ')``` que tiene espacios adicionales y representa un entero), pero fallará si la cadena no representa un número. Por ejemplo, los siguientes casos producirán un error:
  *  float('a')
  *  float('3+2')

  El error que se mostrará Python en estos casos será similar al siguiente:
  
  ```  
  ValueError: could not convert string to float: '3+2'
  ```  

* Finalmente, si el parámetro ```x``` es de tipo ```float``` el resultado de aplicarle la función ```float``` es el mismo valor de ```x```.


#### str(x)

La función ```str``` es una función tremendamente versátil que permite convertir un valor de cualquier tipo a una cadena de caracteres. Los siguientes son algunos ejemplos de invocaciones a la función ```str``` que se podrían hacer junto con el valor que calcularía la función.

* ```str(1)```, valor ```'1'```
* ```str(-1.1)```, valor ```'-1.1'```
* ```str(3.14)```, valor ```'3.14'```
* ```str(1+2+0.14)```, valor ```'3.14'```


### Funciones numéricas

Las 3 funciones anteriores sirven para hacer conversiones entre tipos de datos. A continuación vamos a presentar unas funciones orientadas al trabajo con números.


#### abs(x)

La función ```abs(x)``` sirve para calcular el valor absoluto de un número. Esto quiere decir que si ```x``` es un número positivo, el resultado será el mismo ```x```. En cambio, si ```x``` es un número negativo, el resultado será ```-x```.

Si la función ```abs``` se invoca sobre algo que no sea un número, se producirá un error similar al siguiente:

```
TypeError: bad operand type for abs(): 'str'
```

#### round(n, digits)

La función ```round(n, digits)``` sirve para redondear un número para que sólo tenga la cantidad de decimales que nosotros le indiquemos. En este caso, el parámetro ```n``` hace referencia al número que queremos redondear, mientras que el parámetro ```digits``` especifica cuántos dígitos decimales queremos que tenga el resultado. 

Los siguientes son algunos ejemplos del resultado de evaluar la función:

```python
>>> round(3.14159, 0)
3.0
>>> round(3.14159, 1)
3.1
>>> round(3.14159, 2)
3.14
>>> round(3.14159, 3)
3.142
>>> round(3.14159, 4)
3.1416
>>> round(3.14159, 5)
3.14159
>>> round(3.14159, 6)
3.14159
```

Es importante notar que, a diferencia de la función ```int```, esta función sí hace una aproximación. Esto puede apreciarse en el siguiente ejemplo:

```python
>>> int(2.7)
2
>>> round(2.7, 0)
3.0
```

#### min, max

Las funciones ```min``` y ```max``` sirven para encontrar los valores mínimos y máximos de sus parámetros. El siguiente fragmento ilustra cuál sería el resultado de invocar estas funciones sobre 4 valores numéricos:

```python
>>> min(3,2,6,7,5)
2
>>> max(3,2,6,7,5)
7
```

#### pow(x, y)

La función ```pow``` se utiliza para calcular una potencia de un número. Es decir que ```pow(x, y)``` es equivalente a ```x ** y```.

```python
>>> pow(2,2)
4
>>> pow(2,3)
8
>>> pow(2,4)
16
```



### Funciones de entrada y salida

A continuación describiremos dos funciones que son tremendamente útiles para muchos programas y que son centrales para la interacción con el usuario. La primera función (print) servirá para mostrarle información a los usuarios, mientras que la segunda función (input) servirá para obtener información introducida por los usuarios del programa.

#### print

La función ```print``` ya la habíamos encontrado en secciones anteriores. Su objetivo es sencillamente imprimir información en la terminal o consola. Cuando se invoca la función, ella se encarga de imprimir el valor de cada uno de los parámetros separándolos con un espacio [^print]. 

A continuación se muestra un ejemplo que además ilustra el hecho de que la cantidad de parámetros no es fija.

```python
>>> print("Hola", "Mundo", "!")
Hola Mundo !
>>> print("Hola", "mundo", "!")
Hola mundo !
>>> print("Números", 123)
Números 123
>>> print("Números", 123, 456.0, "...")
Números 123 456.0 ...
```

Un detalle importante de esta función es que permite combinar parámetros de diferentes tipos y todos los imprime. Para lograr esto, la función llama dentro de ella a la función ```str``` para cada uno de los parámetros.

[^print]: Más adelante estudiaremos usos más avanzados de la función que permiten, por ejemplo, separar los elementos usando un caracter diferente.


#### input

La función ```input``` tiene como objetivo permitirle al usuario ingresar información para que el programa la utilice. Para esto la función primero le muestra al usuario un mensaje solicitándole la información y luego se queda esperando a que el usuario ingrese la información solicitada y presione la tecla *return*. Lo que haya tecleado el usuario se convierte en el valor de la invocación a la función.

El siguiente ejemplo ilustra el uso de la función:

```python
>>> valor = input("Por favor ingrese el valor: ")
Por favor ingrese el valor: 345
>>> type(valor)
<class 'str'>
>>> valor
'345'
>>> numero = int(valor)
>>> numero
345
```

En la primera línea, vemos que la función se llamó usando un parámetro que le solicita al usuario que ingrese un valor. En esta línea también vemos que se está asignando a la variable llamada ```valor``` el resultado de evaluar la función ```input```. Como ya se dijo, el valor de una invocación a esta función es igual al valor que ingrese el usuario.

En la segunda línea vemos que el programa imprimió el mensaje y vemos también el valor que tecleó el usuario (```345``` en este caso). El valor que el usuario tecleó queda almacenado en la variable ```valor```. El valor almacenado **siempre** será una cadena de caracteres, como se ven en la siguiente línea cuando se revisa el tipo usando la función ```type```. El valor de la variable es entonces la cadena ```'345'``` y por eso se debe hacer la conversión siguiente para poder usar el valor como un número.



### Funciones sobre caracteres

A continuación vamos a describir dos funciones que aunque no son utilizadas muy frecuentemente, resuelven problemáticas muy específicas e importantes.

#### Sistemas ASCII y UNICODE

Como el objetivo de esta sección no es hacer una descripción completa y pormenorizada de los sistemas ASCII y UNICODE, de su historia y de su uso para representar caracteres, vamos sólo a explicar lo mínimo necesario para entender esos mecanismos. El sistema ASCII se basa en una tabla que le asigna un número entre 0 y 255 a un conjunto de caracteres. Por ejemplo, la tabla dice que al caracter 'A' le corresponde el número 65, que al caracter 'a' le corresponde el 97, al caracter 'á' le corresponde el 192, al caracter '7' le corresponde el 55, y al caracter '!' le corresponde el 33.

Además de caracteres básicos (los que se podrían escribir con un teclado occidental), la tabla ASCII también incluye caracteres de control: como veremos, algunos son importantísimos mientras que otros están obsoletos y tenían sentido para cosas como controlar una impresora de punto.

El caracter de control más importante de todos es el que expresa un fin de línea y que en Python se representa como '\n'. En la tabla ASCII, este caracter tiene asignado el número 10. Otros caracteres de control importantes son el número 9 que representa una tabulación ('\t', el caracter que se introduce cuando se presiona la tecla TAB en un teclado) y el caracter 13 que representa un "retorno de carro" que en Python se representa usando '\r'. Aunque ya no tiene ninguna utilidad real, los computadores basados en el sistema operativo Windows aún representan el fin de línea usando la combinación de caracteres '\r\n' [^beep].

[^beep]: Otro caracter interesante es el que tiene el número 7 y que es llamado "beep": cuando se *imprime* este caracter en la consola, el computador debería emitir un anuncio sonoro. En sistemas operativos modernos, el sonido utilizado es el sonido de alerta configurado.

Hoy en día no se utiliza propiamente la tabla ASCII en la mayoría de sistemas. Se usa en cambio UNICODE, que extiende ASCII y sirve para representar más de 137.000 caracteres incluyendo emoticons, kanjis y letras de alfabetos como el cirílico, árabe, hebreo o tailandés. El hecho de que sea una extensión significa que los primeros elementos de UNICODE son los mismos caracteres del sistema ASCII. Es decir que el caracter número 97 en UNICODE también es el caracter 'a'.


#### Funciones chr y ord

Después de haber presentado lo anterior, ahora sí podemos introducir las funciones ```chr``` y ```ord```. La función ```chr``` permite consultar cuál caracter le corresponde a un número específico dentro del sistema UNICODE. Por ejemplo, si evaluamos la expresión ```chr(97)``` el resultado será una cadena de caracteres con el caracter 'a'. La función ```ord``` tiene el objetivo opuesto: dado un caracter, indica cual es el número que le corresponde en el sistema UNICODE.

Los siguientes son algunos ejemplos que permiten estudiar el uso de estas funciones. Dependiendo de la forma en la que esté visualizando este libro es posible que los ejemplos con caracteres especiales no aprecien correctamente.

```python
>>> chr(98)
'b'
>>> ord('B')
66
>>> ord('☻')
9787
>>> chr(9787)
'☻'
>>> chr(22223)
'囏'
```
Finalmente, si se invoca la función ```ord``` usando una cadena con más de un caracter se producirá el siguiente error:

```
TypeError: ord() expected a character, but string of length 3 found
```


## Ejercicios

1. ¿Qué función básica del lenguaje utilizaría para realizar las siguientes actividades?

  * Calcular el valor mínimo entre 5 números.
  * Convertir una cadena de caracteres a un número decimal.
  * Pedirle al usuario un número entero.



2. Consulte cuáles serían los números correspondientes a los siguiente caracteres dentro del sistema Unicode.
  * z
  * G
  * 0
  * 1
  * 2
  * $
  * \

3. Consulte cuáles serían los números correspondientes a los siguientes caracteres dentro del sistema Unicode:

  * El emoji para una cara triste.
  * El emoji para una bandera de Colombia.
  * El kanji japonés para representar la palabra árbol.


4. Escriba un programa que pida al usuario una cantidad de pesos, una tasa de interés y un número de años. Muestre por pantalla en cuánto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida. Recuerde que un capital de C pesos a un interés del x por cien durante n años se convierten en C(1 + x /100)n pesos. (Pruebe su programa sabiendo que una cantidad de 10,000 pesos al 4.5 % de interés anual se convierte en 24,117.14 pesos al cabo de 20 años)


5. Escriba un programa que le pida al usuario 3 valores y los almacene en 3 variables enteras llamadas x1, x2 y x3. El programa luego debe rotar las variables de forma que al final x2 tenga el valor inicial de x1, x3 el de x2 y x1 el de x3.



## Más allá de Python

Esta sección se concentró en la definición de función que utiliza Python y en la descripción de funciones básicas que hacen parte de la librería fundamental del lenguaje. En otros lenguajes de programación el concepto de función es idéntico, mientras que en otros es mucho menos importante. Por ejemplo, en Java o en C++ el concepto que se usa para agrupar instrucciones, nombrarlas y poder invocarlas es el concepto de método. En Python existe también un concepto similar, pero es este libro no lo estudiaremos puesto que está atado al concepto de clase.

Cuando se cambia de lenguaje de programación, una dificultad importante tiene que ver con aprender el nombre y la forma de usar una buena cantidad de elementos básicos del lenguaje, similares a las funciones que estudiamos en esta sección. Por ejemplo, mientras que en Python se usa la función ```print``` para mostrar algo en la consola, en C tendría que usarse ```printf``` y en Java tendría que usarse el método ```println``` del objeto ```System.out```. 

Aunque conceptualmente no sean difícil entender las diferencias y empezar a usar estas otras funciones, aprender todos esos pequeños detalles hace un poco más largo el proceso de pasar de un lenguaje a otro.

En esta sección describimos también el mecanismo de evaluación de funciones, el cual es "eager", mientras que en otros lenguajes es "lazy" (perezoso): esto quiere decir que en esos lenguajes los valores de los parámetros se evaluan en el último momento posible, cuando realemente se necesite su valor. Esto no hace que Python sea malo o ineficiente, pero en algunas situaciones podría llevar a problemas con el desempeño de un programa. 
