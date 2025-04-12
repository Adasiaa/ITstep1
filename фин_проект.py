import requests
from bs4 import BeautifulSoup

class EkUa:
    def __init__(self, url):
        self.url = url
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        }
        self.soup = None
        self.products = []

    def auditSite(self):
        response = requests.get(self.url, headers=self.header)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            print("Не вдалося підключитися до сайту")

    def getInfo(self):
        if not self.soup:
            return []

        products = []
        blocks = self.soup.find_all('div', class_='model-short-div')[:10]

        for block in blocks:
            name_tag = block.find('a', class_='model-short-title')
            price1 = block.find('span', id='price_2760972')
            price2 = block.find('span', id='price_2603099')
            price3 = block.find('span', id='price_2793973')
            price4 = block.find('span', id='price_2827612')
            price5 = block.find('span', id='price_2771892')
            price6 = block.find('span', id='price_2529964')
            price7 = block.find('span', id='price_2532653')
            price8 = block.find('span', id='price_2606917')
            price9 = block.find('span', id='price_2761288')
            price10 = block.find('span', id='price_2776291')

            name = name_tag.text.strip() if name_tag else "Відсутня назва"
            if price1:
                price_text = price1.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0

            elif price2:
                price_text = price2.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0

            elif price3:
                price_text = price3.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0

            elif price4:
                price_text = price4.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0

            elif price5:
                price_text = price5.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0

            elif price6:
                price_text = price6.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0

            elif price7:
                price_text = price7.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0

            elif price8:
                price_text = price8.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0

            elif price9:
                price_text = price9.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0
                
            else:
                price_text = price10.get_text(strip=True)
                price_num = ''.join(filter(str.isdigit, price_text))
                price = int(price_num) if price_num else 0

            products.append({
                'Назва': name,
                'Ціна': price
            })

        self.products = products
        return products

    def showInfo(self):
        print('\nСписок товарів:\n')
        print('НАЗВА                                           ЦІНА')
        for product in self.products:
            print(f"{product['Назва']:<45}{product['Ціна']} грн")

    def buyProducts(self):
        cart = []
        total = 0

        while True:
            self.showInfo()
            try:
                number = int(input("\nВведіть номер товару: "))
                if 1 <= number <= len(self.products):
                    q = int(input("Введіть кількість: "))
                    if q > 0:
                        p = self.products[number - 1]
                        s = p['Ціна'] * q
                        total += s
                        cart.append((p, q, s))

                        more = input("Бажаєте ще щось? (так/ні): ").lower()
                        if more != 'так':
                            break
                    else:
                        print("Неправильний номер товару")
                        
            except ValueError:
                print("Будь ласка, введіть число!")

        if cart:
            print("\nВаш кошик:")
            for p, q, s in cart:
                print(f"- {p['Назва']} x{q} = {s} грн")
            print(f"Загальна сума: {total} грн")

url = "https://ek.ua/ua/list/122/"
obj = EkUa(url)
obj.auditSite()
site = obj.getInfo()
if site:
    obj.buyProducts()
else:
    print("Жодної інформації не отримано")
 
