number = int(input())
number += ord('a')

for i in range(97, number):
    for j in range(97, number):
        for k in range(97, number):
            print(f'{chr(i)}{chr(j)}{chr(k)}')