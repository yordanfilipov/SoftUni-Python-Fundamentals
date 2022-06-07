numbers = [int(el) for el in input().split()]

average_num = sum(numbers) / len(numbers)
result = []

numbers.sort(reverse=True)
for number in numbers:
    if number > average_num:
        result.append(number)
    if len(result) == 5:
        break

if result:
    print(*result, sep=" ")
else:
    print("No")