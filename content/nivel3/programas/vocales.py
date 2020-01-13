
def contar_vocales(cadena: str)->str:
  cadena = cadena.lower()
  a = cadena.count('a')
  e = cadena.count('e')
  i = cadena.count('i')
  o = cadena.count('o')
  u = cadena.count('u')
  mayor = 'a'
  cant_mayor = a
  if e > cant_mayor:
    mayor = 'e'
    cant_mayor = e
  if i > cant_mayor:
    mayor = 'i'
    cant_mayor = i
  if o > cant_mayor:
    mayor = 'o'
    cant_mayor = o
  if u > cant_mayor:
    mayor = 'u'
    cant_mayor = u
  return mayor

print(contar_vocales('aaa'))
print(contar_vocales('aeeiiiooouuuu'))
print(contar_vocales('uoiea'))
print(contar_vocales('Uuuuyyyyyy!!!'))
print(contar_vocales('¡Oe Oe Oooeeeea!'))
print(contar_vocales('Esto no es ni una prueba ni un simulacro'))





