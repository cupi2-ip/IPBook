def probar(n, mu, sigma):
    valores = []
    total = 0    
    for i in range(n):
        valores.append(random.normalvariate(mu, sigma))
        total += valores[-1]
    media = total / len(valores)
    suma_cuadrados = 0
    for i in range(len(valores)):
        suma_cuadrados += (valores[i]-media)**2
    varianza = suma_cuadrados / len(valores)
    desviacion = varianza**0.5
    plantilla = "N:{0:^20}\nmu:{1:>10.2f} Media:{2:>10.2f}\nsigma:{3:>7.2f} ST.Dev:{4:>9.2f}"
    print(plantilla.format(n, mu, media, sigma, desviacion))


probar(15, 3.8, 0.6)
probar(5000, 3.8, 0.6)


