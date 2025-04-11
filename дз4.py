# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

# class Cart:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product, count):
#         if product.quantity >= count:
#             self.products.append((product, count))
#             product.quantity -= count

#     def remove_product(self, name):
#         new_products = []
#         for product, count in self.products:
#             if product.name != name:
#                 new_products.append((product, count))
#         self.products = new_products

#     def total_price(self):
#         total = 0
#         for product, count in self.products:
#             total += product.price * count
#         return total

#     def show_cart(self):
#         for product, count in self.products:
#             print(product.name, "-", count, "шт. по", product.price, "грн")
#         print("Сума:", self.total_price(), "грн")



class Wallet:
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money

    def add_money(self, amount):
        self.money += amount

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
        else:
            print("Недостатньо грошей")

    def show_info(self):
        print("Власник:", self.owner)
        print("Сума грошей:", self.money, "грн")
      
w1 = Wallet("Оля", 100)
w1.add_money(50)
w1.spend_money(30)
w1.show_info()

w2 = Wallet("Іван", 200)
w2.spend_money(250)
w2.show_info()
