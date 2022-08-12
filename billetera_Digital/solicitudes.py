
"""Funcion para la 1a opcion del usuario"""

def recibir_Cantidad():
    import validaciones
    moneda = input("¿Que moneda desea recibir?. Escriba el simbolo [BTN,ETH... etc...]:")
    validaciones.validar_moneda(moneda)

    codigo = input('Teclee el codigo del usuario Cliente: ')
    validaciones.validar_codigo(codigo)

    if validaciones.validar_codigo(codigo)==False:
        codigo = input('Teclee el codigo del usuario Cliente: ')
        validaciones.validar_codigo(codigo)

    cantidad = int(input('Cantidad que desea recibir:'))
    validaciones.validar_cantidad(cantidad)

def transferir_Cantidad():
    import validaciones

    moneda = input("¿Que moneda desea transferir?. Escriba el simbolo [BTN,ETH]:")
    validaciones.validar_moneda(moneda)

    if validaciones.validar_moneda(moneda) == False:
        transferir_Cantidad()

    codigo = input('Teclee el codigo del usuario Cliente: ')
    validaciones.validar_codigo(codigo)

    if validaciones.validar_codigo(codigo)==False:
        codigo = input('Teclee el codigo del usuario Cliente: ')
        validaciones.validar_codigo(codigo)

    cantidad = int(input('Cantidad que desea enviar:'))
    validaciones.validar_cantidad(cantidad)

def balance_Moneda():
    import validaciones

    moneda = input("¿Que moneda desea mostrar?. Escriba el simbolo [BTN,ETH]:")
    validaciones.validar_moneda(moneda)
    validaciones.cantidad_cripto()
    validaciones.monto_USD(moneda)

def balance_General():
    import validaciones

    validaciones.lista_General()





