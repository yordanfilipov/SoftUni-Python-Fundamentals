products = input().split()

line = input()

while not line == "No Money":
    line = line.split()
    if line[0] == "OutOfStock":
        if line[1] in products:
            products = ["None" if el == line[1] else el for el in products]
    elif line[0] == "Required":
        if 0 <= int(line[2]) < len(products):
            products[int(line[2])] = line[1]
    elif line[0] == "JustInCase":
        products[-1] = line[1]
    line = input()

final_products = [el for el in products if not el == "None"]

print(*final_products, sep=" ")