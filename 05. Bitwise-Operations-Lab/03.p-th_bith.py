number = int(input())
p = int(input())

bit = (number >> p) & 1
print(bit)