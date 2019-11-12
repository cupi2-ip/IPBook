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
