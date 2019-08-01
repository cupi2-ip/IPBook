Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Lógica vs. Interacción

Usualmente la preocupación más importante cuando se construye un programa es que sea correcto, es decir que sus cálculos y la forma en la que manipule la información que le dé un usuario sea correcta. Por ejemplo, lo más importante del sistema que manipula el dinero en un banco es que lleve correctamente las cuentas: nadie puede perder dinero, deben cobrar lo correcto por cada operación, el descuento de impuestos debe ajustarse a la ley y deben abonar los intereses correctamente calculados.

Además de la corrección,  hay otras preocupaciones para tener en cuenta cuando se desarrolla un nuevo programa. Para un usuario, las preocupaciones comunes tienen que ver con la seguridad, el desempeño (qué tan rápido es el sistema) y la usabilidad (qué tan fácil de usar es). Desde el punto de vista de quien desarrolla un sistema, otras preocupaciones importantes son la escalabilidad (qué tan bien funcionará el sistema cuando tenga muchos usuarios o muchos datos), la tolerancia a fallos (cómo se comporta el sistema cuando ocurren ciertos problemas), o la interoperabilidad (qué tan fácil es que el sistema intercambie información con otros sistemas que ya existan) [^ac].

[^ac]: Las preocupaciones de las que hemos estado hablando se conocen usualmente como *Requerimientos No Funcionales* o como *Atributos de Calidad*. Aunque usualmente son un tema que se estudia más adelante, no está de más empezar a usar esta terminología y empezar a tener una sensibilidad hacia estas problemáticas. Pensar únicamente en la corrección del software y en construir programas lo más rápidamente posible nos ha llevado a una situación en la que tenemos cada vez más software que es inutil y tiene que botarse a la caneca y reconstruirse.


Sin embargo, la mayor preocupación para quien desarrolla un sistema debería ser la *mantenibilidad*. Esto quiere decir: qué tan fácil es hacerle un cambio a un sistema (ej. agregarle alguna funcionalidad, corregir algún error, mejorar su apariencia). Cuando se está aprendiendo a programar puede parecer que esta no es una cuestión importante y que lo prioritario son la corrección y el desempeño. La realidad es que una vez se empieza a usar un programa, siempre es necesario hacerle modificaciones, especialmente cuando es muy exitoso. Sólo piense en la cantidad de actualizaciones que tiene que instalar permanentemente en su computador o en su celular: con casi total seguridad usted no está utilizando la primera versión (1.0) de ninguna aplicación [^mant].

[^mant]: Si se compara el tiempo que toma el desarrollo inicial de un software y el tiempo que dura su mantenimiento posterior, en la mayoría de casos de software exitoso se va a encontrar que el mantenimiento se lleva la mayor parte del tiempo. Por ejemplo, el software que utilizan muchos bancos del mundo en su *core*, o el software que usan las areolíneas para el control de vuelos y reservas, o el software que utilizan las empresas de telecomunicaciones para hacer conexiones entre redes, se construyó hace decenas de años, usando tecnologías que hoy ni siquiera se enseñan ya. La tecnología y las necesidades, especialmente de integración, han cambiado, lo cual ha obligado a hacerles actualizaciones permanentes a estos sistemas: si no fuera porque estos sistemas se construyeron para garantizar su mantenibilidad, hace muchos años que habrían tenido que ser remplazados y las empresas que los usan habrían tenido que incurrir en costos altísimos que podrían hasta haberlas quebrado.



La pregunta natural que debería surgir es entonces: ¿cómo logramos que un programa sea mantenible? Ya en este capítulo discutimos la primera recomendación: documentando el código. Cuando el código está documentado es más fácil que otros programadores o nosotros mismos podamos hacer mejoras o correcciones a nuestros programas.

La segunda recomendación es incluso más importante: estructurando el programa de tal forma que sea fácil de entender. Esto significa que queremos que sea fácil entender cómo está organizado para que cuando haya un error sea fácil encontrar donde se debería corregir, o para que cuando se quiera agregar nuevas funcionalidades no se necesite una gran reestructuración.

Es posible que en este momento sea difícil para usted imaginarse la complejidad de un gran desarrollo porque hasta ahora sólo ha trabajado con pequeños programas. Con el tiempo se dará cuenta que las recomendaciones para organizar sus programas son tremendamente valiosas y que le ahorrarán mucho trabajo en el futuro. **Acostúmbrese a estructurar bien sus programas mientras sean pequeños, para que sea natural hacerlo cuando sean grandes.**

En esta sección estudiaremos una primera técnica para propiciar la mantenibilidad de los programas. Incidentalmente, para explicar esta técnica tendremos que introducir el concepto de *módulo* en Python.


## Separación de la lógica y la interfaz



Archivos diferentes / Módulos diferentes

Funciones de la lógica del programa


## Módulos en Python

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__. For instance, use your favorite text editor to create a file called fibo.py in the current directory with the following contents

## Funciones de la interfaz

En una sección anterior hablamos de la conveniencia de tener funciones sin parámetros o funciones sin retorno. En esta sección podemos retomar la discusión puesto que es precisamente en el módulo que implementa la interfaz de un programa donde tiene más sentido incluir este tipo de funciones.

### Funciones sin parámetros

Como dijimos antes, una función sin parámetros no tendría sentido dentro de la definición matemática de función. En el caso de Python, una función cuyo resultado no dependiera de ningún valor externo tampoco tendría mucho sentido; sería mucho más eficiente implementarlo como una constante.

Sin embargo, dentro del módulo de la interfaz sí puede ser conveniente tener funciones sin parámetros. Tomemos como ejemplo el siguiente fragmento de código:

```python
import libreria

def calcular_area_cuadrado() -> float:
    str_lado = input("Por favor indique el lado del cuadrado: ")
    lado = float(str_lado)
    area = libreria.calcular_area(lado)
    return area
```

En este programa tenemos una función sin parámetros que retorna un número decimal, pero ese número puede variar con cada ejecución. De hecho, el resultado de esta función depende completamente de algo externo: el valor que el usuario teclee cuando se ejecute la función.

Como dijimos, esta situación es muy frecuente dentro de los módulos que implementan la interfaz y que reciben información del usuario. Desconfíe de una función que no reciba parámetros y se encuentre mezclada con funciones que tengan que ver con la lógica de la aplicación.

 
### Funciones sin retorno
 
 - sin retorno

None



## Más allá de Python

La primera parte de esta sección introdujo algunos temas relativamente avanzados que tienen que ver con una gran área de trabajo dentro de la informática llamada *Ingeniería de Software*. La principal preocupación de esta área es cómo hacer para construir de forma eficiente software con calidad, lo cual implica considerar aspectos como la forma de estructurar el software, las metodologías de trabajo en los proyectos de desarrollo, las técnicas para diseñar interfaces que ofrezcan una buena experiencia a los usuarios, y hasta la psicología de los desarrolladores.

Es indudable que la selección de los lenguajes de programación que se usen tiene un impacto en muchos de los otros aspectos que son de interés para la Ingeniería de Software. Por ejemplo, el uso de un lenguaje como Python parece acelerar el desarrollo de programas pequeños pero complica el mantenimiento de programas grandes debido a factores como el uso de un sistema de tipado dinámico. 

Esto no quiere decir que no se pueda usar Python exitosamente para proyectos grandes. Lo que queremos decir es que la selección del lenguaje de programación debe tener en cuenta una gran cantidad de factores que van mucho más allá de cuál es el lenguaje de moda, cuál es el lenguaje que conocemos o cuál es el lenguaje que nos gustaría aprender. Todos los lenguajes tienen ventajas y desventajas que se deben sopesar cuidadosamente, y después de tomar una decisión cualquier proyecto debería introducir instrumentos para mitigar los riesgos o el impacto cuando se materialicen esos riesgos.

Por ejemplo, si se decide usar un lenguaje como Python o JavaScript para un gran proyecto, deberían definirse varias reglas desde el inicio para contrarrestar la dificultad para aplicar operaciones de *refactoring*.


#### Notas 

