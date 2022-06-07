data = input()
id_dict = {}

while not data == "End":
    company_name, employee_id = data.split(" -> ")

    if company_name not in id_dict:
        id_dict[company_name] = [employee_id]
    else:
        if employee_id not in id_dict[company_name]:
            id_dict[company_name].append(employee_id)
    data = input()

sorted_dict = dict(sorted(id_dict.items(), key=lambda x: x[0]))

for company in sorted_dict:
    print(company)
    for comp_id in sorted_dict[company]:
        print(f'-- {comp_id}')
