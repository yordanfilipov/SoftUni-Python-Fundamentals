number = int(input())
p = int(input())

bit = number & ~(1 << p)
print(bit)