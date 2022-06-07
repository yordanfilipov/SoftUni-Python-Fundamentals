people = int(input())
wagons = [int(el) for el in input().split()]
free_seats = 0
full_capacity = 4

for wagon in range(len(wagons)):
    taken_seats = wagons[wagon]
    free_seats = full_capacity - taken_seats
    if people == 0:
        break
    if free_seats == 0:
        continue
    else:
        if people >= free_seats:
            wagons[wagon] = full_capacity
            people -= free_seats
        else:
            wagons[wagon] += people
            people -= wagons[wagon]

is_empty_spots = sum(wagons) / len(wagons)

if is_empty_spots < full_capacity:
    print("The lift has empty spots!")
elif people > 0 and is_empty_spots == full_capacity:
    print(f"There isn't enough space! {people} people in a queue!")
print(*wagons, sep=" ")