population = [int(el) for el in input().split(', ')]
minimum_wealth = int(input())
needed_wealth = 0

all_wealth = sum(population)

if all_wealth < minimum_wealth * len(population):
    print("No equal distribution possible")
    exit()

for index in range(len(population)):
    if population[index] < minimum_wealth:
        needed_wealth = minimum_wealth - population[index]
        population[population.index(max(population))] -= needed_wealth
        population[index] = minimum_wealth

print(f"{population}")