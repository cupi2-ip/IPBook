---
title: 'Un programa para leer'
prev_page:
  url: /nivel1/intro
  title: 'Nivel 1'
next_page:
  url: /nivel1/ejercicio_inicial
  title: 'Experimentos'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|



# Un programa para leer

En esta sección vamos a presentar un primer programa escrito usando el lenguaje de programación Python. Si nunca antes ha programado o si nunca ha programado en Python, probablemente habrá cosas que no va a entender completamente. Sin embargo, el simple hecho de revisar de forma detenida este programa le dará un poco de contexto para todos los elementos que se van a ir introduciendo a lo largo de este nivel.


## Por qué leer código de alguien más
Una habilidad muy importante para cualquier programador es la habilidad de leer código escrito por alguien más. Si dependemos de las explicaciones de alguien más para aprender un nuevo concepto o entender cómo utilizar una nueva herramienta o librería, será muy difícil que nos convirtamos en buenos programadores o el aprendizaje será muy lento. Por el contrario, la habilidad de leer el código de otros nos da una ventaja enorme y multiplica las fuentes de las que podemos aprender. En lugar de tener disponibles miles de libros, vamos a poder utilizar miles de millones de programas y de ejemplos que se encuentran disponibles en línea. 

En general, cuando se lee código escrito por alguien más se deben tener en cuenta las siguientes recomendaciones:

 - Hacer una lectura reflexiva, en varias pasadas. Es muy difícil asimilar con una sola lectura el objetivo general o los detalles de un programa que nunca habíamos visto. Además, los programas no se ejecutan en orden desde la primera línea hasta la última: como veremos más adelante, usualmente se definen bloques que se invocan desde otros lugares y que cambian completamente el orden de cualquier ejecución. La lectura se tiene que hacer entonces en varias pasadas, buscando diferentes cosas cada vez. Por otro lado, la lectura de código no es igual a la lectura de un texto cualquiera: se tiene que hacer de forma *lenta y cuidadosa*, evaluando constantemente qué es lo que se tiene claro y qué es lo que queda por descubrir.

 - Buscar una comprensión global vs una comprensión de los detalles. No es lo mismo leer un programa buscando tener una idea global de cuál es su objetivo o cómo está estructurado, que leer un programa para entender en profundidad un detalle particular. Antes de empezar cada lectura se tiene que definir el objetivo que se va a buscar.
 
 - Hacer explícitas las cosas que se desconocen o son poco claras. A medida que se vaya haciendo la lectura aparecerán cosas desconocidas, muchas de las cuales se resolverán más adelante en el mismo programa. Es una buena idea entonces ir marcando cuáles son esas cosas desconocidas y luego hacer explícitos los puntos en los que se resuelvan esas preguntas. 

 - Identificar y apropiar estrategias para resolver problemas. A medida que aumenta su experiencia, cada programador va construyendo en su cabeza su propio conjunto de estrategias que aplicará para resolver problemas aparezcan frecuentemente. Debido a esto, dos programadores pueden llegar a soluciones *aparentemente* muy diferentes incluso aunque estén usando el mismo lenguaje y los mismos algoritmos. Leer con cuidado el código escrito por alguien más nos abre las puertas al conjunto de estrategias de otros programadores y deberíamos aprovecharlo para enriquecer nuestra propia caja de herramientas.

 - Diferenciar estilos. Cada programador tiene también un estilo propio que utiliza en la construcción de sus programas y que afecta la forma en la que se ven. Al leer programas escritos por alguien más se debería también observar con cuidado esas diferencias de estilo y evitar confundir diferencias de estilo (forma) con diferencias en las estrategias (fondo) o incluso diferencias algorítmicas.


## El primer programa en Python

El siguiente es un programa **completo** en Python que utiliza una buena parte de los conceptos que se presentarán dentro de este nivel. Cuando haya terminado el nivel podrá regresar a este programa para volver a estudiarlo: ¡Todo debería ser claro en esta nueva oportunidad!

**Instrucciones:**
Lea el siguiente programa con cuidado, intentando entender qué es lo que está haciendo. 

* Observe los bloques en los que está dividido y tenga en cuenta que en en el lenguaje Python la *indentación* (la cantidad de espacios en blanco al inicio de cada línea, la sangría) es importante y sirve para definir bloques.
* Note que hay algunas palabras que se repiten.
* Nota también que hay algunas cosas escritas en español y otras escritas en inglés.
* Intente descubrir en qué orden se van a ejecutar cada una de las instrucciones del programa. *Ayuda:* Cada instrucción en este programa se va a ejecutar exactamente una vez.
* Anote qué cosas del programa no sabe qué significan.

```python
def perimetro_triangulo(cateto1: float, cateto2: float)->float:
    hipotenusa = calcular_hip(cateto1, cateto2)    
    return cateto1 + cateto2 + hipotenusa


def calcular_hip(cateto1: float, cateto2: float)->float:
    suma_cuadrados = (cateto1 ** 2) + (cateto2 ** 2)
    hipotenusa = pow(suma_cuadrados, 0.5)
    return hipotenusa


cadena_cat_1 = input("Indique la longitud del primer cateto: ")
cadena_cat_2 = input("Indique la longitud del segundo cateto: ")
cat_1 = float(cadena_cat_1)
cat_2 = float(cadena_cat_2)

perimetro = perimetro_triangulo(3,4)

print("El perímetro de un triángulo rectángulo que tenga catetos de longitud",
      cat_1, "y", cat_2, "es", perimetro)

```

A continuación se encuentra el mismo programa con una importante diferencia: esta vez se han incluído **comentarios**, es decir anotaciones que el programador dejó para que otras personas que quieran estudiar o modificar el programa puedan hacerlo con más facilidad. 

**Escribir** buenos comentarios en el código (cortos, útiles y precisos) y **leer** con cuidado los comentarios de otros son muy buenas prácticas de programación.

```python
# Este programa está escrito en el archivo perimetro.py

def perimetro_triangulo(cateto1: float, cateto2: float)->float:
    """
    Esta función calcula el perímetro de un triángulo rectángulo
    dada la longitud de sus dos catetos
    Parámetros:
      cateto1 (float): la longitud del primer cateto del triángulo
      cateto2 (float): la longitud del segundo cateto del triángulo
    Retorno
      (float): la longitud del perímetro del triángulo
    """
    # Usar la función calcular_hip para calcular la longitud del lado faltante
    hipotenusa = calcular_hip(cateto1, cateto2)
    
    # Sumar los tres lados y convertirlos en la respuesta de la función
    return cateto1 + cateto2 + hipotenusa


def calcular_hip(cateto1: float, cateto2: float)->float:
    """
    Esta función calcula la longitud de la hipotenusa en un triángulo rectángulo
    dada la longitud de sus dos catetos
    Parámetros:
      cateto1 (float): la longitud del primer cateto del triángulo
      cateto2 (float): la longitud del segundo cateto del triángulo
    Retorno
      (float): la longitud de la hipotenusa
    """
    # Sumar la longitud de los catetos elevados al cuadrado
    suma_cuadrados = (cateto1 ** 2) + (cateto2 ** 2)
    
    # Calcular la raiz cuadrada de la suma usando la función pow y el exponente 0.5
    hipotenusa = pow(suma_cuadrados, 0.5)
    return hipotenusa


# Solicitarle al usuario la longitud de los dos catetos
cadena_cat_1 = input("Indique la longitud del primer cateto: ")
cadena_cat_2 = input("Indique la longitud del segundo cateto: ")

# Convertir los caracteres dados por el usuario en un número decimal
cat_1 = float(cadena_cat_1)
cat_2 = float(cadena_cat_2)

# Llamar a la función con los valores recibidos
perimetro = perimetro_triangulo(3,4)

# Mostrarle al usuario el resultado de la operación
print("El perímetro de un triángulo rectángulo que tenga catetos de longitud", cat_1, "y", cat_2, "es", perimetro)

```

**Preguntas:**
A partir de su lectura del programa, intente responder las siguientes preguntas. No se preocupe si no está seguro de algo, al final del nivel todas sus dudas deberían haber quedado aclaradas.

* ¿Cuál es el objetivo del programa?
* ¿Qué información tendrá que suministrar el usuario que ejecute el programa?
* ¿Cuál es el objetivo de cada bloque?
* ¿Qué es lo que primero se ejecuta?
* ¿Cual es la diferencia entre las cosas que están escritas en español y las que están escritas en inglés?

