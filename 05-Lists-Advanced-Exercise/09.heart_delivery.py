neighborhood = list(map(int, input().split("@")))

position = 0
count = 0

command = input()
while not command == "Love!":
    text = command.split(" ")
    jump = int(text[1])

    if jump + position > len(neighborhood) - 1:
        position = 0
        jump = 0
    if neighborhood[position+jump] == 0:
        print(f"Place {position+jump} already had Valentine's day.")
    else:
        neighborhood[position+jump] -= 2

        if neighborhood[position+jump] == 0:
            print(f"Place {position+jump} has Valentine's day.")

    position += jump
    command = input()

for el in neighborhood:
    if el > 0:
        count += 1

print(f"Cupid's last position was {position}.")
if sum(neighborhood) == 0:
    print(f'Mission was successful.')
else:
    print(f"Cupid has failed {count} places.")

