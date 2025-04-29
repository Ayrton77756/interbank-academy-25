# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## Objetivo:
Este proyecto realiza el procesamiento de un archivo CSV (`data.csv`) que contiene registros de transacciones de tipo "Crédito" y "Débito".
Se calcula el balance final, se identifica la transacción con el monto mayor y se cuentan las transacciones por tipo.

## Estructura de Datos
El archivo `data.csv` tiene el siguiente formato:

   ```sh
   id,tipo,monto
   1,Crédito,100.00
   2,Débito,50.00
   3,Crédito,200.00
   4,Débito,75.00
   5,Crédito,150.00
   ```
Cada fila representa:
* `id` → Identificador único de la transacción
* `tipo` → Puede ser "Crédito" o "Débito"
* `monto` →  Valor numérico de la transacción

## ¿Qué hace el script?
1. **Leer el archivo CSV usando la librería estándar `csv`**
2. **Salta la primera línea (Los encabezados)**
3. **Procesar cada fila:**
* Convertir el `monto` a `float`.
* Sumar los montos de "Créditos" y "Débitos".
* Contar la cantidad de "Créditos" y "Débitos".
* Identificar la transacción con el monto más alto.
4. **Calcular el balance final**
5. **Mostrar los resultados por consola**
* Mostrar el Balance final: Suma total de montos de crédito - Suma total de montos de débito.
* Transacción con el monto mayor y su ID
* Total de Transacciones de Crédito y Débito.