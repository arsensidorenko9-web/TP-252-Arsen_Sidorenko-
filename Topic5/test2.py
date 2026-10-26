
import requests

response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
data = response.json()

currency = input("Введіть валюту (USD, EUR, PLN): ").upper()
amount = float(input("Введіть суму: "))

for elem in data:
    if elem["cc"] == currency:
        result = amount * elem["rate"]
        print("Сума у гривнях:", result, "грн")
        break
