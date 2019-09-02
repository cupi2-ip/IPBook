---
title: 'Un programa para leer'
prev_page:
  url: /nivel2/intro
  title: 'Nivel 2'
next_page:
  url: /nivel2/seccion2-2
  title: 'Lógica y valores de verdad'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
Versión borrador / preliminar |
-------------------|
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores|


# Un programa para leer

Como dijimos en el primer capítulo, una habilidad importante que se debe desarrollar es la capacidad para leer código escrito por alguien más. En esta sección presentamos un nuevo ejemplo para que se ejercite y para que también observe varias de las características de Python que se van a estudiar en este nivel.

Al igual que en el nivel 1, el programa no tiene comentarios para que el ejercicio de lectura sea más exigente pero también más útil. Un programa tan largo como este normalmente tendría una buena cantidad de comentarios.


## Lógica de la aplicación

El siguiente es el contenido completo del módulo `logica_juego1`.

```python
import random

def mano_nueva()->dict:
    mano = {'carta1': carta_nueva(), 'carta2': carta_nueva(), 'tam': 2}
    return mano

def carta_nueva()->dict:
    palo = nombre_palo(random.randint(1,4))
    valor = random.randint(1,13)
    nombre_carta = "{} de {}".format(nombre_valor(valor), palo)
    carta = {"palo": palo, "valor": valor, "nombre" : nombre_carta}
    return carta

def agregar_carta(mano: dict)->dict:
    tam_actual = mano['tam']
    nueva_carta = carta_nueva()
    nueva_llave = 'carta{}'.format(tam_actual + 1)
    mano[nueva_llave] = nueva_carta
    mano['tam'] = tam_actual + 1
    return nueva_carta


def nombre_palo(num_palo: int)->str:
    nombre = "Picas"
    if num_palo == 2:
        nombre = "Corazones"
    elif num_palo == 3:
        nombre = "Tréboles"
    elif num_palo == 4:
        nombre = "Diamantes"
    return nombre


def nombre_valor(valor: int)->str:
    nombre = str(valor)
    if valor == 1:
        nombre = "AS"
    elif valor == 11:
        nombre = "J"
    elif valor == 12:
        nombre = "Q"
    elif valor == 13:
        nombre = "K"
    return nombre


def contar_puntos_mano(mano: dict)->int:
    puntos = contar_puntos_carta(mano, 1)
    puntos += contar_puntos_carta(mano, 2)
    puntos += contar_puntos_carta(mano, 3)
    puntos += contar_puntos_carta(mano, 4)
    puntos += contar_puntos_carta(mano, 5)
    return puntos


def contar_puntos_carta(mano: dict, numero_carta: int)->int:
    puntos = 0
    llave = "carta{}".format(numero_carta)
    if llave in mano:
        carta = mano[llave]
        valor = carta["valor"]
        if valor == 1:
            puntos = 11
        elif valor > 10:
            puntos = 10
        else:
            puntos = valor        
    return puntos


def casa_debe_continuar(mano_casa: dict)->bool:
    puntos_casa = contar_puntos_mano(mano_casa)
    return puntos_casa < 16 or puntos_casa > 21
```

**Preguntas:**
A partir de su lectura del programa, intente responder las siguientes preguntas. No se preocupe si no está seguro de algo, al final del nivel todas sus dudas deberían haber quedado aclaradas.

* ¿Cuál cree que es el objetivo del programa?
* ¿Cuál es el objetivo de cada bloque?
* ¿Qué elementos de la sintaxis utilizada no conoce todavía?


## Interfaz de la aplicación

El siguiente es el contenido completo del módulo `interfaz_juego1`.

```python
import logica_juego1 as juego

def mostrar_menu()->int:
    print("\n¿Cómo quiere continuar?")
    print("  1. Quiero otra carta")
    print("  2. No quiero más cartas")
    respuesta = input("Seleccione una opción: ")
    if respuesta.isnumeric():
        opcion = int(respuesta)
        if opcion != 1 and opcion != 2:
            print("Sólo podía seleccionar 1 o 2. Suponemos que no quiere más cartas")
            opcion = 2            
    else:
        print("Sólo podía seleccionar 1 o 2. Suponemos que no quiere más cartas")
        opcion = 2
    return opcion


def mostrar_primera_carta(mano: dict)->None:
    plantilla = "La mano tiene {} cartas y está mostrando un {}"
    print(plantilla.format(mano['tam'], mano['carta1']['nombre']))


def mostrar_mano_abierta(mano: dict)->None:
    num_cartas = mano['tam']
    puntos_mano = juego.contar_puntos_mano(mano)
    plantilla = "La mano tiene {} cartas y vale {} puntos"
    print(plantilla.format(num_cartas, puntos_mano))
    print("  La primera carta es: ", mano['carta1']['nombre'])
    print("  La segunda carta es: ", mano['carta2']['nombre'])

    if num_cartas >= 3:
        print("  La tercera carta es: ", mano['carta3']['nombre'])

    if num_cartas >= 4:
        print("  La cuarta carta es: ", mano['carta4']['nombre'])

    if num_cartas >= 5:
        print("  La quinta carta es: ", mano['carta5']['nombre'])


def mostrar_juego_actual(mano_jugador: dict, mano_casa: dict, abrir_casa: bool = False):
    print("MANO JUGADOR")
    mostrar_mano_abierta(mano_jugador)
    print("MANO CASA")
    if abrir_casa:
        mostrar_mano_abierta(mano_casa)
    else:
        mostrar_primera_carta(mano_casa)


def turno_jugador(mano_jugador: dict, mano_casa: dict)->bool:
    continuar_juego = True
    opcion = mostrar_menu()
    if opcion == 2:
        continuar_juego = False
    else:
        nueva = juego.agregar_carta(mano_jugador)
        print("Tu nueva carta es: ", nueva['nombre'])
        mostrar_juego_actual(mano_jugador, mano_casa)
        puntos_mano = juego.contar_puntos_mano(mano_jugador)
        if puntos_mano > 21:
            print("\nTienes más de 21 puntos: ¡Perdiste!")
            continuar_juego = False
        elif puntos_mano == 21:
            print("\nTienes exactamente 21 puntos: esperemos que la casa no tenga lo mismo.\n")
            continuar_juego = False
            
    return continuar_juego


def turno_casa(puntos_jugador: int, mano_casa: dict)->bool:
    continuar_juego = True
    puntos_casa = juego.contar_puntos_mano(mano_casa)
    if puntos_casa > puntos_jugador:
        print("La casa gana: {1} de la casa vs {0} del jugador".format(puntos_jugador, puntos_casa))
        continuar_juego = False
    else:
        if juego.casa_debe_continuar(mano_casa):
            nueva = juego.agregar_carta(mano_casa)
            print("La casa saca otra carta ... {}".format(nueva['nombre']))
            mostrar_mano_abierta(mano_casa)
            
        puntos_casa = juego.contar_puntos_mano(mano_casa)
        if puntos_casa > 21:
            print("\nLa casa tiene más de 21: ¡el jugador gana!\n")
            continuar_juego = False
        elif puntos_casa == 21:
            print("\nLa casa tiene 21: ¡la casa gana!\n")
            continuar_juego = False
    
    return continuar_juego


def iniciar_aplicacion()->None:
    mano_jugador = juego.mano_nueva()
    mano_casa = juego.mano_nueva()
    mostrar_juego_actual(mano_jugador, mano_casa)

    continuar_juego = True

    # tercera carta del jugador
    if continuar_juego:
        continuar_juego = turno_jugador(mano_jugador, mano_casa)

    # cuarta carta del jugador
    if continuar_juego:
        continuar_juego = turno_jugador(mano_jugador, mano_casa)

    # quinta carta del jugador
    if continuar_juego:
        continuar_juego = turno_jugador(mano_jugador, mano_casa)

    puntos_jugador = juego.contar_puntos_mano(mano_jugador)
    if puntos_jugador <= 21:
        mostrar_juego_actual(mano_jugador, mano_casa, True)
        print("\nEs el turno de la casa de jugar\n")
        continuar_juego = True
        
    # tercera carta de la casa
    if continuar_juego:
        continuar_juego = turno_casa(puntos_jugador, mano_casa)

    # cuarta carta de la casa
    if continuar_juego:
        continuar_juego = turno_casa(puntos_jugador, mano_casa)
    
    # quinta carta de la casa
    if continuar_juego:
        continuar_juego = turno_casa(puntos_jugador, mano_casa)

    puntos_casa = juego.contar_puntos_mano(mano_casa)
    if puntos_casa < puntos_jugador and puntos_jugador <= 21:
        print("¡Ganaste!: tienes {} puntos vs {} puntos de la casa".format(puntos_jugador, puntos_casa))


iniciar_aplicacion()
```

**Preguntas:**
A partir de su lectura del programa, intente responder las siguientes preguntas. No se preocupe si no está seguro de algo, al final del nivel todas sus dudas deberían haber quedado aclaradas.

* ¿Cuál cree que es el objetivo del programa?
* ¿Qué información tendrá que suministrar el usuario que ejecute el programa?
* ¿Cuál es el objetivo de cada bloque?
* ¿Qué es lo que primero se ejecuta?

