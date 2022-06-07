first_word = input()
second_word = input()

new_word = list(first_word)

for i in range(0, len(first_word)):
    if first_word[i] != second_word[i]:
        new_word[i] = second_word[i]
        print("".join(new_word))
    else:
        continue
