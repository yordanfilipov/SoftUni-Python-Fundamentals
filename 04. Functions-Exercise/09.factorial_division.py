def factorial_division(number):
    factorial = 1
    for i in range(number, 1, -1):
        factorial *= i
    return factorial


num_1 = int(input())
num_2 = int(input())

first_factorial = factorial_division(num_1)
second_factorial = factorial_division(num_2)

result = first_factorial / second_factorial
print(f'{result:.2f}')