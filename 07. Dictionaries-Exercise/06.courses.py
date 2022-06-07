command = input()
my_dict = {}

while not command == "end":
    course_name, student_name = command.split(" : ")
    if course_name not in my_dict:
        my_dict[course_name] = []
    my_dict[course_name].append(student_name)
    command = input()

sorted_dict_by_name = {_: sorted(list_) for _, list_ in my_dict.items()}

sorted_dict = dict(sorted(sorted_dict_by_name.items(), key=lambda x: -len(x[1])))

for key, values in sorted_dict.items():
    print(f'{key}: {len(values)}')
    for value in values:
        print(f'-- {value}')