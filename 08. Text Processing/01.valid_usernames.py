data = input().split(", ")
flag = True

for word in data:
    flag = True
    for char in word:
        if not char.isalpha() and not char.isdigit() and not char == "_" and not char == "-":
            flag = False
    if flag and 3 <= len(word) <= 16:
        print(word)