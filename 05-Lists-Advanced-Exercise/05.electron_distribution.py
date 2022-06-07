electrons = int(input())
result = []
n = 1

while not electrons == 0:
    formula = 2 * (n ** 2)
    if formula > electrons:
        result.append(electrons)
        break
    result.append(formula)
    electrons -= formula
    n += 1
print(result)