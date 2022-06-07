def perfect_number(number):
    sum_ = 0
    for i in range(1, number):
        if number % i == 0:
            sum_ = sum_ + i
    return sum_


num = int(input())

if num == perfect_number(num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")