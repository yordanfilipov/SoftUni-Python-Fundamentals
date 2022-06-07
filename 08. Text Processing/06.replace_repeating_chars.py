data = input()
result = data[0]
current_char = data[0]

for char in data:
    if not current_char == char:
        result += char
        current_char = char
print(result)