number = int(input())
word = input()
my_list = []
special_list = []

for index in range(number):
    line = input()
    my_list.append(line)
    if word in line:
        special_list.append(line)
print(my_list)
print(special_list)