import re

text = input()
pattern = r"(::|\*\*)[A-Z][a-z][a-z]+\1"

cool_threshold = 1
for el in text:
    if el.isdigit():
        cool_threshold *= int(el)

print(f"Cool threshold: {cool_threshold}")

all_emojis = [el.group() for el in re.finditer(pattern, text)]

cool_emojis = []

for i in range(len(all_emojis)):
    current_emoji = all_emojis[i]
    coolness = 0
    for symbol in range(2, len(current_emoji) - 2, 1):
        coolness += ord(current_emoji[symbol])
    if coolness > cool_threshold:
        cool_emojis.append(current_emoji)

print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
for cool in cool_emojis:
    print(cool)