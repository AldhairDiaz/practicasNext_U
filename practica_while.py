valorCripto=0
cantMonedas=0
totalAcumulado=0
totalCripto=0
x=1

while x <= 5:
    nombreCripto=input("Dame el nombre de la criptomoneda: ")
    valorCripto=float(input("Dame el valor $ de la criptomoneda "+nombreCripto+":"))
    cantMonedas=int(input("Cantidad de monedas "+nombreCripto+":"))
    totalCripto=(valorCripto*cantMonedas)
    total=print("El total de "+nombreCripto+" es de:"+str(totalCripto))
    totalAcumulado=float(totalAcumulado+totalCripto)
    x=x+1


print("El total acumulado de todas las Criptomonedas es de:"+str(totalAcumulado))





