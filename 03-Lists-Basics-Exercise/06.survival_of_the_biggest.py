input_text = input()
input_list = input_text.split(" ")
removed_number = int(input())
int_list = []

for i in input_list:
    index = int(i)
    int_list += [index]

for j in range(removed_number):
    int_list.remove(min(int_list))

print(int_list)
