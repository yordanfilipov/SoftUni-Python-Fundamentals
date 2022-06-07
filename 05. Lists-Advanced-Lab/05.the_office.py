employees_happiness = list(map(lambda x: int(x), input().split()))
improvement_factor = int(input())

improved_happiness = [x*improvement_factor for x in employees_happiness]
avg = sum(improved_happiness) / len(improved_happiness)

filtered_employees = list(filter(lambda x: x >= avg, improved_happiness))

all_emp = len(employees_happiness)
happy_emp = len(filtered_employees)

if happy_emp < all_emp / 2:
    print(f'Score: {happy_emp}/{all_emp}. Employees are not happy!')
else:
    print(f'Score: {happy_emp}/{all_emp}. Employees are happy!')