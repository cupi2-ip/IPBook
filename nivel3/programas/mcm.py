def minimo_comun_multiplo(a: int, b:int) -> int:
  maximo = a * b
  multiplos_a = [False] * (maximo+1)
  multiplos_a[a::a] = [True]*b
  multiplos_b = [False] * (maximo+1)
  multiplos_b[b::b] = [True] * a
  encontre_mcm = False
  candidato_mcm = max(a,b)
  while not encontre_mcm:
    if multiplos_a[candidato_mcm] and multiplos_b[candidato_mcm]:
      encontre_mcm = True
    else:
      candidato_mcm += 1
  return candidato_mcm


def minimo_comun_multiplo_zip(a: int, b:int) -> int:
  maximo = a * b
  multiplos_a = [False] * (maximo+1)
  multiplos_a[a::a] = [True]*b
  multiplos_b = [False] * (maximo+1)
  multiplos_b[b::b] = [True] * a
  parejas = list(zip(multiplos_a, multiplos_b))
  candidato_mcm = parejas.index((True, True))
  return candidato_mcm
