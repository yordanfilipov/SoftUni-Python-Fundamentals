students = int(input())
lectures = int(input())
bonus = int(input())
current_bonus = 0
max_bonus = 0
max_lectures = 0

for i in range(students):
    student_attendances = int(input())
    total_bonus = student_attendances / lectures * (5 + bonus)
    if current_bonus < total_bonus:
        current_bonus = total_bonus
        max_bonus = total_bonus
        max_lectures = student_attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_lectures} lectures.")