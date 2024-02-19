# es para iprimir las listas y diccionarios de una forma mas bonita :)
from pprint import pprint

registers = []


class Vehicle():  # clase padre
    def __init__(self, identification, brand, color, year, cost, type):
        self.identification = identification
        self.brand = brand
        self.color = color
        self.year = year
        self.cost = cost
        self.type = type


class Car(Vehicle):  # clase hija con la clase padre dentro del parametro
    # se usa el super().__init__ para acceder a los atributos de la clase padre
    def __init__(self, identification, brand, color, year, cost, type, plate, car_type):
        super().__init__(identification, brand, color,
                         year, cost, type)
        self.plate = plate
        self.car_type = car_type

    def show(self):
        show = {"Name": self.identification, "Type": self.type, "Brand": self.brand,
                "Year": self.year, "Color": self.color, "Cost": self.cost + "$", "Plate": self.plate, "Car type": self.car_type}
        registers.append(show)
        return show


class Plane(Vehicle):
    def __init__(self, identification, brand, color, year, cost, type, capacity, range):
        super().__init__(identification, brand, color, year, cost, type)
        self.capacity = capacity
        self.range = range

    def show(self):
        show = {"Name": self.identification, "Type": self.type, "Brand": self.brand,
                "Year": self.year, "Color": self.color, "Cost": self.cost + "$", "Capacity": self.capacity, "Plane range": self.range + 'M'}
        registers.append(show)
        return show


class Boat(Vehicle):
    def __init__(self, identification, brand, color, year, cost, type, name, size):
        super().__init__(identification, brand, color, year, cost, type)
        self.name = name
        self.size = size

    def show(self):
        show = {"Name": self.identification, "Type": self.type, "Brand": self.brand,
                "Year": self.year, "Color": self.color, "Cost": self.cost + "$", "Boat name": self.name, "Size": self.size + 'ft'}
        registers.append(show)
        return show


while True:
    vehicle = input("""What type of vehicle do you want to register?
      1. Car
      2. Boat
      3. Plane
      4. See all registers
      Insert number: """)

    if vehicle == "1":
        identification = input("Full name: ")
        type = "Car"
        brand = input("What brand is your car: ")
        year = input("What year is your car: ")
        color = input("What color is your car: ")
        cost = input("What is the cost of your car: ")
        plate = input("Insert the license plate of your car: ")
        car_type = input("Insert the type of car you're registering: ")
        vehicle = Car(identification=identification, brand=brand, color=color,
                      year=year, cost=cost, type=type, plate=plate, car_type=car_type)
        reveal = input("Would you like to see your register? ").lower()
        if reveal == 'yes':
            pprint(vehicle.show(), width=1)
        else:
            print("Ok...")
        question = input("Would you like to register anything else? ").lower()
        if question == 'yes':
            continue
        else:
            break

    elif vehicle == "2":
        identification = input("Full name: ")
        type = "Boat"
        brand = input("What brand is your boat: ")
        year = input("What year is your boat: ")
        color = input("What color is your boat: ")
        cost = input("What is the cost of your boat: ")
        name = input("Insert the name plate of your boat: ")
        size = input("Insert the size of the boat you're registering (ft): ")
        vehicle = Boat(identification=identification, brand=brand, color=color,
                       year=year, cost=cost, type=type, name=name, size=size)
        reveal = input("Would you like to see your register? ").lower()
        if reveal == 'yes':
            pprint(vehicle.show(), width=1)
        else:
            print("Ok...")
        question = input("Would you like to register anything else? ").lower()
        if question == 'yes':
            continue
        else:
            break

    elif vehicle == "3":
        identification = input("Full name: ")
        type = "Plane"
        brand = input("What brand is your plane: ")
        year = input("What year is your plane: ")
        color = input("What color is your plane: ")
        cost = input("What is the cost of your plane: ")
        capacity = input("Insert the capacity your plane: ")
        range = input(
            "Insert the range of the plane you're registering (miles): ")
        vehicle = Plane(identification=identification, brand=brand, color=color,
                        year=year, cost=cost, type=type, capacity=capacity, range=range)
        reveal = input("Would you like to see your register? ").lower()
        if reveal == 'yes':
            pprint(vehicle.show(), width=1)
        else:
            print("Ok...")
        question = input("Would you like to register anything else? ").lower()
        if question == 'yes':
            continue
        else:
            break

    elif vehicle == "4":
        print("Here are all of the registers saved so far:")
        pprint(registers, width=1)

    else:
        print("I cant' understand that... ")
        continue
