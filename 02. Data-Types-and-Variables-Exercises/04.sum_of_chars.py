number = int(input())
result = 0

for i in range(number):
    char = input()
    asci_num = ord(char)
    result += asci_num
print(f'The sum equals: {result}')