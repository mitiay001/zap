import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос к странице с товарами
response = requests.get("https://hottours.in.ua/")

# Создаем объект BeautifulSoup для парсинга HTML-разметки
soup = BeautifulSoup(response.content, "html.parser")

# Находим все элементы с классом "product-item"
product_items = soup.find_all(class_="product-item")

# Создаем файл для записи данных
with open("products.txt", "w", encoding="utf-8") as file:
    # Обходим каждый товар
    for product in product_items:
        # Извлекаем информацию о товаре
        title = product.find(class_="product-title").text.strip()
        price = product.find(class_="product-price").text.strip()
        description = product.find(class_="product-description").text.strip()

        # Записываем информацию в файл
        file.write(f"Название: {title}\n")
        file.write(f"Цена: {price}\n")
        file.write(f"Описание: {description}\n")
        file.write("-" * 50 + "\n")