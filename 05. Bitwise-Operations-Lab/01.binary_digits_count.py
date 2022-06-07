number = int(input())
binary_digit = int(input())
result = ""
counter = 0

while not number == 0:
    reminder = number % 2
    result += str(reminder)
    number = number // 2

binary_number = result[::-1]

for digit in binary_number:
    if int(digit) == binary_digit:
        counter += 1

if binary_digit == 1:
    print(f'We have {counter} ones.')
else:
    print(f'We have {counter} zeroes.')