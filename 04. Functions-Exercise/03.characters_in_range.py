def two_chars(first_char, second_char):
    result = ""
    first_char = ord(first_char)
    second_char = ord(second_char)

    for index in range(first_char + 1, second_char):
        result += chr(index) + " "
    print(result)


char_1 = input()
char_2 = input()

two_chars(char_1, char_2)
