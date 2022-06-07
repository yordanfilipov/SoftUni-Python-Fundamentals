import re
n = int(input())

pattern = r"@\#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@\#+"
all_products = [input() for _ in range(n)]

for i in range(len(all_products)):
    el = re.match(pattern, all_products[i])
    if not el:
        print("Invalid barcode")
        continue
    el = el.group()
    group = ""
    for ch in el:
        if ch.isdigit():
            group += ch
    if group:
        print(f"Product group: {group}")
    else:
        print("Product group: 00")