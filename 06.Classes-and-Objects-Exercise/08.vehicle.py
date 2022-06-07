class Vehicle:
    owner = None

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price

    def buy(self, money, owner):
        self.money = money
        if Vehicle.owner is not None:
            return "Car already sold"
        elif self.money >= self.price and Vehicle.owner is None:
            self.owner = owner
            return f"Successfully bought a {self.type}." \
                   f" Change: {(self.money - price):.2f}"
        else:
            return "Sorry, not enough money"

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        return f"{self.model} {self.type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
