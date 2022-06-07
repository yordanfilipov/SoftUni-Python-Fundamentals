command = input()
my_dict = {}

while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in my_dict:
        my_dict[name] = []
    my_dict[name] += price, quantity

    command = input()

for key, value in my_dict.items():
    quantity_list = []
    current_price = value[-2]
    for ind, obj in enumerate(value):
        if not ind % 2 == 0:
            quantity_list.append(obj)
    current_sum = sum(quantity_list) * current_price
    print(f'{key} -> {current_sum:.2f}')

# ......................solution with classes.................................
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#
# data = input()
# products = []
#
# while not data == "buy":
#     name, price, quantity = data.split()
#     price = float(price)
#     quantity = int(quantity)
#     if name in map(lambda x: x.name, products):
#         product = list(filter(lambda x: x.name == name, products))[0]
#         product.price = price
#         product.quantity += quantity
#     else:
#         product = Product(name, price, quantity)
#         products.append(product)
#     data = input()
#
# for product in products:
#     print(f"{product.name} -> {product.price * product.quantity}")