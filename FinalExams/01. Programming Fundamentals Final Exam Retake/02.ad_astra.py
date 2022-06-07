import re
text = input()

pattern = r"(?P<separator>(#|\|))(?P<product>[a-zA-Z\s]+)(?P=separator)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(?P=separator)(?P<calories>\d+)(?P=separator)"

result = re.finditer(pattern, text)
all_calories = 0
all_items = []

for el in result:
    obj = el.groupdict()
    all_items.append(f"Item: {obj['product']}, Best before: {obj['date']}, Nutrition: {obj['calories']}")
    all_calories += int(obj['calories'])

days = all_calories//2000
print(f"You have food to last you for: {days} days!")
print('\n'.join(all_items))
