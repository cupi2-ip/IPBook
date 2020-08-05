
def factorial(n: int) -> int:
  resultado = 1
  actual = 1
  while actual <= n:
    resultado = resultado * actual
    actual += 1
  return resultado