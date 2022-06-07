rooms = int(input())

current_amount = 0
room_chairs = 0
flag = False

for chairs in range(1, rooms + 1):
    line = input()
    free_chairs, taken_chairs = line.split(" ")
    taken_chairs = int(taken_chairs)
    free_chairs = int(len(free_chairs))

    if free_chairs == taken_chairs:
        continue
    if free_chairs > taken_chairs:
        room_chairs = free_chairs - taken_chairs
        current_amount += room_chairs
    else:
        flag = True
        room_chairs = taken_chairs - free_chairs
        print(f'{room_chairs} more chairs needed in room {chairs}')

if not flag:
    print(f"Game On, {current_amount} free chairs left")