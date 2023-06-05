import requests
from bs4 import BeautifulSoup

# Ссылка на страницу с курсами валют
url = "https://privatbank.ua/"

# Функция для получения информации о курсах валют
def get_exchange_rates():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Находим элементы с информацией о курсах
    # и извлекаем необходимые данные
    eur_rate = float(soup.find("span", class_="eur-rate").text)
    usd_rate = float(soup.find("span", class_="usd-rate").text)

    return eur_rate, usd_rate

# Функция для конвертации валюты
def convert_currency(amount, from_currency, to_currency):
    eur_rate, usd_rate = get_exchange_rates()

    # Конвертируем валюту в соответствии с выбранными данными
    if from_currency == "EUR":
        if to_currency == "USD":
            converted_amount = amount * (usd_rate / eur_rate)
        else:
            converted_amount = amount
    elif from_currency == "USD":
        if to_currency == "EUR":
            converted_amount = amount * (eur_rate / usd_rate)
        else:
            converted_amount = amount
    else:
        converted_amount = None

    return converted_amount

# Пример использования
amount = 100  # Сумма для конвертации
from_currency = "EUR"  # Исходная валюта
to_currency = "USD"  # Целевая валюта

converted_amount = convert_currency(amount, from_currency, to_currency)

if converted_amount is not None:
    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
else:
    print("Ошибка: Неподдерживаемая валюта")
