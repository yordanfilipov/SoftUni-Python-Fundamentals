RANGE_CLOTHES = range(0, 51)
RANGE_SHOES = range(0, 35)

collection_of_items = input().split("|")
budget = float(input())
sold_items = []
total_profit = 0
current_budget = budget

for item in collection_of_items:
    type_of_item, price = item.split("->")
    price = float(price)

    if type_of_item == "Clothes" and price > 50:
        continue
    elif type_of_item == "Shoes" and price > 35:
        continue
    elif type_of_item == "Accessories" and price > 20.50:
        continue

    if current_budget >= price:
        current_budget -= price
        current_profit = 0.4 * price
        total_profit += current_profit
        sold_price = current_profit + price
        sold_price = round(sold_price, 2)
        sold_price = str(sold_price)
        sold_items.append(sold_price)

print(' '.join(sold_items))
print(f'Profit: {total_profit:.2f}')

budget += sum(sold_items)

if budget + total_profit > 150:
    print("Hello, France!")
else:
    print("Time to go.")
