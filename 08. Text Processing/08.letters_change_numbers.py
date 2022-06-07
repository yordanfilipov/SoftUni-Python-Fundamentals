# def alphabet_position(letter):
#     position = ord(letter.lower()) - 96
#     return position
#
#
# data = input().split()
# final_nums = []
#
# for word in data:
#     current_sum = 0
#     fist_letter = word[0]
#     last_letter = word[-1]
#     # current_num = int(''.join([word[num] for num in range(1, len(word) - 1, 1)]))
#     current_num = int(word[1:-1])
#
#     if fist_letter.isupper():
#         current_sum = current_num / int(alphabet_position(fist_letter))
#     else:
#         current_sum = current_num * int(alphabet_position(fist_letter))
#
#     if last_letter.isupper():
#         current_sum = current_sum - int(alphabet_position(last_letter))
#     else:
#         current_sum = current_sum + int(alphabet_position(last_letter))
#
#     final_nums.append(current_sum)
#
# print(f'{sum(final_nums):.2f}')

positions_alphabet = {chr(ele + 97): ele + 1 for ele in range(26)}

data = input().split()
result = 0

for el in data:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])
    if first_letter.isupper():
        number /= positions_alphabet[first_letter.lower()]
    elif first_letter.islower():
        number *= positions_alphabet[first_letter]

    if last_letter.isupper():
        number -= positions_alphabet[last_letter.lower()]
    elif last_letter.islower():
        number += positions_alphabet[last_letter]

    result += number

print(f"{result:.2f}")