

def conversionCripto (canBTN,canXRP ):

    BTCUSD = 7442.50
    XRPUSD = 0.660982
    saldo_total_USD=(BTCUSD*canBTN)+(XRPUSD*canXRP)
    TOTAL=print("La suma de las Criptomonedas es de: "+str(saldo_total_USD))
    return TOTAL


BTN=int(input("Dame la cantidad de BTN:"))
XRP=int(input("Dame la cantidad de XRP:"))
conversionCripto(BTN,XRP)
