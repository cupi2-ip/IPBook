# Ambiente básico de trabajo

```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```

```{admonition} Objetivo de la sección
El objetivo de esta sección es presentar las principales herramientas que se necesitan para poder programar, para que usted pueda reconocer sus nombres y buscar las que le hagan falta.
```

Para escribir programas es necesario utilizar unas herramientas que pueden variar dependiendo del lenguaje de programación. Incluso, para el mismo lenguaje es normal que existan muchas alternativas: no es necesario conocerlas todas, pero sí es importante poder utilizar al menos una con destreza.

En el caso de Python, lo usual es que se utilicen los siguientes elementos.


## IDE - Integrated Development Environment

```{figure} ./images/spyder.png
---
width: 100%
name: spyder
---
Captura de pantalla de Spyder
```


Un ambiente integrado de desarrollo es un programa que integra muchas herramientas que se requieren para programar con facilidad. El elemento más importante de un IDE es un editor enriquecido para el lenguaje, que es capaz de marcar errores de sintaxis y que utilice colores, entre otras ayudas, para facilitar la comprensión del código. Otras herramientas que se encuentran usualmente en un IDE son un depurador (para seguir la traza de una ejecución), un explorador de archivos y un mecanismo para ejecutar los programas con facilidad.

En este libro utilizaremos un IDE para Python llamado Spyder que, aunque no es el IDE más poderoso disponible, tiene muchas características que lo hacen propicio para aprender a programar:
 
* Es sencillo. Comparado con otros IDEs, ofrece menos opciones, pero esto hace que un desarrollador sin experiencia no se pierda en medio de muchas opciones que no sabría utilizar.
* Tiene un intérprete de Python bien integrado.
* Ayuda al desarrollo, pero no demasiado. Otros IDEs tienen muchos más mecanismos automatizados que sugieren o incluso cambian cosas a medida que el desarrollador va trabajando. Aunque esto es muy útil para desarrolladores experimentados, hemos visto que a los estudiantes les da una falsa sensación de que saben lo que están haciendo, cuando en realidad es el IDE el que los está guiando. El resultado de esto es que después no logran explicar lo que hicieron o no logran utilizar otra herramienta que los ayude de forma diferente.
* Multiplataforma. Está disponible para todas las plataformas principales (Windows, Linux, Mac)
* No usa formatos propietarios. Lo que se desarrolle en Spyder se puede llevar a otra herramienta sin ningún problema.
* Es gratuito y fácil de instalar.

Otros IDE populares que están disponibles en este momento para desarrollar programas en Python incluyen Visual Studio Code, PyCharm, Eclipse (+PyDev) y VIM. Si tiene la oportunidad de escoger el IDE que va a usar, asegúrese de entender las capacidades que tenga (por ejemplo para completar código y hacer *debugging*), la compatibilidad con otras herramientas, y el tipo de licencia que esté disponible.
 

## Intérprete

```{figure} ./images/hola_mundo.png
---
width: 60%
name: interprete
---
Ejecución del primer programa
```

Python es un lenguaje interpretado [^interpretado]: esto significa que para correr los programas escritos en Python es necesario que otro programa llamado intérprete los ejecute. En la {numref}`figura {number} <interprete>` se puede ver que se corrió un programa que se escribió en el archivo ```hola_mundo.py``` usando el intérprete de Python que se invocó con el comando ```python```.

[^interpretado]: Python, al igual que otros lenguajes como Java, es realmente un lenguaje compilado e interpretado. Más aún, dependiendo de la implementación que se use, podría ser que los programas efectivamente se compilen y que no haya interpretación. Por simplicidad, en este libro hablaremos del intérprete de Python, sin entrar en detalles sobre el proceso de compilación.

Cada lenguaje de programación interpretado tiene su propio intérprete, e incluso puede haber varios intérpretes diferentes para el mismo lenguaje. En este libro vamos a suponer que usted está usando el intérprete básico, pero para Python hay varios adicionales que tienen características especiales como ser más rápidos, o requerir menos memoria, o incluso correr en plataformas especiales como plataformas de prototipado electrónico (ej. ESP8266 y ESP32) [^JS].

[^JS]: Otro ejemplo es el lenguaje JavaScript, para el que diferentes compañías han construido sus propios intérpretes: SpiderMonkey para Mozilla Firefox, V8 para Google Chrome, JavaScriptCore para Safari, Chakra para Microsoft Edge y Hermes para aplicaciones Android basadas en React Native.


## REPL para Python

```{figure} ./images/repl.png
---
width: 100%
name: repl
---
REPL de Python
```


Como en el caso de otros lenguajes interpretados, Python ofrece una herramienta de tipo **REPL**, la cual permite que un usuario interactúe con el lenguaje y vaya ejecutando instrucciones una por una. La sigla REPL hace referencia al orden en el que se van realizando las operaciones:

* **Read**. En primer lugar, la herramienta lee lo que escribió el usuario y le informa si hay algún error.
* **Evaluate**. Luego, la herramienta evalúa lo que escribió el usuario usando el intérprete del lenguaje. Esto quiere decir que en este punto se ejecuta lo que el usuario haya escrito.
* **Print**. Se imprime en la herramienta el resultado de la ejecución para que el usuario lo pueda leer.
* **Loop**. Se repite el proceso completo.

En la imagen anterior se demuestra el uso del REPL estándar de Python con varios ciclos de ejecución. Cada vez que aparecen los caracteres ```>>>``` se le pidió al usuario que ingresara un comando. Lo que aparece en la siguiente línea es el resultado de cada una de las ejecuciones.

Para acceder al REPL estándar de Python hay dos opciones básicas:

1. Ejecutar el comando ```python``` desde la línea de comandos o el terminal (ver siguiente sección).
2. Usar el IDE. En el caso de Spyder, hay una ventana con el título 'IPython Console' que nos permite interactuar directamente con el REPL.

El otro REPL para Python ampliamente utilizado se llama IPython y es el que está embebido dentro de Spyder. También puede ejecutarse desde la línea de comandos usando el comando ```ipython```. Aunque IPython tiene algunas ventajas sobre el REPL normal, no son realmente significativas cuando apenas se está aprendiendo a programar. Usted reconocerá que estamos usando IPython en lugar del REPL normal porque en lugar de los caracter ```>>>``` aparece el número de la instrucción que se está ejecutando y se separan las instrucciones ingresadas (```IN```) del resultado de la ejecución (```OUT```) :

```{figure} ./images/ipython.png
---
width: 100%
name: ipython
---
Captura de pantalla de IPython
```


**Actividades:**

1. Abra el REPL en su computador, copie las instrucciones del ejemplo y revise que el resultado sea similar.
2. Evalúe en el REPL la instrucción ```10/3```. ¿Qué piensa del resultado? ¿Es el que usted esperaba?
3. Escriba la instrucción que convierta 15 grados Celsius al equivalente en grados Fahrenheit. Recuerde que cada grado Fahrenheit equivale a 5 novenos de un grado Celsius y que la escala está desplazada 32 grados. Ayuda: 0 grados Celsius equivalen a 32 grados Fahrenheit, 37.5 (la temperatura aproximada de un cuerpo humano) equivalen a 99.5, y 15 grados Celsius equivalen a 59 grados Fahrenheit.



## Línea de comandos / terminal / consola

La última herramienta que probablemente tenga que usar cuando esté programando es la línea de comandos del sistema operativo. Esto también se conoce como la terminal o la consola y es un ambiente *no gráfico* interactivo que le permite ejecutar comandos directamente sobre el sistema operativo. Entre otras muchas opciones, desde la línea de comandos usted puede ejecutar programas, trabajar con el sistema de archivos (crear, renombrar, mover, eliminar y hasta editar archivos) y utilizar una gran cantidad de utilidades.

Para los que nunca la han utilizado, usar la línea de comandos suele parecer incómodo y difícil. La realidad es que su uso eficiente requiere un tiempo de práctica, pero después termina siendo mucho más rápido para hacer ciertas tareas que utilizar un ambiente gráfico y el mouse. Por ejemplo, imagine que en una carpeta suya hubiera una colección de 500 fotos y que usted quisiera tener versiones reducidas de esas imágenes (*previews*, *thumbnails*). Normalmente a usted le tomaría una buena cantidad de clics abrir cada una de esas fotos y cambiarle el tamaño. Desde la línea de comandos de OS X usted simplemente puede usar el comando ```sips -Z 120 *.png``` y realizar la operación sobre todas las imágenes.

El objetivo de esta sección no es explicar en detalle el funcionamiento de las líneas de comandos de cada sistema operativo, sino mostrarle que existen e invitarlo para que estudie por su cuenta su funcionamiento.

En Windows, la línea de comandos se invoca corriendo el programa ```cmd```.

```{figure} ./images/cmd.png
---
width: 100%
name: cmd
---
Línea de comandos en Windows: cmd
```

En MacOS X, la línea de comandos se invoca corriendo el programa ```Terminal```.

```{figure} ./images/terminal.png
---
width: 80%
name: terminal
---
Línea de comandos en MacOS X: Terminal
```


En Linux, la línea de comandos suele estar corriendo todo el tiempo, pero dependiendo de la distribución que esté usando se llega a ella de formas diferentes.


## Otras herramientas

### Manejador de paquetes

En el mundo de la programación, una de las cosas más complejas de manejar son las dependencias hacia otros programas. En este libro veremos cómo nuestros programas poco a poco van a volverse más complicados y vamos a empezar a integrar programas construidos por otros desarrolladores. Para lidiar con esa complejidad existen herramientas llamadas *manejadores de paquetes*. 

En el mundo de Python hay dos manejadores de paquetes que se usan principalmente. El primero se llama ```pip``` y es capaz de buscar, instalar, actualizar y desinstalar paquetes disponibles en el Python Package Index [https://pypi.org/](https://pypi.org/). Como se ve en la {numref}`figura {number} <pip>`, usando ```pip``` es posible instalar un paquete y todas sus dependencias utilizando un solo comando.

```{figure} ./images/pip.png
---
width: 100%
name: pip
---
Ejemplo de uso de pip para instalar el paquete 'pyroids' y sus dependencias.
```

El otro manejador de paquetes ampliamente utilizado es ```conda```, que utiliza el repositorio de paquetes de Anaconda [https://repo.anaconda.com/](https://repo.anaconda.com/): si usted instaló Python en su computador utilizando Anaconda, probablemente sea buena idea que utilice ```conda``` para manejar la instalación de paquetes en su máquina.


### Notebooks

En el mundo Python es frecuente que en lugar de utilizar un IDE, donde cada programa se construye en uno o varios archivos python, se utilicen unas estructuras llamadas **notebooks**. En síntesis, un **notebook** es un archivo  que se lee y se edita a través de una aplicación web y que puede mezclar texto con fragmentos de código que se pueden ejecutar dentro del notebook. La {numref}`figura {number} <notebooks>` muestra una captura de pantalla de un notebook en uso: tiene una *celda* en la que hay un texto con formato y luego tiene una *celda* con un fragmento de un programa y con el resultado de su ejecución abajo.

```{figure} ./images/notebooks.png
---
width: 100%
name: notebooks
---
Captura de pantalla de un *notebook* con Jupyter
```
Si quiere saber más sobre notebooks puede visitar la página del proyecto Jupyter, los cuales desarrollan la principal herramienta para soportar notebooks: [https://jupyter.org/](https://jupyter.org/). Sin embargo, su instalación y uso puede no ser tan fácil para un principiante.



