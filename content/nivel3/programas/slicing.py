
def extraer_slice(elementos: list, inicio: int, fin: int, paso: int) -> list:
  """ Extrae un slice de una lista
  Parámetros:
    elementos (list): la lista de la que se van a extraer los elementos
    inicio (int): la primera posición desde la que se van a extraer los elementos. Puede ser un número negativo.
    fin (int): la última posición de la que se van a extraer los elementos. Puede ser un número negativo.
    paso (int): indica cada cuántas posiciones se va a extraer un elemento.
  Retorno:
    (list): Una lista con los elementos extraídos desde 'inicio' hasta 'fin', donde los elementos extraídos están separados por 'paso' posiciones.
  """
  tam = len(elementos)
  # Ajustar la posición inicial si se usó un valor negativo
  if inicio < 0:
    inicio = tam + inicio
  inicio = max(0, inicio)
  inicio = min(inicio, tam-1)
  # Ajustar la posición final si se usó un valor negativo
  if fin < 0:
    fin = tam + fin
  # Preparar la lista resultante
  extraccion = []
  posicion = inicio
  # El ciclo se repite mientras siga siendo posible avanzar desde
  # la posición actual hacia la posición final
  while (posicion >= 0 and posicion < tam) and ((posicion < fin and paso > 0) or (posicion > fin and paso < 0)):
    extraccion.append(elementos[posicion])
    posicion += paso  
  return extraccion