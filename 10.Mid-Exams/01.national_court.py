first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

daily_people = int(input())
total_handled_per_hour = first_employee + second_employee + third_employee
time = 0

while daily_people > 0:
    time += 1
    if time % 4 == 0:
        continue
    daily_people -= total_handled_per_hour

print(f"Time needed: {time}h.")