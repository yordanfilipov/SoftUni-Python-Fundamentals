cards = input().split()
n = int(input())

hpp = int(len(cards) // 2)
result = []

for i in range(n):
    result = []
    for i in range(len(cards)):
        if i == len(cards) / 2:
            break
        one = cards[i]
        ff = i + hpp
        two = cards[ff]

        result.append(one)
        result.append(two)
    cards = result

print(result)