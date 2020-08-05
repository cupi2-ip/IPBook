import random

numero_buscado = 6
numero_intentos = 0
encontre_numero = False
while not encontre_numero:
  numero_intentos += 1
  nuevo_numero = random.randint(1, 6)
  if nuevo_numero == numero_buscado:
    encontre_numero = True

print("Encontré el número", numero_buscado, "después de", numero_intentos, "intentos")




import random

def buscar_numero(numero_buscado: int)->int:
  numero_intentos = 0
  encontre_numero = False
  while not encontre_numero:
    numero_intentos += 1
    nuevo_numero = random.randint(1, 6)
    if nuevo_numero == numero_buscado:
      encontre_numero = True
  return numero_intentos

def buscar_numero_dos_dados(numero_buscado: int)->int:
  numero_intentos = 0
  encontre_numero = False
  while not encontre_numero:
    numero_intentos += 1
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    if dado1 + dado2 == numero_buscado:
      encontre_numero = True
  return numero_intentos





print("Encontré el número", numero_buscado, "después de", numero_intentos, "intentos")


def probar(intentos, numero) -> int:
  total = 0
  i = 0
  while i < intentos:
    i += 1
    total += buscar_numero(numero)
  return total / intentos


def probar2(intentos, numero) -> int:
  total = 0
  i = 0
  while i < intentos:
    i += 1
    total += buscar_numero_dos_dados(numero)
  return total / intentos


def correr_pruebas(tam:int) -> int:
  for i in range(2, 13):
    intentos = probar2(tam, i)
    print(i, intentos)

def probar_dados(numero, iteraciones) -> int:
  total_lanzamientos = 0
  i = 0
  while i < iteraciones:
    cantidad = buscar_numero_dos_dados(numero)
    total_lanzamientos += cantidad
    i += 1
  return total_lanzamientos / iteraciones


import math

def seno_v1(x:float) -> float:
  iteraciones = 5
  suma = 0
  n = 0
  while n < iteraciones:
    signo = 1 if n % 2 == 0 else -1
    denom = math.factorial(2*n + 1)
    mult = pow(x, 2*n + 1)
    suma += (signo*mult/denom)
    n += 1
  return suma

def probar(angulo: float) -> None:
  res = seno_v1(angulo)
  real = math.sin(angulo)
  error = res - real
  print("Ángulo:", round(angulo, 2), "Calculado:", round(res, 2), "Real:", round(real, 2), "Error:", round(error, 4))

probar(0)
probar(math.pi/6)
probar(math.pi/3)
probar(math.pi/2)
probar(math.pi)

probar(math.pi * 1.5)
probar(math.pi * 2)
probar(math.pi * 2.5)
probar(math.pi * 3)
probar(math.pi * 4)



def seno_v2(x:float, epsilon: float) -> float:
  suma = 0
  suma_anterior = -1
  n = 0
  while abs(suma - suma_anterior) > epsilon:
    signo = 1 if n % 2 == 0 else -1
    denom = math.factorial(2*n + 1)
    mult = pow(x, 2*n + 1)
    suma_anterior = suma
    suma += (signo*mult/denom)
    n += 1
  print("Fueron", n, "iteraciones")
  return suma


def probar2(angulo: float) -> None:
  res = seno_v2(angulo, 0.01)
  real = math.sin(angulo)
  error = res - real
  print("Ángulo:", round(angulo, 2), "Calculado:", round(res, 2), "Real:", round(real, 2), "Error:", round(error, 4))


def seno_v3(x:float, epsilon: float) -> float:
  suma = 0
  suma_anterior = -1
  n = 0
  while abs(suma - suma_anterior) > epsilon:
    signo = 1 if n % 2 == 0 else -1
    denom = math.factorial(2*n + 1)
    mult = pow(x, 2*n + 1)
    suma_anterior = suma
    termino = signo*mult/denom
    print(termino)
    suma += (termino)
    n += 1
  print("Fueron", n, "iteraciones")
  return suma


