
# Ejercicios adicionales

```{admonition} Versión borrador / preliminar
:class: warning
Este documento es una versión preliminar para uso interno. Si encuentra algún problema o error, o si tiene algún comentario por favor repórtelo a los autores.
```




## Conceptos básicos

1. Defina y dé un ejemplo para cada uno de los siguientes conceptos que se estudiaron en este capítulo:

	  * Tipo de datos
	  * Variable
	  * Expresión
	  * Operador
	  * Función 
	  * Parámetro

2. ¿Qué tipo de dato utilizaría para representar cada uno de los siguientes elementos?

	  * El nombre de una persona
	  * El número de identificación de una persona
	  * La edad de una persona
	  * El cilindraje del motor de un carro
	  * La capacidad en litros del baúl de un carro
	  * El año de fabricación de un carro
	  * La marca de un carro

## Lectura de programas

¿Qué imprimen los siguientes programas? Intente predecir qué van a imprimir los siguientes programas y depués copie el código al intérprete de Python y verifique sus respuestas.

```{code-block} python
v1 = 5
v2 = 1 + v2
v3 = v1 + v2
v4 = v3 / (4 + 1)
print("v4:", v4)
```

```{code-block} python
v1 = 5
v2 = v1 ** 2
v2 = v1 + v2
print("v2:", v2)
```


```{code-block} python
v1 = '5'
v2 = v1 * 3
print("v2:", v2)
```

```{code-block} python
v1 = '5'
v2 = v1 * 3
v3 = v1 + v2
print("v3:", v3)
```

```{code-block} python
v1 = '5'
v2 = v1 * 3
v3 = v1 + v2 + 9
print("v3:", v3)
```

```{code-block} python
v1 = 124
v2 = v1 // 3
v3 = v1 % 3
print("124/3:", v2, v3)
```

## Búsqueda de errores

Revise con atención los siguientes enunciados y el programa que intenta resolverlos. Explique cuál es el problema del programa y corríjalo.

*Ayuda:* Si no encuentra los problemas leyendo el código, copie los programas a su IDE y ejecútelos para intentar diagnosticar los problemas. Para esto tendrá que identificar valores de los parámetros que le sean útiles y posiblemente hacer los cálculos *a mano* para ver qué podría estar mal.

### Tiempo de descarga

**Enunciado:**
Escriba una función que reciba la velocidad del Internet de un usuario (en Mbps, es decir, Megabits por segundo), y el tamaño de un archivo a descargar (en GB, es decir, Gigabytes), y retorne el tiempo en minutos estimado (redondee al entero más cercano) para realizar la descarga de dicho archivo sobre esa red. Para esto, tenga en cuenta que el tiempo lo puede calcular como *t = tamaño archivo/velocidad descarga*. El tamaño y velocidad deben estar en unidades homogéneas (por ejemplo, MB y MB/s, o GB y GB/s) para que se puedan operar). *Nota*: Recuerde que un MB (Megabyte) equivale a 8 Mb (Megabits), y que un GB equivale a 1000 MB. 

```{code-block} python
def calcular_tiempo_descarga(velocidad: int, tamanio_archivo: int)->int:
    """ Tiempo de descarga
    Parámetros:
      velocidad (int): Velocidad de descarga de la red, en Mbps
      tamanio_archivo (int): Tamaño del archivo a descargar, en GB
    Retorno:
      int: Tiempo estimado en minutos que toma la descarga del archivo
    """
    gb_megas = tamanio_archivo * 1000
    v = velocidad * 8
    tiempo = gb_megas / v
    return round(tiempo)
```

### IVA y propina

**Enunciado:**
Escriba una función que reciba el costo en pesos de una cuenta de restaurante, y luego calcule el impuesto IVA asociado y la propina para el mesero. La tasa del IVA corresponde al 19%, y la propina en el restaurante es del 10% del valor de la factura (sin impuestos). Debe retornar una cadena que muestre el IVA, propina y total de la siguiente manera: "X,Y,Z", donde X es el IVA, Y la propina y Z el total. No olvide aproximar los números al entero más cercano. 

```{code-block} python
def calcular_iva_propina_total_factura (costo_factura: int) -> str:
    """ IVA y propina
    Parámetros:
      costo_factura (int): Costo de la factura del restaurante, sin impuestos ni propina
    Retorno:
      str: Cadena con el iva, propina y total de la factura, separados por coma
    """
    IVA = round (costo_factura*19/100)
    propina = round (costo_factura*10/100) 
    total = round (costo_factura + propina + IVA)
    return str(IVA) + "," + str(propina) + "," + str(total)
```

### Saludo prolongado

**Enunciado:**
Escriba una función que reciba un nombre y un entero, y retorne la cadena 'Hola' seguida del nombre recibido por parámetro, pero con la letra 'o' repetida tantas veces como indique el entero recibido, así como la letra 'a' la mitad de las veces que la 'o' (si la mitad no es exacta, se debe tomar la parte entera). Por ejemplo, si se reciben como parámetros 'Egan' y 5, la cadena a retornar será 'Hooooolaa Egan'.

```{code-block} python
def saludar_repetidas_veces(nombre: str, veces: int)->str:
    """ Saludo prolongado
    Parámetros:
      nombre (str): Nombre a incluir en el saludo
      veces (int): Cantidad de veces a repetir las letras
    Retorno:
      str: Cadena con el saludo con letras repetidas
    """
    o_varias_veces = "o" * veces
    a_varias_veces = "a" * (veces//2)
    return "h" + o_varias_veces + "l" + a_varias_veces +" "+ nombre
```

## Solución de problemas

1. **Enunciado:** El volumen de un cilindro se puede calcular multiplicando el área de su base circular por su altura. Cree una función que reciba el radio de la base y la altura del cilindro, y calcule su volumen. Retorne el resultado redondeado a un solo decimal. 

2. **Enunciado:** Cree una función que pueda calcular el índice de masa corporal (BMI) de una persona a partir de su peso en libras y su altura en pulgadas. La fórmula para calcular el BMI es la siguiente: $BMI = peso/(altura^{2})$, pero para que la fórmula funcione $peso$ debe estar en kilogramos y $altura$ en metros. Recuerde que 1 libra corresponde a 0.454 kg, y que 1 pulgada corresponde a 0.0254 metros. El valor de retorno debe estar redondeado a dos decimales.