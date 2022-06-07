collecting_items = input().split(", ")

command = input()


def collect(items, item):
    if item not in items:
        collecting_items.append(item)
    return items


def drop(items, item):
    if item in items:
        collecting_items.remove(item)
    return items


def combine(items, item):
    old_item, new_item = item.split(":")
    if old_item in items:
        old_index = collecting_items.index(old_item)
        collecting_items.insert(old_index + 1, new_item)
    return items


def renew(items, item):
    if item in items:
        collecting_items.append(item)
        collecting_items.remove(item)
    return items


while not command == "Craft!":
    action, item = command.split(" - ")
    if action == "Collect":
        collect(collecting_items, item)
    elif action == "Drop":
        drop(collecting_items, item)
    elif action == "Combine Items":
        combine(collecting_items, item)
    elif action == "Renew":
        renew(collecting_items, item)

    command = input()

print(", ".join(collecting_items))