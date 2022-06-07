# data = [1, 2, 3, 4]
#
# try:
#     data.remove(10)
# except ValueError:
#     pass
# print(data)

n = int(input())
data = []

for i in range(n):
    line = input()
    data.append(line)
print(data)