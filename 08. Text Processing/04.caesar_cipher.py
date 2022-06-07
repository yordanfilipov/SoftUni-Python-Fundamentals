data = input()
result = ""

for char in data:
    new_symbol = chr(ord(char) + 3)
    result += new_symbol
print(result)