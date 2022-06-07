def exchange(nums_list, index):
    if 0 <= index < len(nums_list):
        first_part = nums_list[:index+1]
        second_part = nums_list[index+1:]
        exchanged_list = second_part + first_part
        return exchanged_list
    else:
        print("Invalid index")
        return nums_list


def get_max_odd(nums_list):
    filter_only_odds = []
    for el in nums_list:
        if el % 2 == 1:
            filter_only_odds.append(el)
    if not filter_only_odds:
        return print("No matches")

    max_odd = max(filter_only_odds)

    for index in range(len(nums_list)-1, -1, -1):
        if nums_list[index] == max_odd:
            print(index)
            break


def get_max_even(nums_list):
    filter_only_evens = []
    for el in nums_list:
        if el % 2 == 0:
            filter_only_evens.append(el)
    if not filter_only_evens:
        return print("No matches")

    max_even = max(filter_only_evens)

    for index in range(len(nums_list) - 1, -1, -1):
        if nums_list[index] == max_even:
            print(index)
            break


def get_min_odd(nums_list):
    filter_only_odds = []
    for el in nums_list:
        if el % 2 == 1:
            filter_only_odds.append(el)
    if not filter_only_odds:
        return print("No matches")

    min_odd = max(filter_only_odds)

    for index in range(len(nums_list) - 1, -1, -1):
        if nums_list[index] == min_odd:
            print(index)
            break


def get_min_even(nums_list):
    filter_only_evens = []
    for el in nums_list:
        if el % 2 == 0:
            filter_only_evens.append(el)
    if not filter_only_evens:
        return print("No matches")

    min_even = min(filter_only_evens)

    for index in range(len(nums_list) - 1, -1, -1):
        if nums_list[index] == min_even:
            print(index)
            break


def first_odd(nums_list, count):
    filter_only_odds = []
    if count > len(nums_list):
        return print("Invalid count")
    step = 0
    for el in nums_list:
        if step == count:
            break
        if el % 2 == 1:
            filter_only_odds.append(el)
            step += 1
    return print(filter_only_odds)


def first_even(nums_list, count):
    filter_only_evens = []
    if count > len(nums_list):
        return print("Invalid count")
    step = 0
    for el in nums_list:
        if step == count:
            break
        if el % 2 == 0:
            filter_only_evens.append(el)
            step += 1
    return print(filter_only_evens)


def last_odd(nums_list, count):
    filter_only_odds = []
    if count > len(nums_list):
        return print("Invalid count")
    step = 0
    for el in nums_list[::-1]:
        if step == count:
            break
        if el % 2 == 1:
            filter_only_odds.append(el)
            step += 1
    return print(filter_only_odds)


def last_even(nums_list, count):
    filter_only_evens = []
    if count > len(nums_list):
        return print("Invalid count")
    step = 0
    for el in nums_list[::-1]:
        if step == count:
            break
        if el % 2 == 0:
            filter_only_evens.append(el)
            step += 1
    return print(filter_only_evens)


numbers_as_string = input().split()

numbers = list(map(int, numbers_as_string))

command = input()

while not command == "end":
    if command.split()[0] == "exchange":
        index = int(command.split()[1])
        numbers = exchange(numbers, index)
    elif command.split()[0] == "max":
        if command.split()[1] == "odd":
            get_max_odd(numbers)
        elif command.split()[1] == "even":
            get_max_even(numbers)
    elif command.split()[0] == "min":
        if command.split()[1] == "odd":
            get_min_odd(numbers)
        elif command.split()[1] == "even":
            get_min_even(numbers)
    elif command.split()[0] == "first":
        count = int(command.split()[1])
        if command.split()[2] == "odd":
            first_odd(numbers, count)
        elif command.split()[2] == "even":
            first_even(numbers, count)
    elif command.split()[0] == "last":
        count = int(command.split()[1])
        if command.split()[2] == "odd":
            last_odd(numbers, count)
        elif command.split()[2] == "even":
            last_even(numbers, count)

    command = input()
print(numbers)
