"""
Crear un programa que sea un controlador de gastos mensuales, que podamos 
ingresar gastos e ingresos mes a mes y nos vaya actualizando la información.
"""

meses = {}
dineroTotal = float(0)

def verTotalYMeses(meses,total):
    print('¿Quiere ver el total actual y el dinero de cada mes?')
    respuesta = str(input('["SI" o "NO"]: '))
    if respuesta == "SI":
        for i in meses:
            meses[i].mostrar()
        print(f'El SALDO TOTAL de la cuenta es: {total}')

class DineroEsteMes:
    def __init__ (self,entra,sale,mes = str(" "),cuenta = float(0)):
        self.cuenta = float(cuenta + (entra - sale))
        self.mes = mes
        self.entra = entra
        self.sale = sale
    
    def ingresar (self,nuevoEntra=0):
        self.cuenta += self.entra + nuevoEntra
        self.entra += nuevoEntra
    
    def descontar (self,nuevoSale=0):
        self.cuenta -= self.sale + nuevoSale
        self.sale += nuevoSale
    
    def mostrar(self):
        if self.cuenta > 0:
            print(f'El mes de -{self.mes}- tuvo un movimiento total de +{self.cuenta}, con {self.entra} ingresos y {self.sale} egresos')
        else:
            print(f'El mes de -{self.mes}- tuvo un movimiento total de {self.cuenta}, con {self.entra} ingresos y {self.sale} egresos')

stringMes = str(input('Escriba el MES actual [para finalizar escriba 0]:'))

while stringMes != "0":
    if not (meses.__contains__(stringMes)):
        ingresos = float(input(f'Anote ingresos del mes {stringMes}: '))
        gastos = float(input(f'Anote gastos del mes {stringMes}: '))
        dineroTotal =  dineroTotal + (ingresos - gastos)
        mesActual = DineroEsteMes(ingresos,gastos,stringMes,0)
        meses[stringMes] = mesActual
        verTotalYMeses(meses,dineroTotal)
        stringMes = str(input('Escriba el MES actual [para finalizar escriba 0]:'))
    else:
        ingresos = float(input(f'Anote ingresos del mes {stringMes}: '))
        gastos = float(input(f'Anote gastos del mes {stringMes}: '))
        dineroTotal =  dineroTotal + (ingresos - gastos)
        mesActual = meses[stringMes]
        mesActual.ingresar(ingresos)
        mesActual.descontar(gastos)
        verTotalYMeses(meses,dineroTotal)
        stringMes = str(input('Escriba el MES actual [para finalizar escriba 0]:'))

verTotalYMeses(meses,dineroTotal)
