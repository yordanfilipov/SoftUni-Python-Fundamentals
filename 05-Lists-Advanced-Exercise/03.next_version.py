version = input()

first, second, third = version.split(".")
first = int(first)
second = int(second)
third = int(third)

if not third == 9:
    third += 1
else:
    third = 0
    if not second == 9:
        second += 1
    else:
        first += 1
        second = 0

print(f'{first}.{second}.{third}')
