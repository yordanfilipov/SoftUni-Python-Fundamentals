def sum_even_odd_digits(number):
    odd_sum = 0
    even_sum = 0
    for index in range(len(str(number))):
        digit = number % 10
        number = number // 10
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')


num = int(input())

sum_even_odd_digits(num)