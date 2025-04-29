#Agregamos la librería CSV para leer archivos .CSV
import csv
#Inicializamos nuestras variables
suma_credito = 0
cant_credito = 0

suma_debito = 0
cant_debito = 0

monto_mayor = 0
id_mayor = ''

#Abrimos el archivo CSV con la función open('archivo.csv')
with open('data.csv', newline='', encoding='utf-8') as archivo: #abre el archivo y nos da acceso a él mediante la variable "archivo"
    lector = csv.reader(archivo) #genera una lista de strings por cada fila
    next(lector) #Saltar la línea 1 (encabezados)
    for fila in lector:
        id = fila[0]
        tipo = fila[1]
        monto = float(fila[2])
        #print(tipo)
        if tipo == 'Crédito':
            suma_credito += monto
            cant_credito = cant_credito + 1
        elif tipo == 'Débito':
            suma_debito += monto
            cant_debito = cant_debito + 1
        
        if monto_mayor < monto:
            monto_mayor = monto
            id_mayor = id

resultado = suma_credito - suma_debito
print("---------------------------------")
print(f"Balance final: {resultado:.2f}")
print("Transacción de Monto Mayor: ID: ", id_mayor, ", Monto: ", monto_mayor)
print("Cant. Transacciones Crédito: ", cant_credito, ", Cant. Transacciones Débito: ", cant_debito)