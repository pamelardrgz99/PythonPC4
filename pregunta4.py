import csv

with open('temperaturas.txt', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Saltar la cabecera si existe
    temperaturas = [float(row[1]) for row in csv_reader]

temp_max = max(temperaturas)
temp_min = min(temperaturas)
temp_promedio = sum(temperaturas) / len(temperaturas)
with open('resumen_temperaturas.txt', mode='w') as file:
    file.write(f"Temperatura Máxima: {temp_max}\n")
    file.write(f"Temperatura Mínima: {temp_min}\n")
    file.write(f"Temperatura Promedio: {temp_promedio:.2f}\n")
