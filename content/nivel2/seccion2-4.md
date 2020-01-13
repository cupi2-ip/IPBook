Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Instrucciones condicionales

> El objetivo de esta sección es introducir las instrucciones condicionales, mostrando por qué son necesarias, qué significan y cómo pueden utilizarse en Python. 

Entre el nivel 1 y lo que llevamos hasta este momento del nivel 2, hemos estudiado tipos de datos (int, str, float, bool), operadores (aritméticos, sobre cadenas, lógicos), expresiones y variables, y un conjunto reducido de instrucciones que nos permiten:

* Asignarle un valor a una variable
* Definir una nueva función
* Invocar una función con unos argumentos
* Retornar un valor al terminar una función
* Importar un módulo existente

Aunque no parece mucho, este reducido conjunto de elementos son la base para construir cualquier tipo de programas. En esta sección vamos a introducir un nuevo tipo de instrucción, los condicionales, con el cual incrementaremos enormemente el potencial de problemas que podemos solucionar y de programas que podemos construir.

## Motivación

La gran limitación que tienen los programas que podemos construir hasta el momento es que siempre van a ejecutar las mismas instrucciones. Esto implica que no pueden tomar ninguna decisión y que incluso funcionalidades pequeñas son imposibles de implementar.

Tomemos como ejemplo la funcionalidad de verificar si la contraseña introducida por un usuario es correcta o no: si es correcta, quisiéramos informarle al usuario que sí es correcta; si no es correcta, quisiéramos decirle que no es correcta y que debe volver a intentarlo. En la sección anterior aprendimos a comparar cadenas de caracteres, así que ya podríamos saber si la contraseña es correcta o no:

```python
contrasena_correcta = contrasena_almacenada == contrasena_ingresada
```
Lo que no podemos hacer, sin usar instrucciones condicionales, es *calcular* el mensaje correcto para mostrarle al usuario con base en el valor de ```contrasena_correcta```.

Consideremos ahora otro ejemplo en el que queremos calcular el valor de una factura:

```python
valor_producto = 14000
impuestos = valor_producto * 0.19
valor_factura = valor_producto + impuestos
```

¿Qué pasa si no todos los productos tienen que pagar impuestos? ¿Qué pasa si el porcentaje de impuestos es diferente dependiendo del valor del producto (ej. 19% para productos de más de 10000 y 10% para productos de menos)? Para lograr representar estas situaciones también necesitamos usar instrucciones condicionales.

Cuando una persona recorre un camino, es usual que llegue a un punto en el que tiene que detenerse, analizar algo y tomar una decisión sobre qué camino seguir. Eso es precisamente lo que nos van a permitir modelar las instrucciones condicionales: marcar un punto en el programa en el que se tiene que evaluar una condición y continuar por un camino dependiendo del resultado de la evaluación.

![](./images/crossroads.png)


## Condicionales en Python: IF-ELSE

Una instrucción condicional es una instrucción cuya ejecución depende del valor que resulte de evaluar una expresión booleana. Esta evaluación se hace durante la ejecución de un programa, así que cuando estamos programando nosotros no podemos saber a ciencia cierta qué es lo que va a ejecutarse. Además, ejecuciones sucesivas del mismo programa no necesariamente van a comportarse de la misma manera.

En Python, las instrucciones condicionales se usan utilizando la siguiente estructura:

```python
if expresion_booleana:
    cuerpo_if
else:
    cuerpo_else
```

* **expresion_booleana**: es una expresión que tiene que tener un valor de verdad (una operación relacional, una variable booleana, un llamado a una función booleana, etc.). Note los dos puntos (**:**) al final de la expresión.
* **cuerpo_if**: son las instrucciones que se van a ejecutar si la expresión booleana es verdadera en el momento de la evaluación. El cuerpo del IF debe ir indentado como el cuerpo de una función.
* **cuerpo_else**: son las instrucciones que se van a ejecutar si la expresión booleana es falsa en el momento de la evaluación. El cuerpo del ELSE también debe ir indentado.

Veamos ahora cómo podemos usar esta estructura usando el ejemplo de la verificación de contraseña:

```python
contrasena_almacenada = "secreto"
contrasena_ingresada = input("Ingrese su contraseña:")

if contrasena_almacenada == contrasena_ingresada:
    mensaje = "Su contraseña es correcta"
else:
    mensaje = "La contraseña es incorrecta"

print(mensaje)
```

En primer lugar, tenemos que notar que este programa tiene sólo cuatro instrucciones: 1. una asignación, 2. un llamado a una función (input), 3. una instrucción condicional y 4. una invocación a una función (print). Como veremos, la instrucción condicional tiene varios elementos por dentro, pero deberíamos considerarla una sola instrucción.

En la primera instrucción se hace una asignación y se almacena en una variable la cadena ```'secreto'``` para que ese sea la contraseña contra la que se va a hacer la verificación.

En la segunda instrucción se hace una invocación a la función ```input``` y se espera a que el usuario ingrese un valor. Ese valor se almacena en la variable ```contrasena_ingresada``` pero nosotros no lo conocemos, así que no podemos saber si es el valor correcto o no.

La siguiente instrucción en el programa es el ```if``` con todos sus elementos. En primer lugar, Python verifica el valor de la expresión booleana para ver cuál es la siguiente instrucción que tendrá que ejecutar. En este caso la expresión es ```contrasena_almacenda == contrasena_ingresada``` y tiene un valor que nosotros no podemos conocer porque depende de lo que escriba el usuario cada vez que se ejecute el programa. Lo que sí sabemos es que si el valor es verdadero se ejecutará el *cuerpo del if* y que si es falso se ejecutará el *cuerpo del else*.

El *cuerpo del if* en este caso sólo tiene una instrucción que hace una asignación a la variable mensaje con un valor que indique una autenticación exitosa. El *cuerpo del else* también tiene sólo una asignación, pero esta vez deja un mensaje fallido. Estos dos bloques de código (el cuerpo del if y el cuerpo del else) son muy sencillos en este caso, pero podrían ser tan complicados como se quisiera: dentro de ellos puede haber casi cualquier cosa que pueda estar dentro de un programa, incluyendo asignaciones, llamados de funciones y otros condicionales [^poder].

Un aspecto muy importante para tener en cuenta acá es la **indentación**: así como cuando definimos una función tenemos que indentar el cuerpo de la función, cuando usamos instrucciones condicionales el cuerpo del if y el cuerpo del else tienen que estar consistentemente indentados.

Cuando se termine de ejecutar bien sea el cuerpo del if o el cuerpo del else, se considerará que la instrucción condicional terminó de ejecutarse y Python podrá pasar a la siguiente instrucción, que en este imprime el mensaje para el usuario.

### Alternativas

Veamos ahora otras dos maneras en las que habríamos podido escribir el mismo programa.

En la primera alternativa vamos a extraer la instrucción condicional y convertirla en una función que calcule el mensaje.

```python
def revisar(contrasena_almacenada: str, contrasena_ingresada: str)->str:
    contrasena_correcta = contrasena_almacenada == contrasena_ingresada
    
    if contrasena_correcta:
        mensaje = "Su contraseña es correcta"
    else:
        mensaje = "La contraseña es incorrecta"
    return mensaje

contrasena_almacenada = "secreto"
contrasena_ingresada = input("Ingrese su contraseña:")
mensaje = revisar(contrasena_almacenda, contrasena_ingresada)
print(mensaje)
```

Este pequeño cambio hace mucho más evidente lo que dijimos antes: la instrucción condicional, aunque tuviera varios elementos por dentro, era fundamentalmente sólo una instrucción que calculaba el valor de la variable ```mensaje```.

Esta nueva versión también tiene un cambio con respecto a la expresión condicional: la comparación no se hace ahora dentro del if sino que se hace antes y su resultado se almacena en una variable. Aunque funcionalmente es equivalente, es posible que esta versión sea un poco más legible y haga que la instrucción condicional sea más fácil de entender. En ejercicios más avanzados, en los que las condiciones son mucho más largas y complejas, es recomendable aplicar esta técnica para simplificar el código y disminuir la posibilidad de introducir errores.

La siguiente es la segunda alternativa al código original: en este caso no hay una función adicional pero tampoco hay un ```else```.

```python
contrasena_almacenada = "secreto"
contrasena_ingresada = input("Ingrese su contraseña:")

mensaje = "La contraseña es incorrecta"
if contrasena_almacenada == contrasena_ingresada:
    mensaje = "Su contraseña es correcta"

print(mensaje)
```

Como se ve en este programa, no es obligatorio que cada instrucción condicional tenga un bloque ```else```: sólo el bloque ```if``` tiene que existir siempre en una instrucción condicional. En estos casos, la condición sirve para saber si un bloque de instrucciones tiene que ejecutarse o no. 

Volviendo a nuestro ejemplo, el bloque condicional revisa que la contraseña sea correcta y, en caso afirmativo, le asigna a la variable ```mensaje``` la cadena que informa del éxito en la autenticación. Como en este caso la variable ```mensaje``` siempre tiene que tener un valor, bien sea exitoso o no, tuvimos que asignarle un valor inicial antes de llegar a la instrucción condicional. Si no lo hubiéramos hecho, la variable ```mensaje``` no existiría cuando el usuario pusiera la contraseña equivocada y nuestro programa habría fallado al momento de intentar imprimir el mensaje:

```
NameError: name 'mensaje' is not defined
```

[^poder]: En realidad, también puede haber cosas que es poco usual encontrar dentro de un condicional, como declaración de funciones y llamados para importar módulos. No es muy recomendable usar estas capacidades a menos que haya motivos muy bien justificados para hacerlo.


### Ejercicios

1. Queremos escribir una función que nos diga quién ganará en el lanzamiento de una moneda. Escriba una función que reciba el nombre de la persona que pidió 'cara', el nombre de la persona que pidió 'sello' y el resultado del lanzamiento ('cara' o 'sello') y responda con el nombre de la persona que haya acertado.




## Condicionales en Python: IF-ELIF-ELSE

Vimos ya que una instrucción condicional puede tener una pareja de bloques if y else, o puede tener sólo un bloque if. Ahora agregaremos la posibilidad de tener más de una condición, para lo cual tenemos que introducir los bloques que en Python se llaman ```elif``` y que en muchos otros lenguajes se conocen como **else if**. 

Veamos un ejemplo de una instrucción que incluya varias condiciones. Suponga que las funciones `longitud`, `tiene_numeros`, `tiene_minusculas`, `tiene_mayusculas` y `cambiar_contrasena` ya están definidas en alguna otra parte del programa. El bloque condicional empieza con la palabra reservada `if` y una condición; de ahí en adelante, cada condición se acompaña de la palabra reservada `elif`. Al final encontramos un bloque ELSE que, como todos los bloques ELSE que hemos estudiado, incluye la palabra `else` pero no tiene una condición asociada.

```python
nueva = input("Introduzca su nueva contraseña:")

if longitud(nueva) < 8:
    mensaje = "La nueva contraseña debe tener al menos 8 caracteres"
    
elif nueva == contrasena_anterior:
    mensaje = "La nueva contraseña no puede ser igual a la anterior"

elif nueva.isalnum():
    mensaje = "La nueva contraseña debe tener signos de puntuación"
    
elif not tiene_numeros(nueva):
    mensaje = "La nueva contraseña debe tener al menos un número"

elif not tiene_mayusculas(nueva):
    mensaje = "La nueva contraseña debe tener al menos una letra mayúscula"

elif not tiene_minúsculas(nueva):
    mensaje = "La nueva contraseña debe tener al menos una letra minúscula"

else:
    cambiar_contrasena(nueva)
    mensaje = "La contraseña se cambió exitosamente"

print(mensaje)
```

En este programa lo que tenemos es una sola instrucción condicional que incluye la evaluación de varias condiciones. La primera condición que se evalúa es la que tiene que ver con la longitud de la cadena (`longitud(nueva) < 8`) para ver si se ejecuta el primer cuerpo o no. Si la condición es falsa, se pasa a revisar la segunda condición. Lo interesante es si la condición es verdadera, porque entonces se ejecuta el cuerpo del IF y se pasa a la siguiente instrucción del programa. Es decir que se pasa a imprimir el mensaje.

Esto es muy importante y debe quedar muy claro: cuando se encuentra una condición verdadera, se ejecuta el cuerpo asociado a la condición y se termina la ejecución del condicional sin importar si más adelante había otras condiciones que también fueran verdaderas.

La implicación de esto para nuestro programa es que el mensaje que le vamos a mostrar al usuario es el mensaje que corresponda al primer error que hayamos encontrado. Por ejemplo, si la nueva contraseña no tenía signos de puntuación y no tenía números, el usuario sólo se enterará del primer problema. 

Finalmente, analicemos las estructuras de los siguientes condicionales. En el primer condicional, usaremos bloques ELIF.

```python
if cond1:
    bloque1()
elif cond2:
    bloque2()
elif cond3:
    bloque3()
else:
    bloque_else()
```
Ahora veamos una estructura equivalente pero que no utiliza bloques ELIF.

```python
if cond1:
    bloque1()
if not cond1 and cond2:
    bloque2()
if not cond1 and not cond2 and cond3:
    bloque3()
if not cond1 and not cond2 and not cond3:
    bloque_else()
```
En este segundo caso se remplazaron los bloques ELIF por bloques IF y se volvieron mucho más complejas las condiciones. Por ejemplo, en la primera estructura el llamado `bloque2()` sólo se podía ejecutar si la condición `cond1` no había sido verdadera y si la condición `cond2` sí lo había sido. En la segunda estructura encontramos exactamente las mismas condiciones, pero de una manera mucho más explícita que se va complicando progresivamente. 

Esto nos demuestra la ventaja que nos trae utilizar bloques ELIF para ayudar a simplificar y hacer más comprensible el código.


### Condicionales consecutivos

Suponga ahora que queremos cambiar nuestro programa para que al usuario no se le informe sólo el primer problema que se encuentre con su nueva contraseña, sino que se le digan de una vez todos los problemas que tenga. En este caso la estructura basada en IF-ELIF-ELSE ya no nos sirve porque necesitamos que *siempre* se verifiquen *todas* las condiciones.

Para lograr que esto pase, lo único que podemos hacer es separar las condiciones en instrucciones diferentes, asegurando así que todas sean verificadas. Es decir que, en lugar de tener un IF seguido de varios ELIF, en los cuales sólo 1 condición puede ser cierta a la vez, vamos a tener varios IF totalmente desconectados. Observe esto en la siguiente versión de nuestro programa:

```python
nueva = input("Introduzca su nueva contraseña:")
contrasena_correcta = True
mensaje = ""

if longitud(nueva) < 8:
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos 8 caracteres" + "\n"
    
if nueva == contrasena_anterior:
    contrasena_correcta = False
    mensaje += "La nueva contraseña no puede ser igual a la anterior" + "\n"

if nueva.isalnum():
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener signos de puntuación" + "\n"
    
if not tiene_numeros(nueva):
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos un número" + "\n"

if not tiene_mayusculas(nueva):
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos una letra mayúscula" + "\n"

if not tiene_minúsculas(nueva):
    contrasena_correcta = False
    mensaje += "La nueva contraseña debe tener al menos una letra minúscula" + "\n"

if contrasena_correcta:
    cambiar_contrasena(nueva)
    mensaje = "La contraseña se cambió exitosamente"

print(mensaje)
```

Si seguimos la traza de ejecución de este programa veremos que, después de que se ejecuten las primeras tres asignaciones, Python revisará la condición del primer IF: si es verdadera se ejecutará el cuerpo y se pasará a la siguiente instrucción; si es falsa, se pasará a la siguiente instrucción sin ejecutar nada mas. En este caso, la siguiente instrucción será el segundo IF que se evaluará sin tener en cuenta el valor de la condición del primer IF. Es decir que estamos hablando de instrucciones condicionales completamente independientes la una de la otra. Este mismo proceso se repetirá para cada una de las instrucciones siguientes.

Ahora bien, sabemos que la función `cambiar_contrasena` sólo debe ejecutarse si la nueva contraseña cumple con todos los requisitos de forma que se revisaron en las condiciones anteriores. Si le asignáramos a esas condiciones los nombres P, Q, R, S, T y U, entonces el último bloque IF tendría que escribirse de la siguiente manera:

```python
if not(P or Q or R or S or T or U):
    cambiar_contrasena(nueva)
    mensaje = "La contraseña se cambió exitosamente"
```

Esta condición no es muy fácil de leer porque los nombres de variables no son explícitos, pero si pusiéramos nombres más claros terminaríamos con una expresión muy larga y también difícil de leer. También podríamos haber escrito las expresiones originales, pero eso significaría que cada una la evaluaríamos dos veces: una vez en el IF que la verifique y otra vez en el IF para cambiar la contraseña.

Por estas razones, en nuestro programa decidimos incluir una nueva variable llamada `contrasena_correcta`: cuando inicia el programa suponemos que la nueva contraseña que ingresó el usuario cumple con todas las restricciones, así que inicializamos la variable en el valor `True`. Luego, en cada una de las instrucciones condicionales cambiamos el valor de la variable a falso si descubrimos que la nueva contraseña no cumple alguna de las restricciones.

Como sabemos que si la nueva contraseña no cumple con *al menos una* de las reglas entonces no debemos hacer el cambio, en el último IF basta con revisar el valor de la variable `contrasena_correcta`: si tiene valor verdadero significa que no se encontró ningún problema con la nueva contraseña; si tiene valor falso significa que se encontró *al menos* un problema la nueva contraseña.

El último aspecto para revisar de este programa es el que tiene que ver con el mensaje. Cuando se inicia la ejecución tenemos un mensaje vacío. Luego, cada vez que se encuentra que no se cumple con una restricción se *concatena* un nuevo mensaje al mensaje que se tenía. Esto quiere decir, por ejemplo, que si no se cumple con ninguna de las restricciones entonces la variable `mensaje` tendrá la información de todas las restricciones que no se cumplieron.

Note que en el último IF, el que cambia la contraseña si no hubo ningún problema, no se concatena nada al mensaje, sino que se reemplaza por un mensaje de éxito.

**Recuerde**: un `elif` depende del `if` anterior mientras que un `if` es independiente de lo que haya pasado antes.

### Ejercicios

1. Modifique el programa que cambia la contraseña para que en caso de que no se pueda cambiar la contraseña se le informe al usuario no sólo las restricciones que no se cumplieron sino también las condiciones que sí se cumplieron.

2. El valor de un peaje depende del tipo de vehículo (categoría) que pase y de la cantidad de ejes que tenga: automóviles, camionetas y camperos (AUTO) deben pagar 10000; buses y busetas (BUS), 14300; camiones grandes de 2 ejes (CAMION), 16000; camiones de 3 y 4 ejes (CAMION), 28100; camiones de 5 ejes (CAMION), 37700; y camiones de 6 o más ejes (CAMION) deben pagar 41400. Adicionalmente, un vehículo podría tener un descuento especial del 15% por paso frecuente. Escriba una función que reciba el tipo de un vehículo ('AUTO', 'BUS' o 'CAMION') y si tiene descuento especial y calcule el valor que debe pagar en el peaje.


## Aspectos metodológicos

Como hemos visto con algunos de los ejemplos anteriores, usualmente el mismo problema puede resolverse correctamente usando estructuras diferentes. A continuación exploramos cuatro formas de resolver el mismo problema: queremos saber si un número es positivo y además es menor de 10.


### Condicionales anidados 

El siguiente bloque muestra la definición de una función que resuelve el problema utilizando condicionales anidados:

```python
def es_positivo_de_un_solo_digito_v1(x: int)->bool:
   if x > 0:
       if x < 10:
           return True
       else:
           return False
   else:
       return False
```

Llamamos condicional anidado a la situación en la cual hay una instrucción condicional dentro del cuerpo de otra instrucción condicional. 

En el caso de nuestro ejemplo, lo que se hizo en este ejemplo fue analizar por partes el problema. En primer lugar se decidió que, si el número es positivo, entonces se debe revisar la segunda condición. Esta revisión quedó entonces anidada en un condicional dentro del cuerpo del primer if. Por otra parte, si el número es negativo no hay necesidad de revisar la segunda condición y se puede retornar False inmediatamente.

Sin embargo, este ejemplo podría simplificarse un poco si se analizan las condiciones que llevan al único caso en que se retorna `True` en esta función: para que se pueda llegar a este punto es necesario que las dos condiciones sean verdaderas simultáneamente, es decir que `x > 0` *y* `x < 10`. En todos los otros casos, la función debería retornar `False`. 

Si llevamos eso en al código llegamos a la segunda versión de la función:

```python
def es_positivo_de_un_solo_digito_v2(x: int)->bool:
   if x > 0 and x < 10:
       return True
   else:
       return False
```

No se puede decir ni que el uso de condicionales anidados sea una mala idea ni que armar expresiones condicionales más completas sea una buena idea. De hecho, siguiendo esta estrategia es muy fácil terminar con estructuras muy difíciles de entender y, por ende, de mantener, extender y corregir cuando tengan problemas.

Como siempre, mantener la claridad del código debería ser una prioridad para tomar decisiones con respecto a su estructura.


### Returns

A pesar de sus diferencias, los dos ejemplos anteriores coinciden en un aspecto: tan pronto encuentran la respuesta, retornan verdadero o falso y terminan la ejecución de la función. Aunque esto no está necesariamente mal, una práctica que suele hacer el código más fácil de entender y por ende mucho más mantenible, es limitar la cantidad de puntos en los cuales se utilice la instrucción `return`. Por ejemplo, la última versión de la función puede remplazarse por la siguiente versión remplazando los `return` por asignaciones a una variable y dejando sólo un `return` al final de la función.

```python
def es_positivo_de_un_solo_digito_v3(x: int)->bool:
   resultado = False
   if x > 0 and x < 10:
       resultado = True
       
   return resultado
```
En esta función tan pequeña no es fácil apreciar que esta nueva versión es mucho más fácil de mantener que la versión anterior. Sin embargo, nuestra recomendación es que minimice la cantidad de puntos en los cuales usted retorne un valor desde una función.

### Expresiones vs. condicionales

En varios casos, incluyendo el que hemos estado trabajando, existen formas de remplazar las instrucciones condicionales por expresiones booleanas. Eso es lo que hemos hecho en la cuarta y última versión de la función: en lugar de calcular un resultado y luego retornarlo, acá el valor mismo de la expresión es el retorno de la función.

```python
def es_positivo_de_un_solo_digito_v4(x: int)->bool:
   return x > 0 and x < 10
```
Esta estrategia funciona muy bien cuando las condiciones son fáciles de leer y entender. Cuando las condiciones son mucho más complicadas probablemente sea mejor tener la estructura de las instrucciones condicionales, incluso si son anidadas, para ayudar a quien lea el código a entender su propósito.


## Caso de estudio: el mayor de 4 números

En esta sección vamos a estudiar un problema recurrente y muy importante que debe resolverse utilizando instrucciones condicionales, pero puede resolverse de maneras diferentes. Empezaremos planteándole el problema para que usted lo resuelva y luego pasaremos a discutir nuestras alternativas de solución. Esperamos que usted vaya comparando nuestras soluciones con la suya.

### Enunciado del problema

Escriba una función que reciba por parámetro cuatro números enteros y devuelva el mayor de estos. Si hay dos o más iguales y mayores, retorna cualquiera de estos. La signatura de la función debe ser:

```python
def mayor(a: int, b: int, c:int, d:int)->int:
```
Escriba su solución y compárela con las que nosotros proponemos a continuación.

### Solución 1: múltiples returns

La primera solución es la solución que es más natural para este problema: si nos damos cuenta que el valor `a` es mayor al valor `b` y es mayor al valor `c` y es mayor al valor `d`, entonces tiene que se que `a` es el mayor valor. Algo similar se hace con los otros parámetros.

```python
def mayor(a: int, b: int, c:int, d:int)->int:
    if (a >= b) and (a >= c) and (a >= d):
        return a
    elif (b >= a) and (b >= c) and (b >= d):
        return b
    elif (c >= 1) and (c >= b) and (c >= d):
        return c
    else:
        return d        
```

El problema con esta solución es que requiere mucho cuidado en su elaboración: es fácil tanto intercambiar dos variables como olvidar hacer una de las comparaciones. Esta solución además tiene como limitante que agregar un nuevo elemento para calificar requiere modificaciones sobre prácticamente toda la función.


### Solución 2: un solo return

La segunda solución no dista mucho de la primera: el único cambio que se hizo fue eliminar las instrucciones `return` que estaban dentro de cada IF.

```python
def mayor(a: int, b: int, c:int, d:int)->int:
    if (a >= b) and (a >= c) and (a >= d):
        mayor = a
    elif (b >= a) and (b >= c) and (b >= d):
        mayor = b
    elif (c >= 1) and (c >= b) and (c >= d):
        mayor = c
    else:
        mayor = d

    return mayor
```


### Solución 3: aproximación algorítmica

La tercera solución es muy diferente de las anteriores y tiene una aproximación mucho más algorítmica, en la que los cuatro valores van analizándose uno por uno. Primero observemos con cuidado la nueva función hasta estar convencidos de que funciona.

```python
def mayor(a: int, b: int, c:int, d:int)->int:
    mayor = a
    if (b > mayor):
        mayor = b
    if (c > mayor):
        mayor = c
    if (d > mayor):
        mayor = d
        
    return mayor
```

Al igual que en la segunda solución, tenemos una variable llamada `mayor` donde debería quedar la respuesta porque es la variable que vamos a retornar al final.

La primera instrucción de la función le asigna el valor de `a` a la variable `mayor`, implicando que `a` es el mayor valor. ¿Es esto correcto? No podemos saber si será correcto al final, pero lo que sí podemos decir con seguridad es que, si sólo hubiera un valor, entonces `a` sería el mayor. Esto es tan trivial que a veces resulta difícil al leerlo: el mayor en un conjunto que tiene sólo un elemento es ese único elemento.

¿Qué hace la primera instrucción condicional? En este caso hemos ampliado nuestro conjunto y ahora tenemos también a `b`, así que comparamos a `b` con `a` para ver cuál es el mayor. Si resulta que `b` era mayor, entonces dejamos en la variable `mayor` a `b`. Si no era mayor, entonces dejamos el valor que ya teníamos.

¿Qué hace la segunda instrucción condicional? Acá es donde todo se pone interesante porque agregamos a `c` a nuestro conjunto de valores y lo comparamos con el *mayor*. Esto quiere decir que lo comparamos con `a` o lo comparamos con `b`, pero no lo comparamos con los dos porque sería inútil: lo único que nos interesa saber es si `c` es mayor que el valor mayor que se había encontrado hasta el momento. Note que tampoco podemos saber si el mayor era `a` o `b`. Sólo sabemos que el valor mayor está dentro de la variable `mayor`. Al finalizar este condicional dentro de la variable también podría estar el valor de `c`, pero sólo si este fuera mayor que el mayor valor entre `a` y `b`.

¿Qué hace la tercera instrucción condicional? Lo mismo que la instrucción anterior: compara a `d` con el mayor valor que se hubiera encontrado entre `a`, `b` y `c` y, si resulta que `d` es mayor, entonces remplaza el valor de `mayor` con el valor de `d`.

Al llegar a la última instrucción de la función podemos estar seguros que dentro de la variable `mayor` se encuentra el mayor valor entre `a`, `b`, `c` y `d`, a pesar de que nunca hayamos comparado los cuatro valores entre ellos.

Esta estrategia es mucho más conveniente que la de las otras versiones de la función por varias razones. Por un lado, el código es mucho más sencillo y tiene menos comparaciones: es más fácil de leer y tiene menos posibilidades de tener errores. Por otro lado, es clara cuál era la intención del programador y, si ahora hubiera un quinto valor para comparar, sería clarísimo cómo debería modificarse la función para soportar este nuevo valor.


## Ejercicios

1. Modifique el ejercicio que retorna el número mayor para que retorne el número del parámetro en el que se encuentra el número mayor. Si hay dos o más iguales y mayores, debe retornar el número de parámetro menor (ej. si el primer y el tercer parámetro eran los mayores, debe retornar el número 1).
 
2. La calificación final de un estudiante en un curso depende de las calificaciones que obtenga en 3 exámenes, pero con unas reglas especiales. Si el estudiante sacó más de 4.0 sobre 5.00 en el tercer examen (el examen final), la nota en el curso será la nota del examen final. Si el estudiante saca menos de 2.0 en el examen final, ese examen valdrá el 50% de la nota y los otros dos exámenes valdrán el 25% cada uno. En cualquier otro caso, los exámenes pesarán lo mismo para calcular la nota final. Escriba una función que dadas las notas de los tres exámenes calcule la nota del estudiante en el curso.

3. En muchos torneos de fútbol es usual que dos equipos jueguen dos partidos para definir cuál es el mejor de ellos: uno en el estadio del primer equipo y otro en el estadio del segundo equipo. También es usual que, en caso de empate en la cantidad de partidos ganados, los goles de los equipos visitantes cuenten por dos al momento de calcular la diferencia de goles. Escriba una función para calcular el ganador entre dos equipos. La función debe recibir el nombre del primer equipo (A), el nombre del segundo equipo (B), los goles que hizo A de local, los goles que hizo B de visitante, los goles que hizo A de visitante y los goles que hizo B de local. La función debe retornar el nombre del ganador de la serie o la cadena "EMPATE" si hubo un empate entre los equipos.

4. Las denominaciones de las monedas actualmente disponibles en un país son: 20, 50, 100, 200, 500 y 1000. Escriba una función que reciba la cantidad de monedas de cada denominación que tiene una persona y el valor de un producto y le diga si es posible pagar el producto con el dinero en efectivo que tiene. Ayuda: tiene que revisar si tiene suficiente dinero y, si tiene más de lo necesario, si es posible que le den el cambio con las denominaciones de monedas que se encuentran en circulación.

5. *Picas y Fijas* es un juego en el que dos personas intentan adivinar un número de 4 dígitos que mantiene en secreto el otro jugador. En cada turno, un jugador propone un número de 4 dígitos y el otro jugador debe informar la cantidad de *picas* y la cantidad de *fijas* de ese número. Cada *pica* significa que en el número propuesto hay un dígito que también está en el número secreto, pero en una posición diferente. Cada *fija* significa que en el número propuesto hay un número que también está en el número secreto y que está en la misma posición. Por ejemplo, si el número secreto es 5678 y el número que el otro jugador propone es 6579, la respuesta sería *2 picas y 1 fija" porque 5 y 6 están en las posiciones equivocadas y porque el 7 está en la posición correcta. El ganador del juego es el jugador que encuentre el número del otro en la menor cantidad de intentos. En este ejercicio usted debe escribir dos funciones: la primera calculará la cantidad de picas dados un número secreto entre 1000 y 9999, y un número propuesto también entre 1000 y 9999; la segunda función calculará la cantidad de fijas y recibirá también un número secreto y un número propuesto.

6. Un número primo es un número que es divisible sólo por 1 y por sí mismo. Los primeros 10 números primos son 2, 3, 5, 7, 11, 13, 17, 19, 23 y 29. Escriba una función que dado un número diga cuál es el menor de los primeros diez números primos por el que es divisible o retorne -1 si no es divisible por ninguno de esos números.

7. En una competencia sólo pueden participar estudiantes universitarios que sean menores de 23 años o que cumplan 23 años durante el año en curso. Además, pueden participar todos los estudiantes universitarios que hayan cursado menos de 2 años de estudios en la Universidad. Escriba una función que reciba el año de nacimiento de una persona y el año de entrada a la universidad y retorne un valor de verdad indicando si la persona puede participar o no.

8. En una ciudad existe una restricción de circulación para los vehículos que depende del número de la placa, del tipo de vehículo, del día de la semana y de la hora del día. Los vehículos particulares sólo tienen restricción de lunes a viernes, dependiendo del último dígito de su placa: los que terminen en un número par no podrán circular entre 6:00 y 8:30 y 15:00 y 19:30 en los días del mes que sean pares; los que terminen en un número impar no podrán circular en los mismos horarios, pero de los días del mes que sean impares. La restricción para los taxis va desde las 5:30 hasta las 21:30, de lunes a sábado: los taxis cuya placa termine en el mismo dígito en que termine el día del mes no podrán circular ese día. Escriba una función que diga si un vehículo puede circular o no dados: el tipo de vehículo (str, TAXI o PARTICULAR), la placa (str, por ejemplo DMZ042), el día del mes (int, entre 1 y 31), el día de la semana (str - Lunes, Martes, Miércoles, Jueves, Viernes, Sábado o Domingo), la hora (int, entre 0 y 23) y el minuto (int, entre 0 y 59).


## Más allá de Python

Además de las estructuras basadas en IF-ELIF-ELSE, muchos lenguajes ofrecen instrucciones condicionales basados en *switch* y en *operadores ternarios*. Estos últimos son de mucha utilidad porque permiten seleccionar valores basados en condiciones, pero sin tener que utilizar demasiado espacio. Por ejemplo, este código se podría usar en Java para seleccionar una cadena de caracteres basado en el valor de la variable booleana `exito`:

```java
respuesta = exito ? "sí":"no";
```
Lo que haría la máquina virtual de Java (JVM) al encontrar este código sería revisar si la variable `exito` es verdadera y, en caso afirmativo, asignarle a `respuesta` el valor "sí"; en caso negativo, asignarle el valor "no".

En Python existe una estructura similar llamada *expresión condicional*. La traducción del ejemplo anterior a Python sería:

```python
respuesta = "sí" if exito else "no"
```
La interpretación sería exactamente igual que en el caso de Java: se le asignará "sí" a la variable `respuesta` sólo si `exito` es verdadero y de lo contrario se le asignará "no". Las expresiones condicionales pueden ser de mucha utilidad cuando las condiciones son tan fáciles como en el ejemplo, pero se pueden volver difíciles de leer cuando las condiciones son más elaboradas. Sin embargo, todo lo que se haría con una expresión condicional se puede hacer con un IF.


#### Notas 

