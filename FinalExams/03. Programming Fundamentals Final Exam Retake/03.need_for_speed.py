MAX_FUEL = 75


def drive_car(cars, car, distance, fuel):
    if cars[car]['fuel'] >= fuel:
        cars[car]['mileage'] += distance
        cars[car]['fuel'] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")
    if cars[car]['mileage'] >= 100000:
        del cars[car]
        print(f"Time to sell the {car}!")
    return cars


def refuel_car(cars, car, fuel):
    initial_fuel = cars[car]['fuel']
    additional_fuel = fuel
    if initial_fuel + additional_fuel > MAX_FUEL:
        cars[car]['fuel'] = MAX_FUEL
        print(f"{car} refueled with {MAX_FUEL - initial_fuel} liters")
    else:
        cars[car]['fuel'] = initial_fuel + additional_fuel
        print(f"{car} refueled with {additional_fuel} liters")
    return cars


def revert_car(cars, car, kilometers):
    cars[car]['mileage'] -= kilometers
    if cars[car]['mileage'] >= 10000:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    else:
        cars[car]['mileage'] = 10000
    return cars


n = int(input())
cars = {}

for _ in range(n):
    car_info = input().split("|")
    car, mileage, fuel = car_info[:]
    mileage = int(mileage)
    fuel = int(fuel)
    cars[car] = {'mileage': mileage, 'fuel': fuel}

command = input()
while not command == "Stop":
    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        car, distance, fuel = command[1:]
        distance = int(distance)
        fuel = int(fuel)
        cars = drive_car(cars, car, distance, fuel)
    elif action == "Refuel":
        car, fuel = command[1:]
        fuel = int(fuel)
        cars = refuel_car(cars, car, fuel)
    elif action == "Revert":
        car, kilometers = command[1:]
        kilometers = int(kilometers)
        cars = revert_car(cars, car, kilometers)
    command = input()

sorted_cars = sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for car, data in sorted_cars:
    print(f"{car} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")