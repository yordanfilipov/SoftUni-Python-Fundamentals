stops = input()

line = input()

while not line == "Travel":
    line = line.split(":")
    action = line[0]
    if action == "Add Stop":
        index, destination = line[1:]
        index = int(index)
        if 0 <= index < len(stops):
            first_half = stops[:index]
            second_half = stops[index:]
            stops = first_half + destination + second_half
    elif action == "Remove Stop":
        start_index, end_index = line[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if 0 <= start_index < len(stops) and 0 <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]
    elif action == "Switch":
        old_destination, new_destination = line[1:]
        if old_destination in stops:
            stops = stops.replace(old_destination, new_destination)
    print(stops)
    line = input()

print(f"Ready for world tour! Planned stops: {stops}")
