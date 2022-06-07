orders = int(input())
total_price = 0

for i in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsules_count = int(input())
    order_price = (days * capsules_count) * capsule_price
    print(f"The price for the coffee is: ${order_price:.2f}")
    total_price += order_price

print(f"Total: ${total_price:.2f}")