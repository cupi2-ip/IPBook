
# Qué significa y qué se necesita para programar

Programar es la acción de escribir instrucciones para que un computador las ejecute. Por ejemplo, el siguiente es el primer *programa* que la mayoría de programadores conoce:

```python
print('Hola, mundo!')
```

Aunque sencillo, este programa nos permite ilustrar varias ideas importantes. En primer lugar, este programa se escribió usando el *lenguaje de programación* Python. Así como en un lenguaje como el español tenemos reglas de gramática y un conjunto de palabras para combinar (vocabulario), un lenguaje de programación tiene reglas de sintaxis, una colección de librerías con programas que se pueden reutilizar, y unas herramientas que permiten ejecutar los programas que se escriban con ese lenguaje. En el caso de nuestro ejemplo, estamos siguiendo las reglas de sintaxis de Python, usamos usando una función llamada ```print```, y usaremos el intérprete [^interprete] de Python para ejecutar el programa [^c].

[^interprete]: Más adelante vamos a explicar qué significa el intérprete. Por ahora es suficiente con saber que un intérprete es un programa capaz de ejecutar otros programas. En este caso, el intérprete será capaz de ejecutar programas escritos usando Python.

[^c]: Si en lugar de Python hubiéramos usado el lenguaje de programación C, el programa que habríamos tenido que escribir sería el siguiente: ``` main( ) { printf("hello, world\n"); }```. Además, el programa no lo ejecutaríamos usando el intérprete de Python.


Cuando alguien decide *ejecutar* (o correr) este programa, el computador va a mostrar en la pantalla un mensaje que dice ```Hola, mundo!``` (ver imagen). Sin embargo, con algo de práctica y estudio podremos construir programas mucho más avanzados que, por ejemplo, calculen estadísticas a partir de los datos de un censo, analicen una imagen de una resonancia magnética para encontrar un tumor, reproduzcan un video, o sean capaces de sugerir el mejor movimiento para hacer en un juego de ajedrez.


![](./images/hola_mundo.png)

Programar no es una actividad difícil, pero sí es una actividad compleja que involucra varios elementos y habilidades complementarias. La más importante posiblemente sea la habilidad para *resolver problemas*, que en realidad es una combinación de otras habilidades como comprensión de lectura, abstracción, descomposición, razonamiento abstracto, y creatividad. Con esto queremos decir que, para programar, es necesario ser capaz de resolver problemas idenpendientemente de que haya tecnología y computadores involucrados.

El segundo componente para resaltar es el *pensamiento algorítmico*, el cual hace referencia a una cierta forma de aproximarse a la resolución de problemas. El término *algoritmo* hace referencia a las instrucciones para resolver un determinado problema. Dos ejemplos comunes son las instrucciones (el algoritmo) para fritar un huevo y las instrucciones que se encuentran en el embase de un Shampoo. Pensamiento algorítmico hace referencia a la habilidad para describir cómo se debe llegar a la solución de un problema en términos de una serie de instrucciones que alguien más pueda repetir. 

En nuestras vidas resolvemos problemas todo el tiempo (manejar un carro, entrar a nuestra oficina, pagar los recibos de servicios públicos, organizar nuestra casa), pero no necesariamente somos capaces de explicarle a alguien más cada uno de estos procesos con el nivel de detalle suficiente para que lo pueda hacer exactamente igual. Cuando empecemos a programar nos daremos cuenta que uno de los obstáculos más grandes va a ser vencer la tentación de darle al computador órdenes demasiado gruesas y en cambio darle órdenes mucho más pequeñas que permitan ir resolviendo el problema (en lugar de decirle a alguien 'frita un huevo', le vamos a tener que decir 'prende el fogón de la estufa, pon una cacerola con mantequilla, espera a que se derrita la mantequilla, ...' )

Programar requiere también conocer al menos un *lenguaje de programación* para poder escribir las instrucciones para el computador. Posiblemente aprender un lenguaje de programación sea la parte más sencilla de todo el proceso, pero es la que fácilmente se confunde con la parte central de aprender a programar. Esto es análogo a pensar que para pintar al óleo lo más importante es aprender los nombres de los colores y conocer la técnica para usar los pinceles: seguramente alguien que no tenga esos conocimientos básicos encontrará dificultades para pintar, pero con seguridad otras habilidades y actitudes son más importantes para producir verdaderas obras de arte.

Este libro pretende hacer explícito que aprender a programar no es lo mismo que aprender un lenguaje de programación. Inevitablemente tuvimos que escoger un lenguaje para nuestros ejemplos (Python), pero casi todos los conceptos que veremos podrían aplicarse a otros lenguajes de programación. En lo posible, haremos explícito cuando algo de lo que expliquemos sea exclusivo de Python.

Finalmente, programar requiere una buena disposición hacia la *tecnología* y hacia el *auto-aprendizaje*. En este libro usaremos un conjunto de herramientas y librerías relativamente secillo que además será explicado en detalle. Estas deberían ser suficientes para construir desde programas triviales hasta programas muy interesantes y útiles. Pero un buen programador debería ser capaz (¡y debería tener muchas ganas!) de aprender a usar nuevas tecnologías por su propia cuenta.

