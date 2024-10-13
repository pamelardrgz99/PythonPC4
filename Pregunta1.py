import requests

def obtener_precio_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        precio_usd = data['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_total = n * precio_bitcoin
        print(f"El costo actual de {n} Bitcoins en USD es: ${costo_total:,.4f}")

if __name__ == "__main__":
    main()
