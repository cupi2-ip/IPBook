Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Definición de funciones

En la sección anterior definimos el concepto de función y lo ilustramos con varias funciones básicas del lenguaje Python. Como parte de esto, también se mostraron varios ejemplos de invocaciones a estas funciones y se presentaron las principales reglas para la evaluación de funciones. Esta sección completa la discusión sobre funciones en Python explicando cómo se pueden definir nuevas funciones.

Para empezar, presentamos un programa completo que al final de esta sección usted debería ser capaz de explicar y reconstruir. Léalo con cuidado, teniendo en que cuenta que cuando se habla de "una casa" se hace referencia a un dibujo como el siguiente:

![](./images/casita.png)

```python
def area_cuadrado(lado: int)-> int:
    """
       Calcula el área de un cuadrado dada la medida de su lado
    """
    return lado * lado


def area_triangulo(base: int, altura: int)-> float:
    """
        Calcula el área de un triángulo dada la medida de la base y de la altura.
    """   
    return (base * altura) / 2


def area_casa(frente: int, techo: int)-> float:
    """
        Calcula el área del dibujo de una casa que se forma con un cuadrado
        y un triángulo encima (el techo).
        El frente de la casa será igual al lado del cuadrado y a la base del triángulo.
        La altura del techo será la altura del triángulo.
    """
    cuadrado = area_cuadrado(frente)
    triangulo = area_triangulo(frente, techo)
    return cuadrado + triangulo
    
medida_frente = 7
medida_techo = 5
resultado = area_casa(medida_frente, medida_techo)
print("El área de una casa con", medida_frente, "metros de frente y un techo de",
       medida_techo, "metros de alto es ", round(resultado, 2), "metros")
```

Como siempre, no se preocupe si hay cosas en el programa anterior que no haya entendido: todo se irá aclarando a lo largo de la sección.


## Definición de funciones en Python

En la sección anterior vimos que Python incluye varias funciones que nosotros podemos utilizar aunque no sepamos cuáles sean exactamente las instrucciones que ejecuta cada una. Lo que conocemos nosotros de esas funciones es lo que llamamos *signatura*, la cual incluye el nombre, los parámetros que espera y su retorno. Lo que desconocemos es el *cuerpo* o *implementación* de las funciones, es decir las instrucciones que hacen que la función cumpla con lo que se espera de ella.

### La signatura de una función

La signatura de una función puede verse como la especificación de las reglas para utilizar la función y está compuesta por tres cosas:

1. **El nombre**. Este debería ser un nombre claro y fácil de recordar. Además no debería estar repetido para que no haya ambigüedad cuando se quiera invocar a la función.

2. **Los parámetros**. Estos son los valores que se le tienen que pasar a la función cuando se quiera invocar. Pueden verse como la información que tiene que proporcionar quien llame a la función para que se pueda cumplir con su objetivo. Una función puede tener uno o varios parámetros.

3. **El resultado**. En tercer lugar tenemos información sobre el resultado de la función que nos dice si será un número, una cadena de caracteres o cualquier otra cosa.

Volvamos ahora al ejemplo para identificar estos elementos:

```python
def area_cuadrado(lado: int)-> int:
    """
       Calcula el área de un cuadrado dada la medida de su lado
    """
    return lado * lado
```

En este ejemplo, se está definiendo una función y se ha incluido tanto la signatura como el cuerpo. Por ahora vamos a analizar sólo la signatura, que en este caso corresponde a la primera línea del ejemplo. 

Lo primero que nos encontramos es la palabra reservada[^reservada] de Python ```def``` que nos marca el inicio de la definición de una función. La signatura de la función va hasta los dos puntos (```:```) que se encuentran al final de la línea.

Después de la palabra ```def```, viene el nombre que le queremos dar a la función. En este caso escogimos ```area_cuadrado``` para expresar claramente su objetivo: será una función para calcular el área de un cuadrado. Como los nombres de las funciones no pueden tener espacios, hemos separado las dos palabras usando el símbolo ```_```[^estilo]. 


[^reservada]: Una palabra reservada significa que es una palabra que nosotros no podemos usar en nuestros programas para nuestros identificadores. Por ejemplo, no podemos tener ni una función ni una variable que se llamen ```def```. Python tiene varias palabras reservadas que iremos descubriendo, como return, del, import, pass, y raise, entre otras.

[^estilo]: La regla que acabamos de ilustrar (separar palabras usando el símbolo ```_```) no es una regla sintáctica del lenguaje, sino es una regla de *estilo*. Es decir, nosotros podríamos haber llamado a la función ```areaCuadrado``` y el programa habría funcionado igual, pero no habría respetado las reglas de estilo que sirven para hacer los programas más legibles y consistentes. Si usted ha utilizado algún otro lenguaje de programación, es posible que el estilo al que esté acostumbrado le sugiera usar nombres como ```areaCuadrado``` o ```AreaCuadrado```.



Definición de parámetros

El tipo de retorno

### El cuerpo de una función

indent

La instrucción return

Variables locales



## Definir vs. Invocar


nombres de parámetros vs. argumentos

llamar funciones desde funciones

usar funciones en los argumentos de invocaciones



## Documentación de funciones



## Funciones sin parámetro o sin retorno





## Sobre los *type-hints*



## Ejercicios

1. 


## Más allá de Python

Contexto de ejecución: sólo los parámetros

Tipos de parámetros y funciones - dynamic typing vs. strong typing

Camel Case



#### Notas 