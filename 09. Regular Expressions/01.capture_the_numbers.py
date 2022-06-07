import re

data = input()
pattern = r"\d+"
numbers = []

while data:
    current_numbers = re.findall(pattern, data)
    if current_numbers:
        numbers.extend(current_numbers)
    data = input()

print(*numbers, sep=" ")