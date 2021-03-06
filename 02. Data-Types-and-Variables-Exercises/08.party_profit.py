import math
companions = int(input())
days = int(input())

coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        companions -= 2
    if i % 15 == 0:
        companions += 5
        coins -= companions * 2
    coins += 50
    coins -= companions * 2
    if i % 3 == 0:
        coins -= companions * 3
    if i % 5 == 0:
        coins += companions * 20

coins_per_companion = coins / companions

print(f'{companions} companions received {math.floor(coins_per_companion)} coins each.')