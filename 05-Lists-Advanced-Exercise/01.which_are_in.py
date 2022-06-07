first_list = input().split(", ")
second_list = input().split(", ")

result = []

for substring in first_list:
    for string in second_list:
        if substring in string and substring not in result:
            result.append(substring)

print(result)