# import requests
# from bs4 import BeautifulSoup

# class BookScraper:
#     def __init__(self, url):
#         self.url = url
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
#         }
#         self.soup = None

#     def fetch_site(self):
#         response = requests.get(self.url, headers=self.headers)
#         if response.status_code == 200:
#             self.soup = BeautifulSoup(response.content, 'html.parser')
#         else:
#             print("Не удалось подключиться к сайту")

#     def get_books(self):
#         список_книг = []
#         элементы_книг = self.soup.find_all('article', class_='product_pod')[:8]
#         for элемент in элементы_книг:
#             название = элемент.h3.a['title']
#             цена = элемент.find('p', class_='price_color').text
#             рейтинг_класс = элемент.find('p', class_='star-rating')['class']
#             if len(рейтинг_класс) > 1:
#                 рейтинг = рейтинг_класс[1]
#             else:
#                 рейтинг = 'Нет рейтинга'
#             книга = {
#                 'Название': название,
#                 'Цена': цена,
#                 'Рейтинг': рейтинг
#             }
#             список_книг.append(книга)
#         return список_книг

#     def show_books(self, список_книг):
#         номер = 1
#         for книга in список_книг:
#             print(str(номер) + ". Название: " + книга['Название'])
#             print("   Цена: " + книга['Цена'])
#             print("   Рейтинг: " + книга['Рейтинг'])
#             print("")
#             номер = номер + 1

# ссылка = "http://books.toscrape.com"
# объект = BookScraper(ссылка)
# объект.fetch_site()
# результат = объект.get_books()
# if результат:
#     объект.show_books(результат)
# else:
#     print("Информация о книгах не найдена.")


import requests
from bs4 import BeautifulSoup

class WikipediaScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        self.soup = None

    def fetch_site(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            print("Не удалось подключиться к сайту")

    def get_main_info(self):
        информация = []
        блок = self.soup.find('div', class_='main-box')
        if not блок:
            print("Информация не найдена")
            return информация

        абзацы = блок.find_all('p')
        счётчик = 0
        for абзац in абзацы:
            текст = абзац.get_text().strip()
            if текст != "":
                информация.append(текст)
                счётчик = счётчик + 1
                if счётчик == 3:
                    break
        return информация

    def show_info(self, информация):
        print("Информация с главной страницы Википедии:")
        print("")
        номер = 1
        for абзац in информация:
            print(str(номер) + ". " + абзац)
            print("")
            номер = номер + 1

ссылка = "https://ru.wikipedia.org/wiki/Заглавная_страница"
объект = WikipediaScraper(ссылка)
объект.fetch_site()
результат = объект.get_main_info()
if результат:
    объект.show_info(результат)
else:
    print("Не удалось получить информацию.")
