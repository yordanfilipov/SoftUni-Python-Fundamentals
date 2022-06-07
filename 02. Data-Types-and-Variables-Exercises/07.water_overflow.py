number_of_pours = int(input())
taken_capacity = 0

for pour in range(number_of_pours):
    current_pour = int(input())
    taken_capacity += current_pour
    if taken_capacity > 255:
        taken_capacity -= current_pour
        print("Insufficient capacity!")
print(taken_capacity)