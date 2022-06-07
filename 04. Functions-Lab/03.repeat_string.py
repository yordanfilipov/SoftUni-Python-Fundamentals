def repeat_string(string_, count):
    new_string = ""
    for i in range(count):
        new_string += string_
    return new_string


input_string = input()
input_count = int(input())

print(repeat_string(input_string, input_count))