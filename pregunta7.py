import requests
import sqlite3
from pymongo import MongoClient

def obtener_datos_sunat():
    url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?year=2023"
    response = requests.get(url)
    return response.json()

def procesar_datos(datos):
    if datos is None:
        return []
    
    processed_data = []
    for fecha, valores in datos.items():
        compra = valores['compra']
        venta = valores['venta']
        processed_data.append({'fecha': fecha, 'compra': compra, 'venta': venta})
    return processed_data

def almacenar_datos_sqlite(datos):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        fecha DATE,
        compra FLOAT,
        venta FLOAT
    )''')

    for dato in datos:
        cursor.execute('''
        INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)
        ''', (dato['fecha'], dato['compra'], dato['venta']))

    conn.commit()
    conn.close()

def almacenar_datos_mongodb(datos):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['sunat']
    collection = db['sunat_info']

    if collection.count_documents({}) > 0:
        collection.drop()

    collection.insert_many(datos)

def mostrar_datos_sqlite():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sunat_info')

    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

    conn.close()

if __name__ == "__main__":
    datos = obtener_datos_sunat()
    datos_procesados = procesar_datos(datos)
    if datos_procesados:
        almacenar_datos_sqlite(datos_procesados)
        almacenar_datos_mongodb(datos_procesados)
        mostrar_datos_sqlite()
