"""La siguiente lista contiene las opciones deseadas"""
import sys
ee=sys.path.append("../..")



def lista_opciones(num):
 import solicitudes



 if num==1:
  solicitudes.recibir_Cantidad()
 elif num==2:
  solicitudes.transferir_Cantidad()
 elif num==3:
  solicitudes.balance_Moneda()
 elif num==4:
     solicitudes.balance_General()
 else:print("El numero No coincide con las opciones")





"""Interfaz que aparece al usuario"""
opcion = int(input("De la siguiente lista:\n"
                   "1) Recibir cantidad\n"
                   "2) Transferir monto \n"
                   "3) Mostrar balance de moneda\n"
                   "4) Mostrar balance General\n"
                   "5) Mostrar historico de transacciones\n"
                   "6) Salir del programa\n"
                   " Teclee el numero que corresponda a la opcion deseada: \n"))
"""Llamamos a la funcion lista"""
lista_opciones(opcion)






















