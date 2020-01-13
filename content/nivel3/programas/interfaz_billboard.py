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