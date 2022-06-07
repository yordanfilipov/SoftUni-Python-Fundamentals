# def add_and_subtract(num_1, num_2, num_3):


def sum_numbers(num_1, num_2):
    sum_result = num_1 + num_2
    return sum_result


def subtract(result, num_3):
    final = result - num_3
    return print(final)

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

subtract(sum_numbers(num_1, num_2), num_3)
