def loading_bar(num):
    percent_sign = num // 10
    dots = (100 - num) // 10
    loading_string = "["
    for x in range(percent_sign):
        loading_string += "%"
    for y in range(dots):
        loading_string += "."
    loading_string += "]"
    if num == 100:
        print(f'{num}% Complete!')
        print(loading_string)
    else:
        print(f'{num}% {loading_string}')
        print("Still loading...")



num = int(input())

loading_bar(num)
