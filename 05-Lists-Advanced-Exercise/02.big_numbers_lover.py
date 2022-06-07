my_list = input().split()
my_list.sort(reverse=True)
result = ""

for i in my_list:
    result += i

result = int(result)
print(result)

