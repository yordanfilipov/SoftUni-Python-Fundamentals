input_string = input()
input_list = set(input_string.split(" "))

a_players = 11
b_players = 11
flag = False

for index in input_list:
    if "A" in index:
        a_players -= 1
    elif "B" in index:
        b_players -= 1
    if a_players < 7 or b_players < 7:
        flag = True
        break
print(f'Team A - {a_players}; Team B - {b_players}')
if flag:
    print("Game was terminated")
