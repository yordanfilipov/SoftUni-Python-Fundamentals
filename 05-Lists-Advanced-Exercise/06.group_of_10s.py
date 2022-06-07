import math
numbers = [int(el) for el in input().split(", ")]

max_element = max(numbers)
iteration = math.ceil(max_element / 10)
boundary = 0

for iter_count in range(iteration):
    boundary += 10
    current_list = []
    for el in numbers:
        if boundary - 10 < el <= boundary:
            current_list.append(el)
    print(f"Group of {boundary}'s: {current_list}")

