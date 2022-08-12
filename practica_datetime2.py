from datetime import datetime

hoy=datetime.now()
nombreCripto=input("Dame el nombre de la Criptomoneda")
cantidadAcumulada=float(input("Cantidad que posees de criptomoneda"))
cotizacion=float(input("Cotizacion en el mercado por dolares"))
montoTotal=cantidadAcumulada*cotizacion
incremento=(montoTotal*0.05)
incrementoProximaSemana=incremento*8
print("El valor $ que posees hoy es de: "+str(montoTotal)+ "Dolares"+"\n"+"El día de mañana(incremento de 5%) será de: "+str( float(montoTotal+incremento))+
      "El mismo día de la Proxima semana será de: "+str(float(montoTotal+incrementoProximaSemana)))
print("Fecha de consulta: "+hoy.strftime("%A, %d de %B de %Y a las %I:%M:%S%p"))


