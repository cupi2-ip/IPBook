def extraer_slice(elementos: list, inicio: int, fin: int, paso: int) -> list:
  """ Extrae un slice de una lista.
  Parámetros:
    elementos (list): la lista de la que se van a extraer los elementos.
    inicio (int): la primera posición desde la que se van a extraer los elementos. Puede ser un número negativo.
    fin (int): la última posición de la que se van a extraer los elementos. Puede ser un número negativo.
    paso (int): indica cada cuántas posiciones se va a extraer un elemento. Puede ser un número negativo.
  Retorno:
    (list): Una lista con los elementos extraídos desde 'inicio' hasta 'fin', donde los elementos extraídos están separados por 'paso' posiciones.
  """
  tam = len(elementos)
  # Si la posición inicial es negativa, se busca el número positivo equivalente
  if inicio < 0:
    inicio = tam + inicio
  # Asegurar que el inicio siempre esté dentro de la lista
  inicio = max(0, inicio) 
  inicio = min(inicio, tam-1)
  # Si la posición final es negativa, se busca el número positivo equivalente
  if fin < 0:
    fin = tam + fin

  # Preparar la lista resultante
  slice = []
  posicion = inicio
  # El ciclo se repite mientras siga siendo posible avanzar desde
  # la posición actual hacia la posición final y se estén consultando
  # posiciones que estén dentro de la lista
  while (posicion >= 0 and posicion < tam) and \
        ((posicion < fin and paso > 0) or (posicion > fin and paso < 0)):
    slice.append(elementos[posicion])
    posicion += paso  
  return slice
