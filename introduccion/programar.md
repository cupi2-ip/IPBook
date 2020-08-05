
# ¿Qué es programar?

**Programar** es la acción de escribir un conjunto **instrucciones** (un **programa**) para que un computador las ejecute. Por ejemplo, el siguiente es el primer programa que la mayoría de programadores escribe:


```python 
print('Hola, mundo!')
```


Cuando alguien decide **ejecutar** (o correr) este programa, el computador va a 
mostrar en la pantalla un mensaje que dice ```Hola, mundo!```.

```{figure} ./images/hola_mundo.png
---
width: 60%
name: hello_world
---
Ejecución del primer programa
```


Aunque sencillo, este programa nos permite ilustrar varias ideas importantes. En primer lugar, el programa se escribió usando el **lenguaje de programación** Python. Así como en español tenemos reglas de gramática y un conjunto de palabras para combinar (vocabulario), un lenguaje de programación tiene reglas de sintaxis, una colección de librerías con programas que se pueden reutilizar (el vocabulario) y unas herramientas que permiten ejecutar los programas que se escriban con ese lenguaje. En nuestro ejemplo, estamos siguiendo las reglas de sintaxis de Python, usamos una función llamada ```print``` y ejecutaremos el programa usando el intérprete [^interprete] de Python [^c].

[^interprete]: Más adelante vamos a explicar qué significa el intérprete. Por ahora es suficiente con saber que un intérprete es un programa capaz de ejecutar otros programas. En este caso, el intérprete será capaz de ejecutar programas escritos usando Python.

[^c]: Si en lugar de Python hubiéramos usado el lenguaje de programación C, el programa que habríamos tenido que escribir sería el siguiente: ```main( ) { printf("hello, world\n"); }```. Además, el programa no lo ejecutaríamos usando el intérprete de Python.


Programar no es en sí misma una actividad difícil, pero sí es una actividad compleja que involucra varios elementos y habilidades complementarias. La más importante posiblemente sea la habilidad para **resolver problemas**, que en realidad es una combinación de otras habilidades como comprensión de lectura, abstracción, descomposición, razonamiento abstracto y creatividad. Con esto queremos decir que, para programar, es necesario ser capaz de resolver problemas independientemente de que haya tecnología y computadores involucrados.

Otro componente para resaltar es el **pensamiento algorítmico**, el cual hace referencia a una cierta forma de aproximarse a la resolución de problemas. El término **algoritmo** hace referencia a las instrucciones para resolver un determinado problema. Un ejemplo común de algoritmo son las instrucciones para fritar un huevo, o las instrucciones que se encuentran en el envase de un Shampoo. Pensamiento algorítmico hace referencia a la habilidad para describir cómo se debe llegar a la solución de un problema en términos de una serie de instrucciones que alguien más pueda repetir. 

En nuestras vidas resolvemos problemas todo el tiempo (manejar un carro, entrar a nuestra oficina, pagar los recibos de servicios públicos, organizar nuestra casa), pero no necesariamente somos capaces de explicarle a alguien más cada uno de estos procesos con el nivel de detalle suficiente para que los pueda hacer exactamente igual. Cuando empecemos a programar nos daremos cuenta que uno de los obstáculos más grandes va a ser vencer la tentación de darle al computador órdenes demasiado complejas. Por el contrario, programar requiere user órdenes relativamente sencillas que permitan ir resolviendo el problema (en lugar de decirle a alguien 'frita un huevo', le vamos a tener que decir 'prende el fogón de la estufa, pon una cacerola con mantequilla, espera a que se derrita la mantequilla, ...' )

Programar requiere también conocer al menos un **lenguaje de programación** para poder escribir las instrucciones para el computador. Posiblemente aprender un lenguaje de programación sea la parte más sencilla de todo el proceso, pero es la que fácilmente se confunde con la parte central de aprender a programar. Esto es análogo a pensar que para pintar al óleo lo más importante es aprender los nombres de los colores y conocer la técnica para usar los pinceles: seguramente alguien que no tenga esos conocimientos básicos encontrará dificultades para pintar, pero con seguridad otras habilidades y actitudes son más importantes para producir verdaderas obras de arte.

Este libro pretende hacer explícito que *aprender a programar no es lo mismo que aprender un lenguaje de programación*. Tuvimos que escoger un lenguaje para nuestros ejemplos (Python), pero casi todos los conceptos que veremos podrían aplicarse a otros lenguajes de programación. En lo posible, haremos explícito cuando algo de lo que expliquemos sea exclusivo de Python.

Finalmente, programar requiere una buena disposición hacia la **tecnología** y hacia el **auto-aprendizaje**. En este libro usaremos un conjunto de herramientas y librerías relativamente sencillo que además será explicado en detalle. Estas deberían ser suficientes para construir desde programas triviales hasta programas muy interesantes y útiles. Pero un buen programador debería ser capaz (¡y debería tener muchas ganas!) de aprender a usar nuevas tecnologías por su propia cuenta.

