
# Ejercicios adicionales

```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```

## Solución de problemas

1. **Enunciado:** Durante un juego de cartas, un apostador principiante desea hacer algo de trampa para mejorar su juego. Para esto tiene dos cartas escondidas y podrá tomar una de ellas dependiendo de la carta que ya tenga en la mano. Para escoger la carta con la que hará trampa, el apostador comparará la carta que tiene en la mano (`carta_mano`) con las dos opciones de cambio (`opcion_1` y `opcion_2`). Al apostador le serviría una carta que tenga el mismo número de la carta que tiene en la mano o una que tenga el mismo palo.

	  *  Si las dos cartas escondidas le sirven, el apostador siempre escogerá la primera opción.
	  *  Si ninguna de las dos cartas escondidas tiene el mismo número o el mismo palo que la de la mano, entonces el apostador no hará trampa.
	  
    Usted debe construir una función que indique la opción que debería escoger el apostador: `1` para la primera carta escondida, `2` para la segunda carta escondida, o `0` si ninguna carta le ayuda al apostador. Cada carta será representada por un diccionario con las llaves `"numero"` y `"palo"`. Tenga en cuenta que la llave `"numero"` también puede tener asociadas las letras `'J'`, `'Q'`, `'K'` y `'A'`.

2. **Enunciado:** Los cajeros automáticos usualmente tienen restricciones sobre las claves (numéricas) que pueden usarse para retirar. Usted debe construir una función que diga si una clave dada (un número entero con 4 dígitos cuyo primer dígito no es el 0) es permitida de acuerdo a las siguientes reglas:

      * El mismo dígito no puede aparecer más de dos veces.
      * No puede haber dígitos consecutivos.
      * No puede haber números que empiecen por `19`, `200` ni `201`.
      * El número debe tener al menos tres dígitos diferentes.

3. **Enunciado:** Usted ha sido encargado de escribir una función que decida si una contraseña es lo suficientemente segura para un nuevo sistema. Una contraseña segura debe tener al menos 10 caracteres y cumplir con al menos 3 de las siguientes restricciones adicionales:

      * Debe tener al menos una letra mayúscula y una letra minúscula.
      * Debe tener al menos un dígito.
      * Debe tener al menos uno de los siguientes caracteres: `!"@$ %&/()=?#`
      * No puede empezar ni terminar con un espacio.

4. **Enunciado:** Escriba una función que reciba 3 diccionarios que representen las coordenadas de 3 puntos en el espacio. Cada diccionario tendrá dos llaves, `"x"` y  `"y"`, que tendrán asociadas los respectivos componentes de cada coordenada. Su función debe retornar un valor de verdad que indique si los tres puntos se encuentran sobre la misma recta o no.

5. **Enunciado:**  El juego de las Picas y Fijas es un juego matemático muy sencillo, que consiste en adivinar un número de 4 cifras cuyos dígitos son todos diferentes. Para esto, el jugador que intenta adivinar deberá decir el número que cree está escondiendo el otro, y este deberá responder el número de picas y fijas que tiene ahora el jugador.

    Una *pica* es un dígito que se encuentra en el número a adivinar pero no está en el lugar correcto, y una *fija* es un dígito correctamente colocado.

    Por ejemplo, si el número a adivinar es `1234`, y otro jugador dice `1325`, tendrá dos picas y una fija.

    Usted debe crear una función que devuelva un diccionario con las llaves `"PICAS"` y `"FIJAS"` que represente el resultado de la jugada si un jugador trata de adivinar el `numero_secreto` con el número `intento`.
