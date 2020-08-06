
# Errores frecuentes

```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```

En esta sección presentamos algunos de los errores que encontramos frecuentemente en los programas de muchos estudiantes. Revíselos con cuidado y asegúrese de entenderlos para no cometer esos mismos errores


## Confundir los nombres de las variables con los nombres de las llaves en un diccionario

Si utilizamos una variable para indicar una llave en un diccionario, lo único que nos interesa es el valor asociado a la variable y no el nombre utilizado para la variable. Frecuentemente se encuentran confusiones como las del siguiente programa:

```{code-block} python
---
lineno-start: 1
---
diccionario = {"llave": 1, "mensaje": 2}
llave = "mensaje"
mensaje = diccionario[llave]
print(diccionario[mensaje])
```

En la línea 1, se crea un nuevo diccionario con dos llaves de tipo `str`: `"llave"` y `"mensaje"`. En la línea 2 se crea una variable llamda `llave` cuyo valor es la cadena `"mensaje"`.

En la línea 3 se extrae el valor asociado a la llave almacenada en la variable `llave`. La llave es la cadena `"mensaje"`, así que del diccionario se extrae el valor `1` y se almacena en la variable `mensaje`.

En la línea 4 se intenta extraer el valor asociado a la llave almacenada en la variable `mensaje`. Sin embargo, el valor asociado es el entero `1` y, como esa llave no existe en el diccionario, se produce un error.


## Intentar extraer una llave que no existe

Intentar extraer el valor asociado a una llave de un diccionario producirá un error cuando la llave no exista. Las dos formas posibles de evitar esta situación son:

1. Preguntar si la llave existe, usando el operador `in`, antes de intentar el valor.

2. Utilizar el método `get` para no producir el error y obtener en cambio un valor por defecto si la llave no existe en el diccionario.


## Reemplazar un valor por accidente

Como en Python se usa la misma sintaxis para asignarle un valor a una llave en un diccionario y para *actualizar* el valor, es fácil reemplazar un valor por accidente. La principal forma de evitar este problema es averiguar si el valor ya existía antes de hacer la modificación utilizando el operador `in`.

Consideremos por ejemplo el siguiente programa donde la función `incrementar_contadores` se utiliza para construir un histograma de valores:

```python
def incrementar_contadores(histograma: dict, valor: str) -> None:
    histograma[valor] = 1
```

Esta función siempre le asociará el valor `1` a la llave. En realidad se debería haber preguntado si la llave existía antes de hacer la modificación:

```python
def incrementar_contadores(histograma: dict, valor: str) -> None:
    if valor in histograma:
        histograma[valor] += 1
    else:
        histograma[valor] = 1
```
Otra solución posible se podría construir usando el método `get`:
```python
def incrementar_contadores(histograma: dict, valor: str) -> None:
    histograma[valor] = histograma.get(valor, 0) + 1
```


## Modificar un diccionario dentro de una función

Cuando se use un diccionario como parámetro de una función, el cuerpo de la función tendrá acceso al diccionario a través del parámetro. Si el diccionario se modifica dentro de la función, estos cambios serán visibles para quien haya hecho la invocación de la función.

Observemos un ejemplo:

```python
def funcion(histograma: dict) -> None:
    histograma.clear()
    histograma["llave_inicial"] = 0
```

La función mostrada producirá el siguiente efecto sobre cualquier diccionario que se use como parámetro en una invocación a la función:

1. Eliminará todos los elementos del diccionario
2. Le asignará el valor `0` a la llave `"llave_inicial"`.



## Reemplazar un diccionario dentro de la función 

Cuando se use un diccionario como parámetro de una función, el cuerpo de la función tendrá acceso al diccionario a través del parámetro. Sin embargo, si se modifica el parámetro reemplazándolo por un nuevo diccionario, el diccionario que se pasó como parámetro no se verá afectado.

Observemos un ejemplo:

```python
def funcion(histograma: dict) -> None:
    histograma = {"llave_inicial": 0}
```

En esta función se recibe un diccionario como parámetro, posiblemente inicializado con algunos valores. En la única línea del cuerpo de la función, se crea un nuevo diccionario y se asocia al identificador `histograma`. Aunque parece que estamos reemplazando el valor del parámetro, en realidad estamos creando una nueva variable con el mismo nombre que el parámetro y le estamos asociando como valor un nuevo diccionario.

El diccionario original que se haya usado al invocar la función no se verá afectado de ninguna manera por esta función.

## Copias superficiales vs. copias profundas

Cuando se usa el método `copy` de un diccionario, se hace una copia *superficial* en lugar de una copia *profunda*: si el diccionario contenía valores que no fueran valores numéricos (`int`, `float`), booleanos (`bool`) o cadenas (`str`), la copia del diccionario incluirá referencias a los valores originales.

Por ejemplo, si teníamos un diccionario dentro de un diccionario y copiamos el diccionario contenedor, obtendremos un nuevo diccionario contenedor con dentro el mismo diccionario que tenía el contenedor original.


# Para no olvidar

* **Use el operador `in` para saber si una llave existe en un diccionario.** Es mucho mejor revisar si una llave existe antes de intentar extraerla, que intentar sacar el valor con la llave y obtener un error.

* **Use el método `get` para obtener un valor por defecto cuando no exista una llave.** Si tiene sentido obtener un valor por defecto, use `get` para extraer un valor de un diccionario.

* **Los diccionarios pueden usarse como histogramas.** Debido a su eficiencia para encontrar un valor asociado a una llave, los diccionarios son muy útiles para construir histogramas. Además, el uso del método `get` hace que la construcción de un histograma sea muy sencilla.

* **Cuando se usen en los parámetros de una función, los diccionarios se pasan por referencia y son mutables.** Por este motivo, los cambios que se hagan al diccionario desde adentro de la función serán visibles para el que hizo la invocación.

* **El método `copy` crea una copia de un diccionario.** Sin embargo debe tener cuidado: será una copy *superficial*.


