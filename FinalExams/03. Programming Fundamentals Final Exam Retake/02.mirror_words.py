import re


def reverse_string(text):
    result = ""
    for i in range(len(text) - 1, -1, -1):
        result += text[i]
    return result


text = input()

pattern = r"(@|#)[a-zA-Z][a-zA-Z][a-zA-Z]+\1\1[a-zA-Z][a-zA-Z][a-zA-Z]+\1"

pair_words = [obj.group() for obj in re.finditer(pattern, text)]
if pair_words:
    print(f"{len(pair_words)} word pairs found!")
else:
    print("No word pairs found!")

mirror_words = []

for i in range(len(pair_words)):
    pair = pair_words[i]
    first_word = pair[1:int(len(pair) / 2 - 1)]
    second_word = pair[int(len(pair) / 2 + 1):-1]
    if first_word == reverse_string(second_word):
        mirror_words.append(f"{first_word} <=> {second_word}")

if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print("No mirror words!")