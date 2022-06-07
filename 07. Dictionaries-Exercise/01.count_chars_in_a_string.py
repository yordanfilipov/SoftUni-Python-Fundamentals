words = input().split()
chars = {}

for word in words:
    for char in word:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

for key, value in chars.items():
    print(f'{key} -> {value}')