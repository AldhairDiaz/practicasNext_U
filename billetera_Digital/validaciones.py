import billetera_practica
from requests import Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


"""Codigo con los parametrso para acceder a coinmarket"""
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
apiKeyUNIQUE='0944a756-3d07-457e-8072-74625ad96da3' #La llave unica para acceder a mi billetera
parameters = {
    'start': '1',
  'limit': '5000',
  'convert': 'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apiKeyUNIQUE,
}
session = Session()
session.headers.update(headers)

"""lista_Json accede a la lista
data2 la lista cgeneral de las monedas en un archivo json 
con el ciclo for filtro los nombres de las monedas, simbolo y precio en usd actuales, ademas del precio tota
en USD de todas las monedas, ademas que agrego la cantidad total de monedas que hay en existencia"""
def lista_General():
    try:
        lista_JSON = requests.get(url,headers=headers, params=parameters)
        data2 = json.loads(lista_JSON.text)

        contador = 1
        precio_General=0
        for lista in data2['data']:
            precio_unit = lista['quote']['USD']['price']
            print("Nombre de la moneda (",contador,"): ",lista['name'],
                  "Con simbolo: ",lista['symbol'],"Precio en USD: ", precio_unit)
            contador+=1
            #con este if aplico: si hay un dato en precio que no tenga valor, autoaticamente vale cero.
            if precio_unit==None:
                precio_unit=0
            precio_General+=precio_unit

        print("En total hay: ", contador-1, " monedas. Y el costo total de todas las monedas en USD es de :",precio_General )





    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)




def validar_moneda(moneda):

  parametros = {'symbol': moneda}
  lista_JSON=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest", headers=headers, params=parametros)
  moneda_pedida=json.loads(lista_JSON.text)
  valida=moneda_pedida['status']
  if valida['error_code'] != 400:

    print("La moneda existe en la lista JSON")


    for symbol in moneda_pedida['data']:
      if symbol == moneda:
        print("...Moneda encontrada...", symbol)
        return True

  else:
    print("¡¡¡La moneda NO existe!!!. Verificar Simbolo")
    return False

def validar_codigo(codigo):

  with open('BD.json') as file:
     data=json.load(file)
  for cod in data['user_cliente']:
      if codigo != apiKeyUNIQUE and codigo == cod['codigo']:
          print("El codigo es correcto...")
          return True
      else:
          print("El codigo ingresado es ERRONEO. Verifique")
          return False

def validar_cantidad(cantidad):


    with open('BD_CLIENTE.json') as file:
     data=json.load(file)
    with open('BD_ADMIN.json') as file2:
        data2=json.load(file2)

    import billetera
    if billetera.opcion==1:
        for cliente in data['user_cliente']:
            if cantidad >= 0:
                if cliente['cant_total_cripto'] > 0:
                    if cantidad <= cliente['cant_total_cripto']:
                        print("Continua...")
                        new_cant = cliente['cant_total_cripto'] - cantidad
                        billetera_practica.actualizar_cantidad_cliente(new_cant)
                        for admin in data2['user_admin']:
                            new_cant2 = admin['can_total_cripto'] + cantidad
                            billetera_practica.actualizar_cantidad_admin(new_cant2)
                            print("---Transaccion Realizada---\nAhora tienes: ", new_cant2, " En tu billetera ")

                    elif cantidad > cliente['cant_total_cripto']:
                        print("La cantidad que solicita es mayor en cLIENTE")
                else:
                    print("Ya no hay monedas en la billetera")
            else:
                print("No pueden ser numeros negativos")
    elif billetera.opcion==2:
        for admin in data2['user_admin']:
            if cantidad >= 0:
                if admin['can_total_cripto'] > 0:
                    if cantidad <= admin['can_total_cripto']:
                        print("Continua...")
                        new_cant = admin['can_total_cripto'] - cantidad
                        billetera_practica.actualizar_cantidad_admin(new_cant)
                        print("---Transaccion Realizada---\nAhora tienes : ", new_cant, " En tu billetera ")
                        for cliente in data['user_cliente']:
                            new_cant2 = cliente['cant_total_cripto'] + cantidad
                            billetera_practica.actualizar_cantidad_cliente(new_cant2)
                            print("---Transaccion Realizada---\nAhora tiene el cliente: ", new_cant2, " En su billetera ")

                    elif cantidad > admin['can_total_cripto']:
                        print("La cantidad que solicita es mayor en ADMIN")
                else:
                    print("Ya no hay monedas en la billetera")
            else:
                print("No pueden ser numeros negativos")

def cantidad_cripto():
    with open('BD_ADMIN.json') as file2:
        data2 = json.load(file2)
    for admin in data2['user_admin']:
        print("Continua...")
        new_cant = admin['can_total_cripto']
        print("---Transaccion Realizada---\nTienes : ", new_cant, " En tu billetera ")
        return new_cant

def monto_USD(moneda):

   


    parametros = {'symbol': moneda}
    lista_JSON = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest",
                              headers=headers, params=parametros)
    moneda_pedida = json.loads(lista_JSON.text)


    valida = moneda_pedida['data']
    print("PRECIO USD ACTUAL UNITARIO: ", valida[moneda]['quote']['USD']['price'])
    print("CANTIDAD CRIPTOMONEDAS: ",str(cantidad_cripto()))
    cant=cantidad_cripto()
    print("PRECIO TOTAL: ",valida[moneda]['quote']['USD']['price'] * cant)
    return valida[moneda]['quote']['USD']['price'] * cant

