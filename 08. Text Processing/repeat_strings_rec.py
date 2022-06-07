line = input().split()


def multiply(word, required_length, counter):
    if len(word) * counter == required_length:
        return word * counter
    counter += 1
    return multiply(word, required_length, counter)


result = ""

for w in line:
    length_to_exceed = len(w * len(w))
    result += multiply(w, length_to_exceed, 1)

print(result)