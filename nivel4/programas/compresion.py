

def comprimir(cadena: str) -> tuple:
  tam = len(cadena)
  unos = []
  pos = 0
  while pos < len(cadena):
    if cadena[pos] == '0':
      pos += 1
    else:
      inicio = pos
      cantidad = 0
      while pos < len(cadena) and cadena[pos] == '1':
        cantidad += 1
        pos += 1
      unos.append((inicio, cantidad))
  return (tam, unos)


def descomprimir(compresion: tuple) -> str:
  resultado = ""
  tam, unos = compresion
  if len(unos)==0:
    resultado = '0'*tam
  else:
    actual = 0
    for posicion, cantidad in unos:
      nuevos_unos = '1' * cantidad
      ceros_faltantes = posicion - actual
      resultado += '0'*ceros_faltantes + nuevos_unos
      actual = posicion + cantidad
    if actual < tam:
      ceros_faltantes = tam - actual
      resultado += '0'*ceros_faltantes
  return resultado


c1 = "1110011100111"
c2 = "0000"
c3 = "1111"
c4 = "1"
c5 = "0"
c6 = "101101111000110"
c7 = "0001100111001111"
c8 = "01010101010101"

cadenas = [c1, c2, c3, c4, c5, c6, c7, c8]
