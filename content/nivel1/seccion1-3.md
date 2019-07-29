Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Valores y tipos de datos

> El objetivo de esta sección es introducir y discutir los conceptos de  *valor*, *literal*, y *tipo de datos*. Trabajaremos además con los tipos básicos *int*, *str* y *float* de Python.

La razón de ser de cualquier programa es poder trabajar con valores. Estos valores sirven para representar cosas que existan en una realidad, como por ejemplo la temperatura en una ciudad, la cantidad de dinero en una cuenta, el nombre de una persona, o la fecha actual. Algunas veces, los valores se expresan como el resultado de una *operación* (ej. 1 + 2.22) mientras que otras veces se describen de forma directa usando un *literal* (ej. 3.22). 

La naturaleza de los valores hace necesario separarlos en categorías porque en muchos casos no tiene sentido operarlos entre ellos. Por ejemplo, si sabemos que vamos a hacer una multiplicación, no tiene sentido que mezclemos números y palabras. Estas categorías que se usan para separar los valores usualmente reciben el nombre de *tipos*.

Python ofrece mecanismos para representar, interpretar y hacer operaciones sobre valores de varios tipos. Los más importantes son los que vamos a estudiar en esta sección: números enteros (int), números decimales (float) y cadenas de caracteres (st).

Adicionalmente, Python ofrece la función ```type``` que nos permite consultar de qué tipo es un determinado valor. Usaremos ahora esta función en tres ejemplos muy sencillos para introducir lo que se va a presentar en el resto de la sección y para observar el funcionamiento de la función misma:

```python
>>> type(9)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type('Hola')
<class 'str'>
```


## Números enteros (int)

El primer tipo que vamos a estudiar es el que nos permite representar números enteros, positivos y negativos, y que en Python recibe el nombre de ```int```.

En general, los números enteros se describen usando los literales a los que estamos acostumbrados: 0, 1, 2, 3, ... y -1, -2, -3, etc. A diferencia de otros lenguajes, en Python no hay límites sobre los números enteros, así que cualquier número debería poder representarse sin problema [^bases].


## Números decimales (float)

Como complemento al tipo ```int```, Python también ofrece el tipo ```float``` que permite representar números con decimales. Es importante notar que, debido a restricciones técnicas, Python frecuentemente tiene que redondear números decimales. A manera de ejemplo, consideremos el resultado de hacer la división ```10/3``` que resulta en ```3.3333333333333335``` en lugar del resultado irracional.

En Python, los literales para representar números decimales utilizan un punto como separador. Es decir que los siguientes son todos números de tipo float: 0.0, -1.1, 2.33, -4.5555557.


## Cadenas de caracteres (str)

Cadenas de caracteres

'
'''
"

\n



#### Notas

[^bases]: Por defecto, los literales de números enteros asumen que se trata de números en base 10. Sin embargo, si se preceden los números con los caracteres '0b' o '0x' significaría que se trata de números binarios o hexadecimales, respectivamente. Por ejemplo, los tres literales 0b10110, 0x16 y 22 representarían el mismo valor (el número 22 en base 10).