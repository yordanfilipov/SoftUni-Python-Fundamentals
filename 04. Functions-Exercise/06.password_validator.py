def valid_password(input_password):
    length = False
    letters_digits = False
    two_digits = False
    digits_count = 0

    if len(input_password) > 10 or len(input_password) < 6:
        length = True
    for x in input_password:
        if not x.isalpha() and not x.isnumeric():
            letters_digits = True
        if x.isnumeric():
            digits_count += 1
    if digits_count < 2:
        two_digits = True
    if length is False and letters_digits is False and two_digits is False:
        print("Password is valid")
    else:
        if length:
            print("Password must be between 6 and 10 characters")
        if letters_digits:
            print("Password must consist only of letters and digits")
        if two_digits:
            print("Password must have at least 2 digits")


input_pass = input()

valid_password(input_pass)