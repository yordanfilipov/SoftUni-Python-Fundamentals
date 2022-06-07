# words = input().split()
# occurrences = {}
#
# words = [w.lower() for w in words]
#
# for word in words:
#     occurrences[word] = words.count(word)
#
# for key, value in occurrences.items():
#     if not value % 2 == 0:
#         print(f'{key} ', end='')

def reverse_list(list_, start, stop):
    reverse_portion = list(reversed(list_[start:start + stop]))
    numbers = list_[:start] + reverse_portion + list_[start + stop:]
    return numbers


def sort_list(list_, start, stop):
    reverse_portion = list(sorted(list_[start:start + stop]))
    numbers = list_[:start] + reverse_portion + list_[start + stop:]
    return numbers


def remove_list(list_, count):
    numbers = list_[count:]
    return numbers


nums = input().split(' ')

data = input()

while not data == "end":
    command = data.split(' ')[0]

    if command == "reverse":
        _, _, start_index, _, stop_index = data.split(' ')
        start_index = int(start_index)
        stop_index = int(stop_index)
        nums = reverse_list(nums, start_index, stop_index)
    elif command == "sort":
        _, _, start_index, _, stop_index = data.split(' ')
        start_index = int(start_index)
        stop_index = int(stop_index)
        nums = sort_list(nums, start_index, stop_index)
    elif command == "remove":
        count = int(data.split(' ')[-1])
        nums = remove_list(nums, count, )

    data = input()

print(', '.join([str(el) for el in nums]))