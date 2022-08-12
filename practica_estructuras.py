

i = 0
cantidad_cripto =[i]
valor_cripto = [i]
lista_nombres = [i]


while i < 5:
    lista_nombres[i] = input("Ingrese el nombre de la Criptonomeda: ")
    lista_nombres.append(lista_nombres[i])

    cantidad_cripto[i] = input("Ingrese la cantidad de la Criptonomeda " + lista_nombres[i])
    cantidad_cripto.append(cantidad_cripto[i])

    valor_cripto[i] = input("Ingrese el valor $$ de la Criptonomeda " + lista_nombres[i])
    valor_cripto.append(valor_cripto[i])
    i += 1

i=0
while i < 5:
    print(str("Nombre: " +lista_nombres[i]
              +"Cantidad:"+cantidad_cripto[i]+
              "Valor unitario"+valor_cripto[i]))
    i += 1

