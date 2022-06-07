factor = int(input())
count = int(input())
end_point = factor * count
my_list = []

for index in range(factor, end_point + 1, factor):
    my_list.append(index)
print(my_list)