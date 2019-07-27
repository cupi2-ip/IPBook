---
title: 'Introducción'
prev_page:
  url: 
  title: ''
next_page:
  url: /nivel1/intro
  title: 'Nivel 1'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Introducción


## Qué significa y qué se necesita para programar

Programar es, sencillamente, la acción de escribir un conjunto de instrucciones que un computador pueda ejecutar. Por ejemplo, el siguiente es el primer *programa* que la mayoría de programadores se encuentra:

```python
print('Hola, mundo!')
```

Aunque sencillo, este programa nos permite ilustrar varias ideas importantes. En primer lugar, este programa se escribió usando el *lenguaje de programación* Python. Un lenguaje de programación es simplemente una combinación de unas reglas de sintaxis, con una colección de librerías con programas que se pueden reutilizar, y unas herramientas que permiten ejecutar los programas que se escriban con ese lenguaje. En el caso de nuestro programa, estamos usando las reglas de sintaxis de Python, estamos usando una función llamada ```print```, y estamos usando el intérprete [^interprete] de Python para ejecutar el programa [^c].

[^interprete]: Más adelante vamos a explicar qué significa el intérprete. Por ahora es suficiente con saber que un intérprete es un programa capaz de ejecutar otros programas. En este caso, el intérprete será capaz de ejecutar programas escritos usando Python.

[^c]: Si en lugar de Python hubiéramos usado el lenguaje de programación C, el programa que habríamos tenido que escribir sería el siguiente: ``` main( ) { printf("hello, world\n"); }```. Además, el programa no lo ejecutaríamos usando el intérprete de Python.


Cuando alguien decide *ejecutar* (o correr) este programa, el computador simplemente va a mostrar en la pantalla un mensaje que dice ```Hola, mundo!```. Sin embargo, con algo de práctica y estudio podremos construir programas mucho más avanzados que, por ejemplo, calculen estadísticas a partir de los datos de un censo, analicen una imagen de una resonancia magnética para encontrar un tumor, reproduzcan un video, o sean capaces de sugerir el mejor movimiento para hacer en un juego de ajedrez.


Programar no es una actividad difícil, pero sí es una actividad compleja en el sentido de que involucra varios elementos y habilidades complementarias. La más importante posiblemente sea la habilidad para *resolver problemas*, que en realidad es una combinación de otras habilidades como comprensión de lectura, abstracción, descomposición, razonamiento abstracto, y creatividad, entre otras. Con esto queremos decir que, para programar, es necesario ser capaz de resolver problemas idenpendientemente de que haya tecnología y computadores involucrados.

El segundo componente importante para resaltar es el *pensamiento algorítmico*, el cual hace referencia a una cierta forma de aproximarse a la resolución de problemas. El término *algoritmo* hace referencia a las instrucciones para resolver un determinado problema. Dos ejemplos comunes son las instrucciones para fritar un huevo y las instrucciones que se encuentran en el embase de un Shampoo. Pensamiento algorítmico hace referencia a la habilidad para describir cómo se debe llegar a la solución de un problema en términos de una serie de instrucciones que alguien más pueda repetir. 

En nuestras vidas resolvemos problemas todo el tiempo (manejar un carro, entrar a nuestra oficina, pagar los recibos de servicios públicos, organizar nuestra casa), pero no necesariamente somos capaces de explicarle a alguien más cada uno de estos procesos con el nivel de detalle suficiente para que lo pueda hacer exactamente igual. Cuando empecemos a programar nos daremos cuenta que uno de los obstáculos más grandes va a ser vencer la tentación de darle al computador órdenes demasiado gruesas y en cambio darle órdenes mucho más pequeñas que permitan ir resolviendo el problema (en lugar de decirle a alguien más 'frita un huevo', le vamos a tener que decir 'prende el fogón de la estufa, pon una cacerola con mantequilla, espera a que se derrita la mantequilla, ...' )

Programar requiere también conocer al menos un *lenguaje de programación* para poder escribir las instrucciones para el computador. Posiblemente aprender un lenguaje de programación sea la parte más sencilla de todo el proceso, pero es la parte que fácilmente se confunde con la parte central de aprender a programar. Esto es análogo a pensar que para pintar al óleo lo más importante es aprenderse los nombres de los colores y conocer la técnica para usar los pinceles: seguramente alguien que no tenga esos conocimientos básicos encontrará dificultades para pintar, pero con seguridad otras habilidades y actitudes son más importantes para producir verdaderas obras de arte.

Este libro pretende hacer mostrar con claridad que aprender a programar no es lo mismo que aprender un lenguaje de programación. Inevitablemente tuvimos que escoger un lenguaje para nuestros ejemplos (Python), pero casi todos los conceptos que se estudian podrían aplicarse a otros lenguajes de programación. En lo posible, haremos explícito cuando algo de lo que expliquemos sea exclusivo de Python.

Finalmente, programar requiere una buena disposición hacia usar tecnología. En este libro usaremos un conjunto de herramientas y librerías relativamente secillo que además será explicado en detalle. Estas herramientas deberían ser suficientes para construir desde programas triviales hasta programas muy interesantes y útiles.


## Acciones fundamentales

La experiencia de muchos años enseñando a programar nos muestra que con una adecuada actitud y compromiso cualquiera  puede aprender a programar. Los estudiantes que se aproximan a la programación esperando cumplir con un requisito, sin ver el enorme potencial que podría tener para su desempeño profesional, usualmente tienen menos éxito que aquellos que tienen una mente abierta y curiosa y que se enfrenten a cada reto esperando aprender algo de él.

Además de esto, la experiencia también nos ha mostrado que los estudiantes que realizan las siguientes 3 acciones usualmente tienen mucho más éxito en su proceso de aprendizaje, disfrutan más la experiencia, y siguen aprendiendo a programar más allá de su primer curso.


### Lectura con atención

Para poder programar es necesario leer con atención todo lo relacionado con el problema que se esté solucionando. Es casi imposible construir una buena solución si no se han leído con cuidado las condiciones de lo que se está pidiendo ni las restricciones para la solución.

Muchas veces los problemas a los que se enfrentan los estudiantes que empiezan a programar no tienen que ver con la programación en sí misma, sino que tienen que ver con que el estudiante no entendió el problema que tenía que resolver.

¡Nunca empiece a programar sin entender antes lo que le están preguntando!


### Práctica deliberada y reflexiva

Al igual que cualquier otra actividad basada en habilidades, programar requiere practicar. Así como no se puede tocar aprender a tocar violín o a montar bicicleta leyendo todos los libros disponibles sobre el tema, para aprender a programar se necesita practicar programando.

Más aún, para hacer más eficiente su proceso de aprendizaje, un estudiante de programación debería esforzarse por hacer una práctica *deliberada* y *reflexiva*. Práctica deliberada hace referencia a tener un objetivo específico cuando se practica. Por ejemplo, cuando un futbolista practica no se limita a *jugar futbol*, sino que hace en cada sesión repite ejercicios diseñados para ayudarlo a desarrollar una determinada habilidad. De igual forma, en cada sesión de práctica los pianistas más exitosos definen un objetivo particular (practicar un tipo de técnica, resolver un fragmento de una pieza) en lugar de simplemente sentarse a *tocar piano*.

Por otro lado, práctica *reflexiva* hace referencia al proceso que debería hacer un estudiante al terminar una práctica. En lugar de simplemente dar el ejercicio por terminado, el estudiante debería tomarse al menos un momento para reflexionar sobre lo que hizo, lo que aprendió, los problemas que enfrentó y las conclusiones que se podrían sacar de la experiencia. Se ha visto en muy diversas situaciones que el esfuerzo invertido en este proceso de reflexión hace que la práctica sea mucho más efectiva y termina reduciendo el esfuerzo total que se debe hacer.

Este libro incluye numerosos ejercicios para cada uno de los temas, los cuales han sido seleccionados para ejercitar habilidades particulares. A medida que vaya avanzando, procure resolver los ejercicios haciendo una reflexión sobre lo que haya aprendido al final de ellos.

### Lectura de código

Al igual que un pintor no podría pintar sus propias obras sin haber visto las de otros, o un escritor no podría escribir una novela sin haber leído las de muchos otros, para escribir programas es necesario poder leer programas escritos por otros. Sin embargo, no se trata de hacer una lectura superficial de esos programas, sino de hacer una lectura cuidadosa que nos permita identificar las características y objetivos de cada uno y nos permita confrontar nuestras propias dudas y vacíos en nuestro conocimiento.

A lo largo de este libro encontrará numerosos fragmentos de código que ilustran conceptos particulares. Además encontrará también programas más largos y complejos que retarán sus habilidades de lectura. ¡Haga el esfuerzo de leer estos programas, así no los entienda completamente en un primer momento! En el nivel 1 le daremos algunas recomendaciones adicionales sobre cómo leer código.

## Sobre este libro

Este libro ha sido concebido para acompañar el curso de Introducción a la Programación de la Universidad de los Andes, el cual está dirigido a estudiantes que nunca antes hayan programado. Por este momtivo el libro tiene las siguientes características.

* **Libro básico, para aprender a programar:** A diferencia de otros libros que le enseñan Python a programadores que ya conozcan otros lenguajes, este libro no supone ningún conocimiento previo de programación.

* **Libro soporte:** El libro está pensado para soportar y aclarar cualquier duda que haya quedado en el aula. Un estudiante del curso debería poder encontrar acá aclaraciones y ejercicios adicionales sobre cualquier tema.

* **Python:** El curso está basado en Python, así que el libro también está basado en Python. Sin embargo, el libro hace un esfuerzo por identificar claramente los conceptos centrales que son aplicables a otros lenguajes de programación, en lugar de simplemente presentarlos como características del lenguaje.

* **Organización:** El libro está organizado siguiendo la estructura del curso y el curso está organizado teniendo en cuenta restricciones y necesidades que son propias de nuestros programas. Por ejemplo, la cantidad de tiempo disponible, el contenido de los cursos siguientes, los programas en los que están inscritos nuestros estudiantes, y la necesidad de desarrollar competencias algorítmicas por encima de competencias para la estructuración de programas. Esto hace que la organización de este libro sea muy diferente a la de muchos otros libros de programación con Python. Por ejemplo, el tema de programación orientada a objetos, que aparece en los primeros capítulos de otros libros, está completamente ausente en este. Algo similar pasa con el tema de manejo y creación de excepciones.




