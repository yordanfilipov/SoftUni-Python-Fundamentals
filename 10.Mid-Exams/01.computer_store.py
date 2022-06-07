price_without_taxes = 0

while True:
    command = input()
    if command == "special" or command == "regular":
        break
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        continue
    price_without_taxes += current_price


taxes = price_without_taxes * 0.2
total_price = price_without_taxes + taxes
special_discount = total_price - (total_price * 0.1)
if price_without_taxes > 0:
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {price_without_taxes:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------")

    if command == "regular":
        print(f"Total price: {total_price:.2f}$")
    elif command == "special":
        print(f"Total price: {special_discount:.2f}$")
else:
    print("Invalid order!")