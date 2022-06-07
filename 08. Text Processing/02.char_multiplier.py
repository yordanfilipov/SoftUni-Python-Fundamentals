data = input().split()
max_word_length = 0
result = 0

if len(data[0]) >= len(data[1]):
    max_word_length = len(data[0])
else:
    max_word_length = len(data[1])

for word_index in range(max_word_length):
    if word_index < len(data[0]):
        first_word_ch = ord(data[0][word_index])
    else:
        first_word_ch = 0
    if word_index < len(data[1]):
        second_word_ch = ord(data[1][word_index])
    else:
        second_word_ch = 0

    if not first_word_ch == 0 and not second_word_ch == 0:
        current_sum = first_word_ch * second_word_ch
    else:
        current_sum = first_word_ch + second_word_ch

    result += current_sum
print(result)