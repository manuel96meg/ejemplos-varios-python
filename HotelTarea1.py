"""Deberá crear un código que haga referencia a una habitación de un hotel,
en la que se pueda cambiar el status de “sucio” a “limpio” la hora a la que se limpió, 
el nombre de la persona encargada, y que se puedan poner anotaciones en caso de que sean necesarias.

Al final de eso que se arme un informe en texto que muestre los datos ingresados. 
De esta forma la gerencia podría pedir un informe diario de todos los detalles ocurridos.
En el caso de no haber anotaciones, deberían aparecen en el informe “no se hicieron observaciones” además de todos los datos.
"""

#Podrian ser variables de una clase para generar todas las habitaciones, o una lista de diccionarios
habitacion_limpieza_datos = {
    'Estado' : 'INCOMPLETO' ,
    'Persona_Encargada' : 'INCOMPLETO',
    'Hora_Limpiado' : 'INCOMPLETO',
    'Anotaciones' : 'INCOMPLETO' }

def CambiosHabitacion(habitacionAct):
    print()
    CambiarEstado(habitacionAct)
    print()
    CambiarPersona(habitacionAct)
    print()
    CambiarHora(habitacionAct)
    print()
    CambiarAnotaciones(habitacionAct)
    print()

def Informar(hab):
    print()
    print('INFORME:')
    print()
    print(f"-El ESTADO de la habitacion se encuentra {hab['Estado']}.")
    print(f"-La PERSONA encargada de la limpieza de esta habitacion es {hab['Persona_Encargada']}.")
    print(f"-Esta habitacion fue atendida a las {hab['Hora_Limpiado']}.")
    if hab['Anotaciones'] == 'INCOMPLETO':
        print("-No se hicieron observaciones")
    else:
        print(f"-Se realizaron las siguientes observaciones: \n {hab['Anotaciones']}")
    print()

def CambiarEstado(hab):
    print(f"Actualmente el ESTADO de la habitacion es -{hab['Estado']}-.")
    opcion = str(input('Indique "si" o "no" si desea hacerle cambios al ESTADO de la habitacion: '))
    if opcion == 'si':
        respuesta = str(input('Indique si la habitacion se encuentra "limpia" o "sucia": '))
        hab['Estado'] = respuesta

def CambiarPersona(hab):
    print(f"Actualmente la PERSONA encargada es -{hab['Persona_Encargada']}-.")
    opcion = str(input('Indique "si" o "no" si desea hacer cambios: '))
    if opcion == 'si':
        respuesta = str(input('Indique el NOMBRE de la persona encargada de la limpieza de esta habitacion: '))
        hab['Persona_Encargada'] = respuesta

def CambiarHora(hab):
    print(f"La habitacion se limpio a las -{hab['Hora_Limpiado']}- horas.")
    opcion = str(input('Indique "si" en caso de realizar cambios a la HORA en fue limpiada la habitacion: '))
    if opcion == 'si':
        respuesta = str(input('Indique la HORA en fue limpiada la habitacion\nen el siguiente formato [hh:mm]: '))
        hab['Hora_Limpiado'] = respuesta

def CambiarAnotaciones(hab):
    print(f"Las ANOTACIONES de la actual habitacion son -\n{hab['Anotaciones']}-.")
    opcion = str(input('Indique "si" en caso de querer realizar anotaciones: '))
    if opcion == 'si':
        respuesta = str(input('Indique las ANOTACIONES correspondientes [presione Enter para finalizar]: '))
        hab['Anotaciones'] = respuesta

def main_habitacion():
    HabitacionActual = habitacion_limpieza_datos
    CambiosHabitacion(HabitacionActual)
    opcion = str(input('Desea ver el INFORME del dia de hoy? [si/no]: '))
    if opcion == 'si':
        Informar(HabitacionActual)
        print('FIN DEL INFORME')
    print('- - -')

main_habitacion()