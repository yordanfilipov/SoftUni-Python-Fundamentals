n = int(input())

pieces = {}


def add_piece(pieces, piece, composer, key):
    if piece in pieces:
        print(f"{piece} is already in the collection!")
        return pieces
    else:
        pieces[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
        return pieces


def remove_piece(pieces, piece):
    if piece not in pieces:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        print(f"Successfully removed {piece}!")
        pieces.pop(piece)
    return pieces


def change_key(pieces, piece, new_key):
    if piece not in pieces:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    else:
        pieces[piece][1] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    return pieces


for _ in range(n):
    command = input().split("|")
    piece, composer, key = command[0], command[1], command[2]
    if piece not in pieces:
        pieces[piece] = 0
    pieces[piece] = [composer, key]

line = input()
while not line == "Stop":
    line = line.split("|")
    action = line[0]
    if action == "Add":
        piece, composer, key = line[1], line[2], line[3]
        pieces = add_piece(pieces, piece, composer, key)
    elif action == "Remove":
        piece = line[1]
        pieces = remove_piece(pieces, piece)
    elif action == "ChangeKey":
        piece, new_key = line[1], line[2]
        pieces = change_key(pieces, piece, new_key)
    line = input()

sorted_pieces = sorted(pieces.items(), key=lambda x: (x[0], x[1][0]))

for piece, value in sorted_pieces:
    composer, key = value[0], value[1]
    print(f"{piece} -> Composer: {composer}, Key: {key}")