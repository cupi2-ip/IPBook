# El lenguaje de programación Python


```{epigraph}
Simple is better than complex.

-- Tim Peters, The Zen of Python
```

Como ya dijimos, para este libro (y para el curso de **Introducción a la Programación** del [Departamento de Ingeniería de Sistemas](http://sistemas.uniandes.edu.co) de la Universidad de los Andes), el lenguaje de programación que usaremos es Python o más precisamente Python 3 [^python3]. 

[^python3]: Desafortunadamente, Python tiene una historia larga de problemas de versiones. En Diciembre de 2008 apareció oficialmente Python 3.0, lo cual debería haber logrado que las versiones anteriores fueran consideradas *obsoletas*. El problema es que había tantos programas y librerías construidas sobre las versiones *2.x* que la transición completa ha tardado más de 10 años en ocurrir. El resultado de esto es que todavía sea fácil encontrar instalaciones de Python 2.7 como por ejemplo en las instalaciones por defecto del sistema operativo MacOS. Para efectos de este libro, cuando corra el intérprete de Python, tenga siempre cuidado de que sea una versión mayor a la 3.6.


Python es uno de miles de lenguajes de programación existentes en el mundo. Es posible que usted haya escuchado hablar o haya usado alguno de los siguientes: C, C++, Java, Kotlin, Scala, JavaScript, TypeScript, C#, PHP, Ruby, Visual Basic, Pascal, Basic, Logo, Cobol, Fortran, LISP. Además, hay ambientes de trabajo especializados que tienen sus propios lenguajes de programación, como R (para estadística), MathLab (para aplicaciones científicas) o Swift (para aplicaciones en iOS y MacOS).

Seleccionar un lenguaje de programación no es una tarea fácil: todos tienen ventajas y desventajas que van mucho más allá de lo que puede y no puede hacerse. Algunos lenguajes están diseñados o son particularmente buenos para construir cierto tipo de aplicaciones (por ejemplo, JavaScript para aplicaciones que corren en navegadores web, Swift para aplicaciones en iOS, Visual Basic para aplicaciones en Office, C/C++ para aplicaciones de bajo nivel o que requieran un altísimo desempeño) así que sería difícil usarlos en otros contextos o reemplazarlos por otros. Más allá de esto, casi cualquier lenguaje puede utilizarse para resolver cualquier problema. 

Otra diferencia importante entre lenguajes es la disponibilidad de ayuda (manuales, ejemplos, foros, cursos, etc.), librerías (programas que resuelvan problemas específicos que podamos reutilizar en nuestros propios programas) y herramientas de desarrollo. Seguramente será más díficil empezar a usar un lenguaje *esotérico*, usado por pocas personas en el mundo, que un lenguaje muy popular para el cual haya una gran cantidad de recursos disponibles y un público creciente que produzca cada vez más material de soporte. Sin embargo, debe ser claro que popularidad no implica calidad: hay lenguajes que han sido extraordinariamente populares a pesar de la gran cantidad de problemas de fondo que tenían. Además, la popularidad cambia con el tiempo: los lenguajes que hoy en día encabezan las listas eran prácticamente desconocidos hace 10 años y posiblemente serán remplazados dentro de los siguientes 10 años.

Finalmente, hay diferencias importantes en la complejidad misma de los lenguajes y de los programas que se construyen con ellos. El programa que en un lenguaje puede requerir unas pocas líneas de código, en otro lenguaje puede requerir diez o más veces la cantidad de líneas de código [^HelloWorld]. Además, en algunos lenguajes pueden escribirse programas crípticos, cuyo funcionamiento puede ser imposible de entender sin ayuda del autor, mientras que otros lenguajes fomentan que los programas sean sencillos y fáciles de entender y de mantener, sin sacrificar las funcionalidades.

[^HelloWorld]: Un buen ejemplo de esto se encuentra en [The Hello World Collection](http://helloworldcollection.de/), donde hay más de 600 implementaciones del programa para escribir "Hola, Mundo!"

## Python 

Comparado con otros lenguajes, Python tiene algunas limitaciones evidentes, pero que no son relevantes para este libro. Por el contrario, Python tiene varias características que lo hacen un lenguaje muy adecuado, en este momento, para aprender a programar. Las más importante es que Python comparte muchos conceptos y estructuras con muchos otros lenguajes, así que debería ser fácil aprender uno de estos lenguajes después de aprender a programar en Python.

La segunda razón es que la filosofía detrás del diseño del lenguaje buscaba la simplicidad y la claridad. El texto "The Zen of Python", de Tim Peters, resume esta filosofía en 19 aforismos de los cuales quisiéramos destacar los siguientes tres porque deberíamos aplicarlos a nuestros propios programas:

* **Explicit is better than implicit (Explícito es mejor que implícito).** ¿Recuerda cuando su profesor de matemáticas en el colegio le decía que el procedimiento para resolver un examen tenía que quedar escrito? Con esto su profesor buscaba entender qué era lo que estaba haciendo y cómo estaba llegando a la respuesta. Si en algún punto del procedimiento usted tenía un error, su profesor probablemente le corrigió el error y siguió aplicando el procedimiento para llegar a la respuesta correcta. Lo mismo ocurre al programar: es mejor hacer explícito lo que se está haciendo, en pequeños pasos, para que sea más fácil encontrar errores o implementar nuevas funcionalidades.

* **Simple is better than complex (Simple es mejor que complejo).** Cuando tenga que resolver un problema, le recomendamos que busque la solución más simple que pueda funcionar: entre más complicada sea una solución, más difícil será construirla, corregirla o mejorarla.

* **Readability counts (La facilidad de lectura es importante).** Parafraseando al profesor Harold Abelson, los programas se deben construir pensando primero en que humanos van a leerlos y luego en que un computador va a ejecutarlos. Además, el primer humano que va a leer nuestros programas somos nosotros mismos: deberíamos hacernos el favor de siempre escribir código que podamos leer con facilidad.



```{admonition} Tip
:class: tip
En este libro vamos a incluir frecuentemente anotaciones para reforzar estas ideas y, dentro del nivel 1, una sección dedicada enteramente a estos temas. Por favor no los olvide.
```


Para acceder al texto completo de "The Zen of Python" basta escribir ```import this``` en un intérprete de Python. El resultado debería ser el siguiente:

```{code-block} python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## Python para Introducción a la Programación

Para concluir esta sección, vamos a resumir los principales motivos detrás de la decisión que tomamos de usar el lenguaje Python en el curso Introducción a la Programación de la Universidad de los Andes.

1. **Facilidad.** El primer punto tuvo que ver con las características del lenguaje que lo hacen fácil de aprender para los que nunca antes han programado. En particular, para nosotros era importante que no fuera obligatorio utilizar los conceptos de programación orientada a objetos para poder construir programas interesantes y relativamente complejos. 

2. **Uso actual en cursos posteriores.** Introducción a la Programación es el primer curso donde los estudiantes de nuestra Universidad tienen que programar, pero no es el único. Cada vez más programas y facultades tienen cursos donde la programación es un elemento central y en varios de estos cursos Python ya había sido adoptado.

3. **Compatibilidad.** Como dijimos antes, Python se basa en conceptos que son comunes a muchos lenguajes de programación, así que la transición a otros lenguajes debería ser relativamente fácil. Nosotros creemos que al utilizar Python vamos a lograr que nuestros estudiantes desarrollen las habilidades de programación fundamentales que les permitan desempeñarse satisfactoriamente en tanto en cursos posteriores como en sus profesiones.



