Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Más sobre cadenas de caracteres

> El objetivo de esta sección es explorar un poco más el tipo ```str``` y descubrir otras funcionalidades que ofrece Python para manipular cadenas de caracteres. Sin embargo, esta no pretende ser una guía exhaustiva sino un abrebocas para que el lector estudie la documentación Python y descubra muchas otras funcionalidades que están disponibles.

Hace años, cuando se empezaron a construir los primeros computadores programables, el objetivo principal que tenían era permitir hacer cálculos numéricos (trayectorias de misiles, órbitas de naves espaciales, análisis de estructuras, cálculos financieros). Por este motivo, cuando se diseñaron los primeros lenguajes de programación, su diseño estuvo fuertemente influenciado por la necesidad de soportar con facilidad la expresión de cálculos numéricos cada vez más complicados. En esos lenguajes era prácticamente imposible representar una cadena de caracteres.

Hoy en día la situación ha cambiado y la representación y manipulación de información textual es igual o más importante que los cálculos numéricos. Esto ha llevado a que cualquier lenguaje de programación moderno ofrezca sólidos tipos de datos para representar cadenas de caracteres, los cuales vienen acompañados de mecanismos que permiten manipular con facilidad estas cadenas de acuerdo con los requerimientos de cada aplicación. Por ejemplo, hoy en día es muy común que las aplicaciones tengan que incluir mecanismos de internacionalización (para traducir los mensajes a otros idiomas), varios alfabetos diferentes (cirílico, griego, kanjis japoneses y hasta *emojis*), sistemas de cifrado (para garantizar confidencialidad), y sistemas de búsqueda que encuentren términos rápidamente dentro de textos cada vez más grandes. 

En esta sección vamos a continuar con el estudio del tipo ```str``` de Python y vamos a ver algunos de los mecanismos que ofrece para manipular cadenas de caracteres de forma rápida y sencilla. Sin embargo, en esta sección no termina toda la presentación de ```str```: en el siguiente capítulo presentaremos los mecanismos adicionales disponibles que requieren del estudio previo de secuencias e instrucciones repetitivas.


## Aspectos de codificación (encoding)

Si usted está leyendo este libro es muy posible que su lengua materna sea el español, que esté acostumbrado a escribir usando el alfabeto latino y que el teclado de su computador sea un teclado 'QWERTY'[^querty]. Por esto, además de necesitar los 127 caracteres básicos de ASCII, usted también necesita algunos caracteres adicionales, como `'ñ'`, `'Ñ'` y todas las vocales con tilde en mayúsculas y minúsculas. 

Si todo esto es cierto, muy posiblemente usted ha estado utilizando un conjunto de caracteres (encoding) que extiende al conjunto ASCII y que se conoce con el nombre ISO-8859-1: además de tener los 127 caracteres de ASCII, este conjunto incluye caracteres de uso frecuente en lenguajes originados principalmente en Europa occidental. Por ejemplo: á, Á, ñ, Ñ, ç, ü, ò [^error].

Ahora bien, si usted intercambia información con personas que viven en países donde ISO-8859-1 no es de utilidad (por ejemplo, Rusia, Japón, o todo el Sudeste Asiático) tendrá que utilizar un conjunto de caracteres mucho más grande, como el ofrecido por el estándar UNICODE que describe muchos más caracteres incluyendo los cada vez más populares *emojis* - &#128512;. Sin embargo, si usted quiere usar caracteres definidos en UNICODE, los archivos o mensajes que usted escriba tendrán que utilizar bien sea el encoding **UTF-8** o el encoding **UTF-16** [^utf]. 

Si usted puede ver los siguientes tres caracteres (un kanji, un emoji y un caracter griego) significa que su navegador o el programa que está utilizando para leer este texto es compatible con UNICODE y con UTF-8:

 * Kanji: &#23383; 
 * Emoji: &#128540; 
 * Caracter griego: &#916;.

Con esta brevísima explicación no esperamos que usted sea ya un experto en sistemas de codificación de caracteres, pero sí que se dé cuenta que es un asunto más complicado de lo que parece a simple vista. Mientras que sus programas se limiten a usar caracteres que son normales en su idioma, probablemente no tendrá ningún problema. Pero si quiere que sus programas sean capaces de manejar caracteres de otros alfabetos, tendrá que ponerles atención a los asuntos de codificación si no quiere perder información o ver caracteres remplazados por marcas desconocidas. 

La buena noticia es que, por defecto, Python soporta cadenas UNICODE. Así que, si está teniendo problemas con caracteres extraños dentro de sus cadenas, probablemente el problema no sea de Python sino de algo más de lo que usted está haciendo.

Otra cosa con la que usted tiene que tener cuidado es la codificación que utilice para los archivos .py en los que escriba sus programas. La recomendación que le hacemos es que se asegure de que los archivos se guarden con la codificación UTF-8. En Spyder esto se logra poniendo el siguiente comentario al principio de cada archivo:

```python
# -*- coding: utf-8 -*-
```

Si lo hizo correctamente, en la esquina inferior derecha del ambiente debería ver una etiqueta que diga *Encoding: UTF-8*. Si en lugar de esto dice *Encoding: ASCII*, entonces cualquier caracter que usted escriba en su programa y que no sea parte de ASCII (por ejemplo 'á') se convertirá en basura cuando usted cierre el archivo y lo vuelva a abrir.

Finalmente le hacemos una recomendación con respecto al uso de caracteres *no ASCII* dentro de sus programas: está bien usar estos caracteres dentro de la documentación y comentarios, pero evite usarlos en los identificadores de variables, parámetros y nombres de funciones. Por ejemplo, en lugar de llamar a una función ```calcular_año``` use ```calcular_anho```, y en lugar de usar la variable ```máximo``` use la variable ```maximo```. Esta no es una regla escrita en piedra que usted tenga que seguir. Es sólo un consejo para evitar que se tope con problemas sencillos, pero a veces difíciles de diagnosticar.


[^error]: Si usted no puede ver alguno de estos caracteres, significa que el encoding ISO-8859-1 no está soportado o no está activo en su navegador, en el visor que esté utilizando para leer el texto, o en su computador.

[^querty]: QUERTY hace referencia a las primeras 5 letras de la fila de letras superior del teclado.

[^utf]: Esta última parte puede ser un poco complicada de entender. pero no es crítico que entienda todos los detalles: UNICODE define cuáles son los caracteres, cómo deberían verse y qué número le corresponde a cada uno. UTF-8 define cómo se deben representar los caracteres UNICODE usando números binarios de 8, 16, 24 o 32 bits. UTF-16 define cómo representar esos caracteres usando 16 o 32 bits.


## Caracteres de control

Además de los caracteres como los que se describieron en la sección anterior, una cadena de caracteres (```str```) también puede tener caracteres que son llamados caracteres de control. Estos caracteres se pueden usar como cualquier otro dentro de una cadena. 

A continuación, describimos los más importantes y que usted podría necesitar.

Caracter | Significado | Ejemplo de uso | Resultado |
:---------:|:-------------|:----------------|:-----------|
\n       | Cambio de línea | "Hola\nMundo!"| Hola <br/> Mundo!
\t  | Tabulación | "Hola\tMundo" | Hola&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mundo
\\\\  | Barra invertida | "C:\\\\usuarios\\\\invitado" | C:\usuarios\invitado
\'  | Comilla sencilla (2) | "It\'s me!" | It's me!
\"  | Comilla doble | "A so called \"expert\"" | A so called "expert"

Como es posible que con un ejemplo tan breve no se aprecie la importancia de la tabulación, a continuación presentamos un ejemplo un poco más complejo. 
El uso del caracter de tabulación indica que se quiere dejar espacio hasta la siguiente tabulación, con el objetivo de armar columnas más o menos definidas.  Una tabulación típicamente equivale al espacio de 8 caracteres.

```python
print("a\tb\tc" + "\n" + "100\t200\t300")
```

El resultado de ejecutar el programa anterior es el siguiente:

```
a	b	c
100	200	300
```


## Funciones y operadores sobre cadenas de caracteres

En la sección anterior estudiamos los operadores relacionales y vimos que pueden aplicarse a diferentes tipos de datos. En particular, vimos que los operadores <, >, <=, >= hacen comparaciones lexicográficas. De esta manera sabemos que las siguientes expresiones son todas verdaderas:

* ```"AB" < "BC```
* ```"AB" < "ab"```
* ```"234" < "345"```
* ```"!450" < "345"```

Los otros operadores relacionales que podemos aplicar a las cadenas de caracteres son "==" y "!=", los cuales comparan las cadenas caracter por caracter. De esta manera, las siguientes expresiones son todas falsas:

* ```"ABC" == "abc"```
* ```"ABC" == "ABC!"```
* ```"3" == "1+2"```
* ```"Hola, Mundo!" != "Hola, Mundo!"```

Dos nuevos operadores que también se pueden aplicar sobre cadenas de caracteres son ```in``` y ```not in```. El primero permite revisar si una cadena está incluida en otra, mientras que el segundo hace exactamente lo contrario. Veamos un ejemplo de expresiones **verdaderas** basadas en estos operadores:

* ```"Mundo" in "Hola, Mundo!"```
* ```"mundo" not in "Hola, Mundo!"```
* ```"!" in "Hola, Mundo!"```
* ```'?' not in "Hola, Mundo!"```
* ```"Hola, Mundo!" in "Hola, Mundo!"```

Como vemos, estos operadores hacen comparaciones que distinguen entre mayúsculas y minúsculas. Esto debe tenerse en cuenta para evitar tener falsos negativos y falsos positivos.

Finalmente, Python nos ofrece la función ```len``` que podemos utilizar para conocer el tamaño de una cadena.

* ```len("Hola, Mundo!")```
* ```len("Hola,\nMundo!")```
* ```len("")```
* ```len(" ")```
* ```len("\t")```

El resultado de las primeras dos invocaciones es el mismo (12). Esto porque el caracter de control ```\n``` es un solo caracter aunque se represente con dos.

El resultado de la tercera invocación es 0, porque es una cadena vacía (no tiene ningún caracter).

El resultado de las últimas invocaciones es 1 porque se trata de cadenas con sólo un caracter: la cuarta tiene sólo un espacio mientras que la quinta sólo tiene una tabulación. 


## Métodos sobre cadenas de caracteres

### Métodos versus funciones

Además de todo lo que ya hemos estudiado, el tipo ```str``` también ofrece una serie de funciones que pueden utilizarse para transformar cadenas de caracteres. Debido a la forma particular en la que estas funciones están declaradas dentro del módulo ```str```, estas funciones se conocen usualmente como métodos y se pueden invocar de una forma diferente a como lo haríamos con funciones como las que ya conocíamos [^oo].

Para ilustrar este punto, estudiemos la función ```lower``` que está definida dentro del contexto del módulo ```str```. En este módulo es donde se define el tipo que hemos estado usando para las cadenas de caracteres. Usando la función ```help``` podemos consultar la documentación de esta función:

```python
>>> help (str.lower)
Help on method_descriptor:

lower(self, /)
    Return a copy of the string converted to lowercase.
```

Lo que esto nos dice es que si invocamos esta función usando como parámetro una cadena de caracteres vamos a recibir como respuesta *una copia* de la cadena en la cual las letras se habrán pasado todas a minúsculas. Veamos una prueba que nos ayuda a comprobar que esta interpretación es correcta:

```python
>>> str.lower('ABcdEg')
'abcdeg'
```

Sin embargo, la documentación de la función también nos dice que esta función es un método, así que podemos invocarla de una forma un poco diferente que en la mayoría de los casos resulta más conveniente:

```python
>>> 'ABcdEg'.lower()
'abcdeg'
``` 
Observe como el parámetro de la función pasó a ocupar el lugar frente al caracter ```.```, dejando a la función sin parámetro. 

La pregunta que cabe hacer en este punto es ¿cómo sabe Python que la función está definida dentro del módulo ```str```? La respuesta está en que Python primero va a verificar el tipo del valor ```'ABcdEg'``` y como el tipo es ```str``` significa que las funciones que se llamen sobre este valor tienen que estar implementadas en el módulo ```str```.

Hagamos ahora el mismo ejercicio con la función llamada ```str.zfill```:

```python
>>> help(str.zfill)
Help on method_descriptor:

zfill(self, width, /)
    Pad a numeric string with zeros on the left, to fill a field of the given width.

    The string is never truncated.
```

La documentación nos dice que esta función le va a agregar ceros a la izquierda a una cadena, hasta lograr una cadena de la longitud indicada. La documentación también nos dice que esta función requiere dos parámetros (*self* y *width*). Como es un método, esta función podría llamarse sobre una cadena de la siguiente manera:

```python
>>> "abc".zfill(10)
'0000000abc'
```

Si quisiéramos invocarla de la manera *normal*, tendríamos que convertir la cadena en el primer parámetro e indicar en qué módulo está definida la función. El resultado sería el siguiente:

```python
>>> str.zfill("abc", 10)
'0000000abc'
```

En resumen: el módulo ```str``` ofrece unas funciones llamadas métodos que implementan una gran cantidad de funcionalidades interesantes para trabajar con cadenas de caracteres. Estas funciones se pueden invocar de dos formas: **como funciones**, usando un llamado de la forma ```str.funcion(cadena, ...otros parámetros ...)```, o **como métodos**, usando un llamado de la forma ```cadena.metodo(... otros parámetros ...)```. De acá en adelante nosotros vamos a usar estas funciones de la segunda forma (como métodos).


[^oo]: Siendo más precisos, ```str``` es en Python una *clase* y las clases definen un espacio de nombres dentro de los que están definidas un conjunto de funciones que son llamados métodos. Como se anunció en la introducción, en este libro no se tratará el tema de la programación orientada a objetos, así que no ahondaremos en el tema de la definición de clases y métodos. Sin embargo, para construir efectivamente programas Python, es necesario saber que existen librerías básicas basadas en clases, como el caso de ```str```, y es necesario ser capaz de utilizar los métodos implementados en esas librerías.

### Inmutabilidad

Antes de presentar los métodos más utilizados de ```str``` es muy importante hablar de la *inmutabilidad* de las cadenas de caracteres en Python. Esto significa que cuando Python construye una cadena no puede modificarla para cambiar su contenido. Si queremos hacerle algún cambio a la cadena, lo único que Python puede hacer es construir una nueva cadena con los cambios requeridos.

Observemos un ejemplo utilizando el método ```lower``` que ya estudiamos y los operadores ```is``` (comparación de identidad) y ```==``` (comparación de igualdad).

```python
original = "texto original"
minusculas = original.lower()
print("Son iguales:", original == minusculas)
print("Son el mismo:", original is minusculas)
```

El resultado de ejecutar este pequeño programa es el siguiente:

```python
Son iguales: True
Son el mismo: False
```

Lo que esto nos muestra es que, como dice la documentación del método, ```lower()``` retorna una *copia* de la cadena en la cual se hayan hecho las modificaciones para que todas las letras sean minúsculas. En el caso de nuestro ejemplo no hubo ninguna modificación (la comparación de igualdad es exitosa) y de todas maneras el método creó una copia de la cadena original.

**Recuerde:** Las cadenas de caracteres en Python son *inmutables*. Todas las operaciones que se realicen sobre una cadena siempre van a producir una **cadena nueva**.


### Métodos de str

Los siguientes son algunos de los métodos de ```str``` que podría necesitar con más frecuencia cuando trabaje con cadenas de caracteres.

#### Mayúsculas y minúsculas

Nombre | Descripción  |  Ejemplo  |  Resultado  |
:-------|:--------------|:-----------|:-------------|
lower  | Remplaza todas las mayúsculas por minúsculas | "Hola, Mundo!".lower()  | 'hola, mundo!'
upper  | Remplaza todas las minúsculas por mayúsculas | "Hola, Mundo!". upper()  | 'HOLA, MUNDO!'
title  | Le pone mayúscula inicial a todas las palabras de la cadena | "Hola, Mundo!". title()  | 'Hola, Mundo!'
swapcase  | Intercambia mayúsculas por minúsculas y viceversa | "Hola, Mundo!". swapcase()  | 'hOLA, mUNDO!'


#### Análisis de cadenas

Nombre | Descripción  |  Ejemplo  |  Resultado  |
:-------|:--------------|:-----------|:-------------|
find   | Busca la primera posición en la que aparezca la cadena buscada. Si no la encuentra retorna -1. | "Hola, Mundo!".find('o')  | 1
rfind  | Busca la primera posición en la que aparezca la cadena buscada, empezando por la derecha. Si no la encuentra retorna -1. | "Hola, Mundo!".rfind('o')  | 10
count  | Cuenta cuántas veces está la cadena indicada en otra cadena. Si no la encuentra se produce un error. | "Hola, Mundo!".count('o')  | 2
isnumeric  | Revisa si todos los caracteres de una cadena son números | "Hola, Mundo!".isnumeric()  | False 


#### Manipulación de cadenas

Nombre | Descripción  |  Ejemplo  |  Resultado  |
:-------|:--------------|:-----------|:-------------|
replace   | Remplaza algunos elementos de una cadena con otros elementos que llegan como parámetro. El reemplazo puede ser la cadena vacía para eliminar los elementos buscados. | "Hola, Mundo!".replace('o', '67')  | 'H67la, Mund67!'
strip   | Elimina espacios y cambios de línea al final de una cadena de caracteres. No elimina ningún elemento que no se encuentre al final de la cadena. | "Hola, Mundo!   \n".strip()  | 'Hola, Mundo!'
ljust   | Amplía la cadena hasta el ancho indicado, alinea el contenido a la izquierda y llena el espacio vacío con espacios. | "Hola, Mundo!".ljust(15)  | 'Hola, Mundo!&nbsp;&nbsp;&nbsp;&nbsp;'
rjust   | Amplía la cadena hasta el ancho indicado, alinea el contenido a la derecha y llena el espacio vacío con espacios | "Hola, Mundo!".rjust(15)  | '&nbsp;&nbsp;&nbsp;Hola, Mundo!'
center   | Amplía la cadena hasta el ancho indicado y centra el contenido. | "Hola, Mundo!".center(15)  | '&nbsp;&nbsp;Hola, Mundo!&nbsp;'
zfill   | Amplía la cadena hasta el ancho indicado, alinea el contenido a la derecha y llena el espacio vacío con caracteres ```0```. | "Hola, Mundo!".zfill(15)  | '000Hola, Mundo!'


#### El resto de métodos

El módulo ```str``` ofrece una gran cantidad de métodos adicionales que no vamos a cubrir acá pero que sí están bien descritos en la documentación de Python: https://docs.python.org/3.6/library/stdtypes.html#string-methods

Le recomendamos estudiar esa documentación y practicar con todos estos métodos para aprender a utilizarlos y agregarlos a su caja de herramientas de programación.



## Format

Las últimas funcionalidades de las cadenas de caracteres que vamos a estudiar tienen que ver con el método `format`. Este método es muy poderoso y permite utilizar repetidamente una cadena como plantilla para luego remplazar algunos fragmentos por valor particulares. 

Supongamos que tenemos que hacer un programa que sea capaz de generar las siguientes cadenas:

```
Un Lamborghini Aventador del 2016 con motor de 6.5 litros es capaz de pasar de 0 a 100 kph en 2.80 segundos
Un Ferrari Enzo del 2002 con motor de 6.0 litros es capaz de pasar de 0 a 100 kph en 3.60 segundos
Un Bugatti Veyron 16.4 del 2010 con motor de 8.0 litros es capaz de pasar de 0 a 100 kph en 2.50 segundos
Un Porsche 911 GT3 del 2011 con motor de 4.0 litros es capaz de pasar de 0 a 100 kph en 3.80 segundos
Un McLaren P1 del 2013 con motor de 3.8 litros es capaz de pasar de 0 a 100 kph en 2.80 segundos
Un Pagani Huayra BC del 2017 con motor de 6.0 litros es capaz de pasar de 0 a 100 kph en 3.30 segundos
```

Todas estas cadenas tienen la misma estructura que incluye la marca del carro, el nombre del modelo, el año de lanzamiento, el tamaño del motor en litros usando una cifra decimal y el tiempo que necesita para pasar de 0 a 100 kilómetros por hora expresado en segundos con dos cifras decimales.

Estas cadenas se podrían haber armado usando concatenaciones. Sin embargo, el método `format` ofrece características para estructurar las cadenas que son muy difíciles de replicar usando sólo concatenaciones.

Tomemos como ejemplo la plantilla utilizada para generar los mensajes anteriores:

```python
plantilla = "Un {0} {1} del {2:d} con motor de {3:.1f} litros es capaz de pasar de 0 a 100 kph en {4:.2f} segundos"
```

En primer lugar, la plantilla es una cadena de caracteres que tiene marcas rodeadas por los caracteres `{` y `}` en los campos donde se tendrán que insertar valores. Aunque no es obligatorio, es recomendable numerar esos campos empezando desde el 0 y llegando, en este caso, hasta el 4. 

Además del número, cada campo también puede tener una especificación de su formato, la cual viene a continuación del caracter `:`. En nuestro caso, los campos 0 y 1 no tienen ningún formato, así que lo que metamos en esas posiciones se remplazará sin ningún cambio. Para el campo 2 sólo usamos el caracter `d` para indicar que se trataba de un número entero. Para los campos 3 y 4 especificamos que se trataban de números decimales y además dijimos que nos interesaba tener 1 dígito decimal en el primer caso y 2 dígitos decimales en el segundo. Esto quedó especificado usando los formatos `.1f` y `.2f` respectivamente.

Para usar una plantilla se tiene que invocar el método `format` utilizando como parámetros los valores que queremos insertar en los campos. En nuestro caso, invocamos la función `format` con 5 parámetros:

```python
mensaje = plantilla.format(marca, modelo, anho, cc, sec)
```

Acá puede verse la importancia de numerar los campos: el valor marca quedará en el campo marcado con el 0, el valor modelo en el campo marcado con el 1 y así sucesivamente. Esto significa que el orden en el que aparecen los campos en la plantilla no necesariamente es el mismo orden en que se deben pasar los argumentos. También significa que, si hubiéramos marcado dos campos con el mismo número, el valor correspondiente habría aparecido dos veces en el mensaje.

Estudiemos ahora otros mensajes que tienen un poco más de complicaciones que no son fáciles de solucionar sólo usando concatenación de cadenas:

```
100 metros     5.3 s @ 126 kph
500 metros    13.6 s @ 211 kph
1000 metros   22.0 s @ 249 kph
``` 

Estos nuevos mensajes tienen una característica que no tenían los mensajes anteriores: los campos no están completamente llenos y están alineados a la derecha (columnas 2 y 3) o a la izquierda (columna 1). Analicemos entonces la plantilla que se utilizó en este caso

```python
plantilla2 = "{0:<14}{1:>4.1f} s @ {2:>3d} kph"
```

El formato para el primer campo dice `<14`, lo cual se interpreta como que se debe alinear el contenido a la izquierda y que debe tener 14 caracteres de ancho en total. Si el contenido del campo es más corto que esto, se agregarán tantos espacios como haga falta *a la derecha del contenido*.

El formato para el segundo campo dice `>4.1f`. Como ya sabemos, `.1f` significa que se tratará de un número con exactamente un decimal. La otra parte, `>4` indica que el número debe alinearse a la derecha y que debe ocupar, en total, el espacio de 4 caracteres. En este caso como el número está alineado a la derecha los caracteres faltantes se agregan a la *izquierda del contenido*.

El formato para el tercer campo es muy similar: se espera un número entero que terminará alineado a la derecha en una columna de 3 caracteres de ancho.  

Finalmente, veamos cómo se generaron las 3 cadenas invocando el método `format` sobre la plantilla:

```python
plantilla2.format('100 metros', 5.3, 126)
plantilla2.format('500 metros', 13.6, 211)
plantilla2.format('1000 metros', 22, 249)
```

En resumen, cuando se construye una plantilla para usar con el método `format` se debe:

1. Marcar los campos que se van a remplazar, numerándolos de cero en adelante.
2. Para cada campo que se quiera alinear, indicar si la alineación debe ser a la izquierda (<), derecha (>) o el centro (^) y el ancho que debe tener el campo. También se puede especificar el caracter que se debe utilizar para los espacios vacíos (ver documentación).
3. Especificar el formato, especialmente si se trata de números decimales.

Se puede conseguir mucha más información sobre la especificación de plantillas usando el comando `help('FORMATTING')`. La documentación completa también está disponible en 
[https://docs.python.org/3.7/library/string.html#format-string-syntax](https://docs.python.org/3.7/library/string.html#format-string-syntax)


   
## Ejercicios

1. Escriba una función que reciba una cadena de caracteres y una letra. Su función debe retornar la misma cadena que recibió, pero cambiando todas las vocales por la letra que también llegó por parámetro. Por ejemplo, si la cadena original era "Hola, Mundo!" y la letra entregada fue 'I', el resultado debería ser "HIlI, MIndI!".

2. Escriba una función que reciba dos cadenas de caracteres. La función debe retornar 1 si las cadenas son idénticas, 2 si las cadenas sólo se diferencian por las mayúsculas y minúsculas, o 0 de lo contrario.

3. Escriba una función que reciba dos cadenas de caracteres que sólo van a contener letras mayúsculas y minúsculas. La función debe retornar -1 si en un diccionario la primera cadena debería ir antes que la segunda, debe retornar 1 si la segunda cadena debe ir antes que la primera, o 0 si las dos cadenas son la misma (ignorando mayúsculas y minúsculas).

4. Escriba una función que reciba una cadena de caracteres y cuente las palabras que aparecen en la cadena. Usted puede suponer que la cadena tendrá letras (mayúsculas y minúsculas) y espacios, pero no tendrá ningún signo de puntuación ni espacios seguidos.

5. Tres equipos de futbol participaron en un pequeño torneo en que jugaron entre ellos 3 partidos. Escriba una función que reciba el nombre de los tres equipos y los marcadores de los tres partidos, y que retorne una tabla con las posiciones de los equipos al finalizar el torneo. La función recibirá entonces 9 parámetros: primero los nombres de los tres equipos y luego 6 enteros con los marcadores de los 3 partidos. Cada partido ganado entregaba 3 puntos y cada partido empatado entregaba 1 punto. La tabla con el resultado del torneo tiene que ser una cadena de caracteres con la información organizada en columnas bien alineadas. Las columnas deben estar organizadas de la siguiente forma: 
  * posición, 
  * nombre del equipo, 
  * puntos obtenidos, 
  * partidos jugados, 
  * partidos ganados, 
  * partidos empatados, 
  * partidos perdidos, 
  * goles a favor, 
  * goles en contra, 
  * diferencia de goles


6. Escriba una función que, dada la altura de un edificio, retorne una cadena como en el siguiente ejemplo: *"Un objeto que cae de un edificio de 30 metros tarda 2.47 segundos en llegar al piso y alcanza una velocidad de 24.25 metros por segundo."* Su programa debe usar las funciones de formato de cadenas. 

**Ayuda:** El tiempo que tarda la caída es igual a la raíz cuadrada de dos veces la altura sobre la aceleración de la gravedad (9.8 m/s<sup>2</sup>). La velocidad que alcanza el objeto es igual al tiempo de la caída multiplicado por la aceleración de la gravedad.

7. Escriba una función que dados el nombre de un país, la cantidad de habitantes en millones y el Producto Interno Bruto en millones de USD,  retorne una cadena como en el siguiente ejemplo: "Colombia.................=*******45 millones*******=&nbsp;&nbsp;&nbsp;&nbsp;336599 USD Million". La primera columna debe estar alineada a la izquierda, debe tener 25 caracteres y ocupar los espacios vacíos con `.`; la segunda columna debe estar centrada, tener 25 caracteres y ocupar los espacios vacíos con `*`; la tercera columna debe estar alineada a la derecha, tener 10 caracteres más el espacio ocupado por ` USD Million` y debe ocupar los espacios vacíos con espacios.


## Más allá de Python

Las cadenas de caracteres son de muchísima importancia en prácticamente todos los lenguajes de programación, pero hay mucha variedad en los mecanismos para representarlos y manipularlos. Por ejemplo, en lenguajes como C y C++ el uso de cadenas de caracteres no es tan sencillo como en lenguajes más modernos puesto que se construyen sobre tipos más sencillos y requieren de particular cuidado para evitar problemas en la manipulación de la memoria. En lenguajes como Java y Python, estas limitaciones ya no existen y las cadenas se pueden usar con mucha más facilidad, aunque sigue siendo necesario poner mucha atención a ciertos detalles. Por ejemplo, en Java las cadenas de caracteres son objetos que aparentemente son como cualquier objeto otro, pero reciben un tratamiento *preferencial*: hay expresiones en el lenguaje específicas para trabajar con cadenas y el compilador procesa de forma diferente los objetos de tipo String que se construyan explícitamente dentro de un programa.

Otro aspecto común en varios lenguajes es el que tiene que ver con la inmutabilidad de las cadenas de caracteres. Así como en Python, en Java y en otros lenguajes las cadenas de caracteres son inmutables: una vez se construyen no pueden cambiar su contenido. Esto se hace por motivos de eficiencia tanto en los cálculos como en el uso de memoria, pero podría llevar a errores si no se tiene en cuenta esta condición.

En Python las cadenas de caracteres tienen otra propiedad muy interesante y es que son *secuencias*. Es decir que pueden manipularse igual que como se manipularían listas, diccionarios y otras estructuras de datos básicas del lenguaje. Este aspecto de las cadenas de caracteres se estudiará en el siguiente capítulo.


#### Notas 

