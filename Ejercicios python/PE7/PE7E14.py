#Aprovechando el potencial de los diccionarios,
#escribe un programa que llame a un procedimiento,
#que recibe como parámetro la fecha en números
#y devuelve la fecha  con el nombre del mes.
#Comentario: no es necesario validar si la es
#correcta, damos por hecho que lo será.
#calendario=dict()
calendario={
"01": "enero","02": "febrero","03": "marzo","04":"abril","05":"mayo",
"06":"junio","07":"julio","08":"agosto","09":"septiembre",
"10":"octubre","11":"noviembre","12":"diciembre"
}
def cambiaMes(fecha,diccionario):
    if (fecha[3:5] in diccionario)==True:
        fecha=fecha[0:2]+" de "+diccionario.get(fecha[3:5])+" de "+fecha[6:]
        cambio=print(fecha)
    

fecha=input("Indica una fecha en formato dd/mm/aaa: ")


cambiaMes(fecha,calendario)
