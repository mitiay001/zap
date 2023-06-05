import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Button, Text, END, filedialog

def parse_website():
    url = "https://www.example.com"  # Замените на URL нужной веб-страницы

    # Отправляем GET-запрос для загрузки страницы
    response = requests.get(url)

    # Создаем объект BeautifulSoup для парсинга страницы
    soup = BeautifulSoup(response.content, "html.parser")

    # Ищем необходимые элементы на странице и извлекаем информацию
    # В этом примере мы ищем заголовки статей на странице
    articles = soup.find_all("h2", class_="article-title")
    
    # Создаем диалоговое окно для сохранения результатов
    root = Tk()
    root.withdraw()
    save_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not save_path:
        return

    # Записываем результаты в текстовый файл
    with open(save_path, "w", encoding="utf-8") as file:
        for article in articles:
            title = article.text.strip()
            file.write(f"{title}\n")

    # Отображаем сообщение о сохранении
    messagebox.showinfo("Готово", "Результаты сохранены в файл.")

# Создаем графический интерфейс
root = Tk()
root.title("Простой парсер")
root.geometry("300x200")

label = Label(root, text="Нажмите кнопку, чтобы начать парсинг")
label.pack()

button = Button(root, text="Парсить", command=parse_website)
button.pack()

text = Text(root)
text.pack()

root.mainloop()
