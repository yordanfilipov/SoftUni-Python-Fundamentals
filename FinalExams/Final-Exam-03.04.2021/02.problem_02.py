import re


def print_password(psswd):
    result = ""
    for i in range(len(psswd)):
        if i / 3 == 1 or i / 7 == 1 or i / 11 == 1:
            continue
        else:
            result += psswd[i]
    return print(f"Password: {result}")


n = int(input())

pattern = r"(?P<start>.+)>(?P<pass>[0-9]{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<(?P=start)"

for i in range(n):
    text = input()
    is_match = re.match(pattern, text)
    if is_match:
        is_match = is_match.groupdict()
        is_match = is_match['pass']
        print_password(is_match)
    else:
        print("Try another password!")

