number = float(input())

if number == 0:
    print("zero")
if number > 0:
    if 0 < number < 1:
        print("small positive")
    elif 1 < number < 1000000:
        print("positive")
    else:
        print("large positive")
if number < 0:
    if -1 < number < 0:
        print("small negative")
    elif -1000000 < number < 1:
        print("negative")
    else:
        print("large negative")