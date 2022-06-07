def register(reg_name, reg_license):
    if reg_name in my_dict:
        result = f"ERROR: already registered with plate number {reg_license}"
    else:
        my_dict[reg_name] = reg_license
        result = f"{reg_name} registered {reg_license} successfully"
    return result


def unregister(reg_name):
    if reg_name not in my_dict:
        result = f"ERROR: user {reg_name} not found"
    else:
        my_dict.pop(reg_name)
        result = f"{reg_name} unregistered successfully"
    return result


n = int(input())
my_dict = {}
reg = 0

for i in range(n):
    input_text = input()
    command = input_text.split()[0]
    if command == "register":
        _, name, license_plate = input_text.split()
        reg = register(name, license_plate)
    elif command == "unregister":
        _, name = input_text.split()
        reg = unregister(name)
    print(reg)

for key, value in my_dict.items():
    print(f'{key} => {value}')

