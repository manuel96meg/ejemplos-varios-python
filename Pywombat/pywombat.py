"""
def fibonacci(maxnumber):
    fib_list = []
    if int(maxnumber) > 0:
        fib_list = [0]
        if int(maxnumber) == 1:
            return fib_list
        else:
            add = 1
            for i in range(1,maxnumber):
                fib_list.append(add)
                prev = fib_list[i-1] if fib_list[i-1] > 0 else 0
                add = prev + fib_list[i]
    return fib_list

print(fibonacci(12))

#------------------------------------------

#Calcular el area de un circulo

from math import pi
radio = float(input('Introduce el radio: '))
area =  pi* radio**2
print(f'El area del circulo es: {area}') 
"""

#Desarrolla un programa el cual nos permita conocer todos los números pares 
# que se encuentren dentro del rango de de x y y.

def rango_pares(x:int,y:int):
    #genera una lista de numeros pares dentro del rango de 2 numeros ingresados
    lista_pares = []
    if int(x) < int(y) and int(x) > 0:
        lista_pares = [i for i in range(int(x),int(y)) if i%2 == 0] 
        return lista_pares
    else:
        print('ERROR: El primer valor debe ser mayor a 0 y menor al segundo')

print(rango_pares(5,80))