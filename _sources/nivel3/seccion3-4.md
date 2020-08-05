```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```



# Slicing

```{admonition} Objetivo de la sección
El objetivo de esta sección es presentar la herramienta de *slicing* ofrecida por Python y demostrar su uso sobre listas y cadenas.
```

La expresión *slicing* hace referencia a la operación por medio de la cual se extraen elementos de una secuencia, tal como una lista o una cadena de caracteres. Dependiendo del caso, los elementos podrían ser consecutivos o podrían estar separados dentro de la secuencia original. Dado que esta operación es de uso bastante frecuente, Python ofrece características que hacen posible construir *slices* de forma breve, sin tener que construir funciones especializadas para hacerlo.

Esta sección explica cómo crear *slices* en Python a partir de listas y cadenas de caracteres [^tipos]. Además, se presentará la forma en la cual se podrían implementar funcionalidades equivalentes utlizando ciclos.

[^tipos]: Aunque en esta sección nos concentramos en listas y cadenas de caracteres, otros tipos de datos pueden soportar *slicing* también. En particular, soportar estas operaciones requiere la implementación cuidadosa del método `__getitem__`.


## Slicing básico: inicio y fin

Supongamos que tenemos la siguiente cadena de caracteres con la que inicia el himno de Colombia: 

```python
cadena = '¡Oh, gloria inmarcesible! ¡Oh, júbilo inmortal!'
```

En secciones anteriores ya hemos estudiado cómo podemos hacer para extraer elementos de esta cadena usando paréntesis cuadrados y una posición numerada desde cero.

```python
>>> cadena[0]
'¡'
>>> cadena[1]
'O'
```

Para extraer más de un elemento podemos indicar la posición inicial y la posición final usando `':'` como separador. Eso lo hemos hecho en los siguientes ejemplos:

```python
>>> cadena[0:11]
'¡Oh, gloria'
>>> cadena[1:11]
'Oh, gloria'
```

En el primer caso estamos extrayendo un *slice* de la cadena original que tiene sólo los caracteres desde la posición 0 hasta la 11 (excluida), mientras que en el segundo caso lo hacemos desde la posición 1 hasta la 11 (excluida). Es decir que, la posición inicial se incluye dentro del *slice* resultante, pero la posición final **siempre queda por fuera**.

Es también frecuente que se quiera extraer un conjunto de elementos que se encuentran al final o al principio de una cadena. En estos casos lo que se debe hacer es no incluir explícitamente el inicio o el fin, pero sí utilizar el separador `':'`. Si no se quiere dejar el espacio vacío, otra alternativa es usar None para la posición. Esto puede verse en los siguientes ejemplos:

```python
>>> cadena[30:]
' júbilo inmortal!'
>>> cadena[:30]
'¡Oh, gloria inmarcesible! ¡Oh,'
>>> cadena[None:30]
'¡Oh, gloria inmarcesible! ¡Oh,'
```

En el primer caso, se extrae un *slice* con los caracteres que se encuentran a partir de la posición 30. En el segundo caso, se extrae un *slice* con los caracteres que se encuentran desde el inicio de la cadena hasta el caracter 30 (excluido). 

Algo para notar es que hay una diferencia importante entre no incluir el fin e incluir un valor explícito: como la última posición nunca se incluye en el *slice*, al no incluir la posición final se está asumiento que se debe llegar hasta el final; si por el contrario se hiciera explícita la última posición, el último valor no se incluiría en el *slice*.

```python
>>> cadena[40:]
'mortal!'
>>> cadena[40:46]
'mortal'
```

Veamos ahora cómo podríamos hacer para extraer la primera frase del himno. Recuerde que el método `index` permite saber en qué posición aparece un determinado caracter dentro de una cadena.

```python
>>> cadena[cadena.index('¡') : cadena.index('!')+1]
'¡Oh, gloria inmarcesible!'
```

Finalmente, si no se incluyen ni la posición inicial ni la final, se entiende que se quiere un *slice* que incluya todos los elementos. En el caso de las listas, esto es equivalente a crear una **copia** de la estructura original.

```python
# Crear una copia de la cadena original
cadena2 = cadena[:]
```


## Slicing intermedio: posiciones negativas

Algo muy interesante en Python con respecto a los *slices*, es que las posiciones de inicio y de fin no necesariamente tienen que ser números positivos: si se usan números negativos, Python asume que se están referenciando las posiciones numeradas desde la última hasta la primera, empezando con -1. Esto se presenta claramente en la {numref}`figura {number} <slicing>`, en la que hemos numerado las posiciones:

```{figure} ./images/slicing.png
---
width: 100%
name: slicing
---
Posiciones numeradas en una cadena
```

Acá podemos ver que cada caracter tiene dos números que indican la posición: uno positivo y uno negativo. Por ejemplo, la última posición de la cadena es la `11` (uno menos que el tamaño de la cadena) y es también la posición `-1`. El penúltimo caracter se encuentra en la posición `10` o, más explícitamente, en la posición `-2`. Finalmente, veamos que el primer caracter de la cadena se encuentra en la posición `0`y en la posición `-12`. Es decir que el primer caracter se puede encontrar siempre multiplicando por `-1` el tamaño de la cadena.

Veamos ahora un ejemplo en que consultamos posiciones negativas sobre nuestra cadena de ejemplo:

```python
>>> cadena[-1]
'!'
>>> cadena[-2]
'l'
```
Las posiciones positivas y negativas son equivalentes y son intercambiables. En los siguientes ejemplos se pueden ver combinaciones de posiciones positivas y negativas para indicar el inicio y el fin de un *slice*.

```python
>>> cadena[-47: -36]
'¡Oh, gloria'
>>> cadena[0: -36]
'¡Oh, gloria'
>>> cadena[-47: 11]
'¡Oh, gloria'
>>> cadena[-47:]
'¡Oh, gloria inmarcesible! ¡Oh, júbilo inmortal!'
>>> cadena[:-1]
'¡Oh, gloria inmarcesible! ¡Oh, júbilo inmortal'
```


## Slicing avanzado: cambiando el paso

Estudiaremos ahora el tercer parámetro disponible para describir un *slice* en Python, el cual también se separa usando el caracter `':'`. Este tercer parámetro, que tiene como valor por defecto `1`, indica cómo se deben recorrer las posiciones desde el inicio hasta el fin. Así, cuando su valor es `1` con cada *paso* se va a sumar `1` a la posición actual, mientras que cuando el valor es `-2` con cada *paso* se resta `2` a la posición actual.

Veamos cómo funciona esto sobre nuestra cadena de ejemplo:

```python
>>> cadena[::2]
'¡h lraimreil!¡h úioimra!'
>>> cadena[::-2]
'!armioiú h¡!liermiarl h¡'
```
En el primer caso, se extrae toda la cadena con un paso de 2: se parte de la posición 0  y se extraen las letras de la cadena, avanzando de 2 en 2 hasta llegar al final de la cadena. En el segundo caso, el paso es -2: se parte de la última posición y se extraen las posiciones retrocediendo de 2 en 2 hasta llegar a la cadena.

El tercer parámetro de un *slice* es particularmente útil para invertir una cadena. Así, un *slice* descrito como `[::-1]` siempre servirá para obtener una cadena invertida.

```python
>>> cadena[::-1]
'!latromni olibúj ,hO¡ !elbisecramni airolg ,hO¡'
```

Al usar el parámetro del *paso*, se debe tener cuidado de construir una expresión coherente. Por ejemplo, si se quiere recorrer desde la posición `0` hasta la `5`, el paso no podría ser `-1` porque desde `0` sería imposible llegar a `5` restando `1`cada vez. Tampoco tendría sentido intentar ir de `-1` a `0` con un paso de `2`.


## Slices sobre listas

En las secciones anteriores hemos ilustrado el uso de *slices* sólo sobre cadenas de caracteres. Sin embargo, es posible también aplicar estas mismas técnicas sobre listas, como se muestra a continuación:

```python
>>> valores
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> valores[0:5]
[0, 1, 2, 3, 4]
>>> valores[5:]
[5, 6, 7, 8, 9, 10]
>>> valores[2:-1:2]
[2, 4, 6, 8]
>>> valores[-1::-2]
[10, 8, 6, 4, 2, 0]
>>> valores[-1:0:-2]
[10, 8, 6, 4, 2]
```
Aunque sencillos, estos ejemplos muestran que el mecanismo de *slicing* se aplica exactamente igual sobre listas que sobre cadenas de caracteres.

## Reemplazando slices por ciclos

La funcionlidad de *slicing* de Python es muy útil porque simplifica el uso de operaciones que se requieren frecuentemente. Sin embargo, no muchos lenguajes ofrecen capacidades comparables para describir *slices* como en Python, así que es conveniente saber cómo reemplazar esta funcionalidad con funciones basadas en ciclos.

En el siguiente fragmento de código mostramos la función `extraer_slice`, la cual permite construir *slices* de forma prácticamente equivalente a como lo hace Python con su sintaxis especializada.

```python
def extraer_slice(elementos: list, inicio: int, fin: int, paso: int) -> list:
  """ Extrae un slice de una lista.
  Parámetros:
    elementos (list): la lista de la que se van a extraer los elementos.
    inicio (int): la primera posición desde la que se van a extraer los elementos. Puede ser un número negativo.
    fin (int): la última posición de la que se van a extraer los elementos. Puede ser un número negativo.
    paso (int): indica cada cuántas posiciones se va a extraer un elemento. Puede ser un número negativo.
  Retorno:
    (list): Una lista con los elementos extraídos desde 'inicio' hasta 'fin', donde los elementos extraídos están separados por 'paso' posiciones.
  """
  tam = len(elementos)
  # Si la posición inicial es negativa, se busca el número positivo equivalente
  if inicio < 0:
    inicio = tam + inicio
  # Asegurar que el inicio siempre esté dentro de la lista
  inicio = max(0, inicio) 
  inicio = min(inicio, tam-1)
  # Si la posición final es negativa, se busca el número positivo equivalente
  if fin < 0:
    fin = tam + fin

  # Preparar la lista resultante
  slice = []
  posicion = inicio
  # El ciclo se repite mientras siga siendo posible avanzar desde
  # la posición actual hacia la posición final y se estén consultando
  # posiciones que estén dentro de la lista
  while (posicion >= 0 and posicion < tam) and \ 
        ((posicion < fin and paso > 0) or (posicion > fin and paso < 0)):
    slice.append(elementos[posicion])
    posicion += paso  
  return slice
```

Las principales diferencias entre esta función y las funcionalidad nativa de Python son las siguientes:

  * Nuestra función no tiene valores por defecto, así que todos los parámetros son obligatorios.
  * Se debe especificar explícitamente el fin del recorrido (no se puede dejar en blanco).

Veamos ahora cómo se comporta la función cuando se aplica a una lista de números.


```python
>>> valores = [0,1,2,3,4,5,6,7,8,9,10]
>>> print(extraer_slice(valores,2,9,1))
[2, 3, 4, 5, 6, 7, 8]
>>> print(extraer_slice(valores,2,9,3))
[2, 5, 8]
>>> print(extraer_slice(valores,-9,9,3))
[2, 5, 8]
>>> print(extraer_slice(valores,9,-9,-3))
[9, 6, 3]
>>> extraer_slice(valores, 5, 50, 1)
[5, 6, 7, 8, 9, 10]
>>> extraer_slice(valores, 50, 5, -1)
[10, 9, 8, 7, 6]
```
  
## Modificar listas usando slices

Además de permitir la extracción de partes de una cadena o de una lista, los *slices* también tienen un rol importante en la modificación de los elementos de una lista.

Empecemos por el caso más sencillo, en el cual se calcula un slice con sólo una posición:

```python
>>> valores = [0,1,2,3,4,5,6,7,8,9,10]
>>> valores[1] = 99
>>> valores
[0, 99, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Si en cambio calculamos un *slice* que pueda tener uno o más valores, es necesario que el valor que asignemos sea también una lista para que pueda remplazar a los elementos del *slice*. En el siguiente ejemplo, primero remplazamos el *slice* de tamaño 1 que se calcula entre las posiciones 3 y 4. A continuación, calculamos un *slice* que va desde la posición 4 hasta la 7 y lo reemplazamos por la lista que sólo tiene el número 97. Finalmente reemplazamos todos los elementos que se encuentran a partir de la posición 5 por los elementos de la lista `[96, 95, 94]`.

```python
>>> valores[3:4] = [98]
>>> valores
[0, 99, 2, 98, 4, 5, 6, 7, 8, 9, 10]
>>> valores[4:7] = [97]
>>> valores
[0, 99, 2, 98, 97, 7, 8, 9, 10]
>>> valores[5:] = [96, 95, 94]
>>> valores
[0, 99, 2, 98, 97, 96, 95, 94]
```

En los ejemplos anteriores, sólo utilizamos el avance por defecto (1). Si queremos utilizar un avance diferente, positivo o negativo, tenemos que tener en cuenta que los valores que vayamos a asignar tienen que tener exactamente el mismo tamaño que el *slice* que se esté calculando. Observemos los siguientes ejemplos que ilustran este punto. 

* Después de haber inicializado de nuevo la lista de valores, intentamos asignarle una lista de tamaño 1 a un *slice* de tamaño 6: Python nos advierte del error de manera muy explícita. 
* En el siguiente intento, asignamos los valores `['a', 'b', 'c', 'd', 'e', 'f']` al mismo slice lo cual sí funciona y modifica la lista de acuerdo a lo que esperábamos. 
* Finalmente, calculamos un *slice* empezando desde la última posición y hacemos la asignación de un nuevo conjunto de valores: `['x', 'y', 'z']`.


```python
>>> valores = [0,1,2,3,4,5,6,7,8,9,10]
>>> valores[-1::-2] = [99]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 1 to extended slice of size 6
>>> valores[::2] = ['a', 'b', 'c', 'd', 'e', 'f']
>>> valores
['a', 1, 'b', 3, 'c', 5, 'd', 7, 'e', 9, 'f']
>>> valores[-1::-4] = ['x', 'y', 'z']
>>> valores
['a', 1, 'z', 3, 'c', 5, 'y', 7, 'e', 9, 'x']
```

### Mínimo Común Múltiplo

Para cerrar esta sección vamos a presentar un ejercicio en el cual la modificación de listas son *slices* resulta de mucha utilidad.

El **mínimo común múltiplo** de dos enteros es el número menor que es múltiplo de ambos enteros. Existen varios algoritmos para encontrar este número, pero acá vamos a presentar una propuesta que basada en el uso de *slices* y en la idea de que el mínimo común múltiplo nunca puede ser superior a la multiplicación de los dos enteros.

El algoritmo que vamos a utilizar se basa en el siguiente esquema:

1. Construir dos listas de valores booleanos que tenga un tamaño igual al máximo valor posible del mínimo común múltiplo. Llenar esas listas con el valor `False`.
2. Poner el valor `True` en todas las posiciones de la primera lista que correspondan a un múltiplo del primer entero.
3. Poner el valor `True` en todas las posiciones de la segunda lista que correspondan a un múltiplo del segundo entero.
4. Buscar la posición en la cual tanto en la primera lista como en la segunda lista se encuentre el valor `True`.

La siguiente función implementa el algoritmo y utiliza *slices* para modificar fácilmente las listas.

```python
def minimo_comun_multiplo(a: int, b:int) -> int:
  maximo = a * b
  multiplos_a = [False] * (maximo+1) # Crea la primera lista
  multiplos_a[a::a] = [True]*b # Marca con True los múltiplos de a
  multiplos_b = [False] * (maximo+1) # Crea la segunda lista
  multiplos_b[b::b] = [True] * a # Marca con True los múltiplos de b
  # Empieza la búsqueda del mcm
  encontre_mcm = False
  candidato_mcm = max(a,b)
  while not encontre_mcm:
    if multiplos_a[candidato_mcm] and multiplos_b[candidato_mcm]:
      encontre_mcm = True
    else:
      candidato_mcm += 1
  return candidato_mcm
```

A continuación se muestran vairos llamado a la función y el resultado que se obtiene en cada caso.

```python
>>> minimo_comun_multiplo(4, 6)
12
>>> minimo_comun_multiplo(4, 5)
20
>>> minimo_comun_multiplo(4, 8)
8
>>> minimo_comun_multiplo(10, 14)
70
>>> minimo_comun_multiplo(4, 9)
36
```

Para complementar este ejemplo, presentamos una segunda versión de la función en la cual se utilizan dos elementos que no se han estudiado hasta ahora: la función `zip` y el tipo de dato `tuple`. La primera parte de esta solución es idéntica a la anterior, pero utiliza otro mecanismo para buscar el mínimo común múltiplo. 

1. Primero, la función `zip` se encarga de construir parejas de valores de las dos listas (el primer elemento de una lista se empareja con el primer elemento de la segunda lista, el segundo con el segundo y así sucesivamente). 
2. Luego, se utiliza el método `index` del tipo `list` para buscar la posición de un elemento. En este caso, lo que se busca es una pareja en la cual los dos valores sean `True`. La posición en la que esta pareja se encuentre debería ser el valor del mínimo común múltiplo.


```python
def minimo_comun_multiplo_zip(a: int, b:int) -> int:
  maximo = a * b
  multiplos_a = [False] * (maximo+1)
  multiplos_a[a::a] = [True]*b
  multiplos_b = [False] * (maximo+1)
  multiplos_b[b::b] = [True] * a
  parejas = list(zip(multiplos_a, multiplos_b))
  candidato_mcm = parejas.index((True, True))
  return candidato_mcm
```

```python
>>> minimo_comun_multiplo_zip(4, 6)
12
>>> minimo_comun_multiplo_zip(10, 14)
70
>>> minimo_comun_multiplo_zip(4, 9)
36
```

Finalmente vamos a presentar una solución a este problema que es considerablemente más eficiente y que se basa en que el mínimo común múltiplo se puede calcular a partir del máximo común divisor.

\begin{equation}
  mcm(a, b)= \frac{|a·b|}{MCD(a, b)}
\end{equation}

```python
import math
def minimo_comun_multiplo_rapido(a: int, b:int) -> int:
  mcm = (a*b)/math.gcd(a,b)
  return mcm
```
En este caso estamos usando la función para calcular el máximo común divisor que provee Python en su módulo math, pero podríamos implementar nuestra propia función si fuera necesario (en otro punto de este libro se propone este problema).


## Ejercicios ##

1. Escriba una función que le sirva para *reconocer* si una palabra es o no palíndrome (se lee igual al derecho y al revés). Su función sólo debe utilizar slices.

2. Escriba una función que le permita reconocer si una frase es palíndrome (se deben ignorar los espacios, signos de puntuación y mayúsculas o minúsculas). Por ejemplo, "Anita lava la tina" es una frase palíndrome. *Ayuda*: el módulo `string` declara el valor `ascii_letters` que podría serle de utilidad. Eliminar los caracteres que no le sirvan probablemente requerirá de un ciclo.

3. Escriba una función que utilice *slices* para extraer las palabras que están en las posiciones impares de una frase. Por ejemplo, si se aplicara la función a la primera frase de este enunciado el resultado debería ser: `['Escriba', 'función', 'utilice', 'para', 'las', 'que', 'en', 'posiciones', 'de', 'frase']`.

4. Escriba una función que extraiga la primera palabra de una frase (hasta el primer espacio).

5. Escriba una función que extraiga la última frase de un párrafo (desde el último punto).

6. Escriba una función que calcule los números primos hasta un cierto límite utilizando el algoritmo conocido como la Criba de Eratóstenes. El principio fundamental de este algoritmo es que una vez se sabe que un número es primo, ninguno de los múltiplos de ese número va a ser un número primo así que no es necesario verificar nada sobre ellos. La modificación de listas con *slices* es particularmente útil para solucionar este problema. *Ayuda:* Recuerde que las listas se pueden construir usando repeticiones (ej: `[False]*50`).



## Más allá de Python

Otros lenguajes, como Julia o Go, ofrecen capacidades similares a las que ofrece Python para hacer *slicing*. Sin embargo, al no ser una característica particularmente difundida, es importante tener la capacidad para escribir los algoritmos equivalentes.
 


