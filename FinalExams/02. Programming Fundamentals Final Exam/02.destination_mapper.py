import re

text = input()

pattern = r"(^|(?<=(?P<sep>(\=|\/))))[A-Z][a-zA-Z][a-zA-Z]+($|(?=(?P=sep)))"

destinations = [el.group() for el in re.finditer(pattern, text)]
print(f"Destinations: {', '.join(destinations)}")

points = 0
for destination in range(len(destinations)):
    points += len(destinations[destination])

print(f"Travel Points: {points}")