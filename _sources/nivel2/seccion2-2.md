
# Lógica y valores de verdad

```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```




```{admonition} Objetivo de la sección
El objetivo de esta sección es repasar conceptos fundamentales de lógica tales como el concepto de proposición, valor de verdad, conjunción, disyunción y negación. La sección presentará los conceptos desde el punto de vista de lógica matemática antes de que sean aplicados a Python en la siguiente sección.
```


Hasta el momento hemos trabajado en nuestros programas usando valores de tipo numéricos y con cadenas de caracteres. A partir de ahora vamos a usar también *valores de verdad*, es decir valores que sólo pueden ser verdaderos o falsos. Estos valores son también llamados valores lógicos o Booleanos (por el matemático George Boole) y se pueden operar utilizando las reglas del *álgebra Booleana*, en lugar de las reglas del álgebra elemental que usamos para valores numéricos.

En esta sección veremos cómo representar, manipular y operar con valores de verdad, haciendo un repaso rápido de lógica matemática, incluyendo las operaciones fundamentales y las leyes y propiedades que deben tenerse en cuenta para su manipulación.


## Valores de verdad y proposiciones

Una proposición es una expresión completa que tiene un valor de verdad, es decir que es verdadera o falsa. Por ejemplo, la frase 'Hoy está haciendo calor' es una proposición porque expresa una idea que puede ser verdadera o falsa. Evidentemente nosotros no podemos saber si, en el momento en que el lector vea esto, estará haciendo calor o no, pero el hecho de que no lo sepamos no hace que la frase deje de ser una proposición. Por el contrario, expresiones como 'azul', 'mañana' o 'cantando' no son frases completas, no se puede decir que sean verdaderas o falsas y por ende no pueden ser proposiciones. En español se suelen usar también los términos *sentencia*, *afirmación* o *juicio* para referirse a una proposición.

Cuando se usan proposiciones dentro del contexto de lógica matemática, se espera que tengan un valor de verdad que, como dijimos, puede ser **verdadero** o **falso**. Dependiendo del momento en que se evalúe, una proposición podría cambiar de valor (piense en la frase 'Hoy está haciendo calor'), pero no es posible que una proposición tenga dos valores diferentes al mismo tiempo.

Finalmente, debemos recalcar que los únicos dos valores de verdad son *verdadero* y *falso*, independientemente de cómo se representen. Por ejemplo, es usual que estos valores se representen con expresiones como *V* y *F*, *true* y *false*, *T* y *F* o incluso números como *1* y *0*. Sin embargo, en todos estos casos estamos hablando de los valores de verdad y no de expresiones de tipo numérico o de cadenas de caracteres.


## Álgebra Booleana

El álgebra Booleana es la rama del álgebra que trabaja con proposiciones y no  con valores numéricos como el álgebra elemental: en lugar de tener los números **0** y **1** y las operaciones de **adición** y **multiplicación** como elementos fundamentales, el álgebra Booleana se basa en los valores **verdadero** y **falso** y las operaciones $\land$ (**conjunción**), $\lor$ (**disyunción**) y $\lnot$ (**negación**). Debido a limitaciones en el formato de este libro, en lugar de usar siempre los símbolos usuales para estas operaciones, usaremos también las expresiones **and**, **or** y **not** para referirnos respectivamente a la **conjunción**, la **disyunción** y la **negación**.


### Operaciones lógicas y tablas de verdad

Como dijimos, son tres las operaciones básicas del álgebra Booleana. El resto de operaciones, como la implicación o la equivalencia, son operaciones secundarias que se pueden construir a partir de la conjunción, disyunción y negación.

1. **Negación**. La negación ($\lnot$, **not**, ***no***) es la operación Booleana que toma un valor de verdad y lo convierte en el otro valor. Es decir que la negación de un valor verdadero es un valor falso, y la negación de un valor falso es un valor verdadero. La negación es una operación *unaria*, que se aplica sobre un solo operando.

2. **Conjunción**. La conjunción ($\land$, **and**, ***y***) es una operación Booleana binaria que tiene valor verdadero sólo cuando ambos operandos tienen valor verdadero. Esto implica que cuando un operando es verdadero y el otro es falso, o cuando ambos operandos son falsos, el resultado de una conjunción es un valor falso.

3.  **Disyunción**. La disyunción ($\lor$, **or**, ***o***) es una operación Booleana binaria que tiene valor verdadero cuando por lo menos uno de los operandos tiene valor verdadero. Esto implica que una disyunción tiene valor falso sólo cuando ambos operandos tienen valor falso.

Veamos ahora algunos ejemplos de estas operaciones aplicadas a proposiciones sencillas en Español. Para esto lo primero que vamos a definir son tres proposiciones que identificaremos con las letras *P*, *Q* y *R*.

* P: Hoy está haciendo calor
* Q: Hoy es martes
* R: Hoy es un día de fiesta

Las siguientes son 6 expresiones lógicas basadas en las 3 proposiciones y en los operadores lógicos. Para cada expresión se presenta también una "traducción" lo más directa posible a una frase en Español.

1. **Q**: Hoy es martes.
2. **$\lnot$ P**: Hoy no está haciendo calor
3. **$\lnot$ Q**: Hoy no es martes
4. **P $\land$ Q**: Hoy está haciendo calor y es martes
5. **Q $\land$ $\lnot$ R**: Hoy es martes y no es un día de fiesta
6. **P $\lor$ R**: Hoy está haciendo calor o es un día de fiesta

A continuación, analizamos estas expresiones una por una.

1. La primera expresión será verdadera sólo cuando sea evaluada un día que sea martes; de lo contrario, será falsa. 
2. La segunda expresión será verdadera sólo cuando sea evaluada un día en que no haga calor. Esto quiere decir que la expresión **$\lnot$ P** será verdadera sólo cuando la expresión **P** sea falsa. De igual forma, **$\lnot$ P** será falsa sólo cuando la expresión **P** sea verdadera.
3. La tercera expresión es similar y será verdadera sólo cuando sea evaluada un día que no sea martes.
4. La cuarta expresión usa una conjunción y será verdadera sólo cuando **P** y **Q** sean verdaderas simultáneamente. Es decir, cuando sea evaluada un día en que esté haciendo calor y también sea martes. Si cualquiera de las dos partes es falsa, o si las dos son falsas, entonces la conjunción será falsa.
5. La quinta expresión usa también una conjunción, pero en este caso será verdadera sólo cuando **Q** sea verdadera y cuando **$\lnot$ R** sea verdadero, es decir cuando **R** sea falso. En otras palabras, será verdadera sólo cuando se evalúe un martes que no sea día de fiesta. Si se evalúa cualquier otro día de la semana, o si se evalúa un martes que además sea día de fiesta, entonces la expresión será falsa.
6. La sexta expresión es la que tiene una interpretación lógica que podría estar más alejada de lo que dice la intuición. En este caso se está usando una disyunción, así que tendrá un valor verdadero cuando al menos uno de los operandos sea verdadero. Esto quiere decir que la expresión será verdadera cuando esté haciendo calor (**P**) o cuando sea un día de fiesta (**R**). Si las dos partes son verdaderas (está haciendo calor y es un día de fiesta), la expresión también será verdadera. La expresión sólo será falsa cuando las dos partes sean falsas simultáneamente, es decir cuando **P** sea falsa y **R** sea falsa, o cuando **$\lnot$ P** sea verdadera y **$\lnot$ R** también sea verdadera. 

Expresiones similares a este último ejemplo a veces se interpretan equivocadamente como si hubiera un *"o exclusivo"* que sólo sería verdadero cuando una de las expresiones fuera verdadera y la otra fuera falsa. Existe un operador para expresar esta relación usualmente llamado *xor*, el cual se puede construir a partir de operaciones de conjunción, disyunción y negación.


#### Ejercicios

1. Escriba la "traducción" más clara posible a español de las siguientes expresiones y analice en qué casos sería verdadera y en qué casos sería falsa:

	  *  **Q $\lor$ R**
	  *  **$\lnot$ P $\land$ $\lnot$ R**
	  *  **Q $\land$ Q**
	  *  **Q $\land$ $\lnot$ Q**
	  *  **P $\land$ (Q $\lor$ R)**
	  *  **(P $\land$ Q) $\lor$ R**
	  *  **(P $\land$ $\lnot$ R) $\lor$ ($\lnot$ P $\land$ R)**
 

2. Escriba las expresiones equivalentes a las siguientes proposiciones en español, usando los 3 identificadores P, Q y R.

	  *  Hoy no es martes
	  *  Hoy no es martes o hoy es martes
	  *  Hoy está haciendo calor o es martes o es un día de fiesta
	  *  Hoy ni es martes ni es un día de fiesta

  
3. Simplifique las siguientes expresiones (escríbalas de una forma más breve) si es posible:

	  *  **Q $\land$ Q**
	  *  **Q $\land$ $\lnot$ Q**
	  *  **Q $\land$ Verdadero**
	  *  **Q $\land$ Falso**
	  *  **Q $\lor$ Verdadero**
	  *  **Q $\lor$ Falso**
	  *  **$\lnot$ Q $\land$ $\lnot$ Q**
	  *  **$\lnot$ Q $\lor$ $\lnot$ Q**
	  *  **$\lnot$(Q $\lor$ P)**
	  *  **$\lnot$(Q $\land$ P)**
	  *  **(P $\land$ Q) $\lor$ (P $\land$ R)**


### Tablas de verdad

Para estudiar el comportamiento de una expresión es usual que se utilice algo llamado una tabla de verdad. Esta no es más que una representación sencilla que nos permite analizar todos los valores posibles de una expresión, en función de los valores de las proposiciones simples involucradas. 

Consideremos la tabla más sencilla posible, en la cual sólo tenemos la proposición P [^TF].

[^TF]: Para mantener las tablas relativamente pequeñas, usaremos T para valores verdaderos y F para valores falsos.


P   | $\lnot$ P |
:----:|:------:|
  T |  F  
F   |  T  

Aunque sencilla, esta tabla es interesante porque nos muestra todos los posibles valores de la expresión **P** y los valores correspondientes que tendría la expresión **$\lnot$ P**. También nos muestra que las dos expresiones no pueden ser verdaderas simultáneamente, sino que tienen valores opuestos. Si extendemos la tabla con un par de expresiones encontraremos dos principios muy importantes:

P   | $\lnot$ P | P $\land$ $\lnot$ P | P $\lor$ $\lnot$ P |
:----:|:------:|:-----:|:-----:|
T   |   F  |  F  |  T  
F   |   T  |  F  |  T  

En primer lugar, vemos que la expresión **P $\land$ $\lnot$ P** siempre es falsa. Esto quiere decir que no es posible que una proposición sea simultáneamente verdadera y falsa, lo cual usualmente se conoce como el principio de no contradicción.

En segundo lugar, vemos que la expresión **P $\lor$ $\lnot$ P** siempre es verdadero. Esto quiere decir que siempre bien sea una proposición o su negación tienen que ser verdaderas. Como no hay una tercera opción, eso se conoce como el principio del tercero excluido.

La siguiente tabla de verdad es un poco más compleja porque involucra dos proposiciones.

P   |  Q  |  P $\land$ Q  |  P $\lor$ Q  |
:----:|:-----:|:-----------:|:----------:|
T   |  T  |     T     |    T     
T   |  F  |     F     |    T     
F   |  T  |     F     |    T     
F   |  F  |     F     |    F     

Acá podemos ver, de otra manera, lo que ya sabíamos sobre la conjunción y la disyunción: una conjunción es verdadera sólo cuando los dos operandos son verdaderos y una disyunción es falsa sólo cuando los dos operandos son falsos.


### Leyes fundamentales

Así como en el álgebra elemental hay algunas leyes muy importantes y conocidas (conmutatividad, asociatividad, distribución, precedencia de operadores, etc.), en el álgebra Booleana también hay algunas leyes importantes que se deben tener en cuenta y pueden servir para replantear expresiones de formas que sean más sencillas.

1. **Conmutatividad**: Tanto la conjunción como la disyunción son conmutativas, así que **A $\lor$ B** es equivalente a **B $\lor$ A**. También es cierto que **A $\land$ B** es equivalente a **B $\land$ A** [^conm]. 

2. **Asociatividad**: Tanto la conjunción como la disyunción son asociativas, así que **A $\lor$ (B $\lor$ C)** es equivalente a **(A $\lor$ B) $\lor$ C**. Además, **A $\land$ (B $\land$ C)** es equivalente a **(A $\land$ B) $\land$ C** [^assoc].

3. **Distribución**: en el álgebra Booleana, la conjunción distribuye sobre la disyunción y viceversa [^dist]. Esto quiere decir que:
    * **A $\land$ (B $\lor$ C) $\equiv$ (A $\land$ B) $\lor$ (A $\land$ C)**
    * **A $\lor$ (B $\land$ C) $\equiv$ (A $\lor$ B) $\land$ (A $\lor$ C)**  


4. **Identidad de la conjunción**: si se hace una conjunción con el valor verdadero, el resultado es el mismo. Es decir que **A $\land$ Verdadero $\equiv$ A** [^ident].

5. **Identidad de la disyunción**: si se hace una disyunción con el valor falso, el resultado es el mismo. Es decir que **A $\lor$ Falso $\equiv$ A**.

6. **Dominación de la conjunción**: si se hace una conjunción con el valor falso, el resultado es falso. Es decir que **A $\land$ Falso $\equiv$ Falso** [^dom].

7. **Dominación de la disyunción**: si se hace una disyunción con el valor verdadero, el resultado es verdadero. Es decir que **A $\lor$ Verdadero $\equiv$ Verdadero**.

Finalmente, proponemos la siguiente equivalencia que, aunque no tiene un nombre común, es de uso extremadamente frecuente y de mucha utilidad cuando se está empezando a programar:

* **Negación y equivalencia a falso**: es lo mismo decir que una proposición tiene un valor falso que decir que su negación tiene un valor positivo. Es decir que **A $\equiv$ Falso** es lo mismo que decir **$\lnot$ A $\equiv$ Verdadero**. Más aún, **B $\equiv$ Verdadero** es lo mismo que decir **B**, así que **A $\equiv$ Falso** se puede reescribir como **$\lnot$ A**.


[^conm]: En el álgebra elemental tanto la adición como la multiplicación son conmutativas.

[^assoc]: En el álgebra elemental tanto la adición como la multiplicación son asociativas. Es decir que **a + (b + c)** es igual a **(a + b) + c**.

[^dist]: El álgebra elemental, la multiplicación distribuye sobre la adición, pero no al contario. Es decir que **a $\times$(b+c)=a$\times$b + a$\times$c**, pero la ecuación no se mantiene si se intercambian las operaciones. 

[^ident]: Esto es equivalente a multiplicar por 1 o a sumar 0.

[^dom]: Esto es equivalente a multiplicar por 0. No existe algo similar para la adición.



### Leyes de De Morgan

Finalizamos este repaso de lógica con dos teoremas muy importantes que se deben tener muy en cuenta cuando se estén reescribiendo operaciones lógicas.

Las leyes o teoremas de De Morgan dicen que:

* **$\lnot$ (P $\land$ Q) $\equiv$ $\lnot$ P $\lor$ $\lnot$ Q**
* **$\lnot$ (P $\lor$ Q) $\equiv$ $\lnot$ P $\land$ $\lnot$ Q**

Volviendo a las proposiciones de ejemplo que usamos anteriormente, la expresión **$\lnot$ (P $\land$ Q)** podría "traducirse" como "no es cierto que (hoy está haciendo calor y hoy es martes)". Hemos agregado los paréntesis para hacer notar que las palabras "no es cierto que" hacen referencia a las dos cláusulas subordinadas. 

Sabemos que la expresión completa será verdadera sólo cuando la parte que está entre paréntesis sea falsa para que la negación invierta su valor. Es decir que la expresión completa será verdadera cuando sea falso que "hoy está haciendo calor y hoy es martes". En este caso tenemos una conjunción, así que la operación será verdadera sólo cuando ambas sean falsas. Como en este caso nos interesa que sea falsa, decimos que la operación de conjunción será falsa cuando cualquiera de las dos partes sea falsa, es decir cuando la primera parte sea falsa **o** la segunda parte sea falsa. Volviendo a la expresión completa, encontramos que la expresión será verdadera cuando la proposición **P** sea falsa o cuando la proposición **Q** sea falsa.

Esto quiere decir que la expresión original también podría haberse traducido de forma equivalente como "no es cierto que hoy esté haciendo calor o no es cierto que hoy sea martes".

La segunda propiedad es análoga a la primera.


## Ejercicios

1. Construya una tabla de verdad para verificar cada una de las leyes de De Morgan. Para la primera, necesitará una columna para **P**, una para **Q**, una para **$\lnot$ (P $\land$ Q)** y una para **$\lnot$ P $\lor$ $\lnot$ Q**. Debería encontrar exactamente los mismos valores en las últimas dos columnas. Para facilitar el trabajo, también le recomendamos agregar una columna con los valores de las expresiones **$\lnot$ P**, **$\lnot$ Q**, **P $\land$ Q** y **P $\lor$ Q**.

2. En un ejercicio anterior se le pidió simplificar unas expresiones. Vuelva a hacer el ejercicio construyendo una tabla de verdad para cada caso y aplicando las leyes que se vieron al final de esta sección.

3. Como vimos, el álgebra booleana se define en términos de dos valores y tres operaciones (conjunción, disyunción y negación). Otras operaciones lógicas pueden definirse como composiciones de las operaciones básicas. Por ejemplo, la operación **xor**, que es verdadera sólo cuando exactamente uno de los operandos es verdadero, se puede definir como: **P xor Q $\equiv$ (P $\land$ $\lnot$ Q) $\lor$ (Q $\land$ $\lnot$ P)**.
Defina cada una de las siguientes operaciones y para cada una construya una tabla de verdad que muestre su comportamiento y le sirva para verificar su definición.

  * xor (or exclusivo): es verdadero cuando exactamente un operando es verdadero.
  * == (equivalencia): es verdadero cuando los operandos tienen el mismo valor.
  * != (desigualdad): es verdadero cuando los operandos tienen valores diferentes.
  * nand: es falso sólo cuando los dos operandos son verdaderos.
  * nor: es verdadero sólo cuando los dos operandos son falsos.

 

