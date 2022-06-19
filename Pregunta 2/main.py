# Importar librerias
import json
import requests
import Funciones
# API
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r.status_code

headers = {
  "X-CMC_PRO_API_KEY": "65",
  "Accepts":"application/json"
}

params = {
    "start": "1",
    "limit": "6",
    "convert": "USD"
}

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
json = requests.get(url, params = params, headers = headers).json()

coins = json["bpi"]["USD"]["rate_float"]
# Funciones
def main():
  valor = Funciones.flo("Ingrese la cantidad de Bitcoins a convertir: ")
  while True:
    if (valor > 0):
      precio = valor * coins
      print(f"${precio:,.4f}")
      break
    else:
      print("El valor ingresado no es correcto ")

# Mi programa
main()
