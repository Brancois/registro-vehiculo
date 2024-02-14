# Cree un programa que permita registrar diferentes tipos de vehículos (e.g.: carros, barcos, aviones)
# definiendo una clase para cada tipo e inicializando al menos dos objetos distintos de cada tipo.
from pprint import pprint

registros = []


class Car:
    def __init__(self, id, title, receipt, insurance, brand):
        self.id = id
        self.title = title
        self.receipt = receipt
        self.insurance = insurance
        self.brand = brand

    def car_info(self):
        information = {"Tipo": "Carro", "Propietario": self.title, "Cedula": self.id,
                       "Marca": self.brand, "Costo": self.receipt, "Seguro": self.insurance}
        registros.append(information)
        return information


class Boat:
    def __init__(self, license, title, receipt, insurance, brand):
        self.license = license
        self.title = title
        self.receipt = receipt
        self.insurance = insurance
        self.brand = brand

    def boat_info(self):
        information = {"Tipo": "Lancha", "Propietario": self.title, "Licencia": self.license,
                       "Marca": self.brand, "Costo": self.receipt, "Seguro": self.insurance}
        registros.append(information)
        return information


class Plane:
    def __init__(self, id, title, tax, insurance, brand):
        self.id = id
        self.title = title
        self.tax = tax
        self.insurance = insurance
        self.brand = brand

    def plane_info(self):
        information = {"Tipo": "Avion", "Propietario": self.title, "Cedula": self.id,
                       "Marca": self.brand, "Impuesto": self.tax, "Seguro": self.insurance, }
        registros.append(information)
        return information


while True:
    vehicle = input("""Que tipo de vehiculo desea registrar?
      1. Carro
      2. Lancha
      3. Avion
      4. Ver todos los registros
      Ingrese el numero: """)

    if vehicle == "1":
        marca = input("Ingrese la marca de su carro: ").capitalize()
        titulo = input(
            "Ingrese el nombre del cual esta el carro: ").capitalize()
        cedula = input("Ingrese su numero de cedula: ")
        recibo = input("Indique el costo del carro: ")
        seguro = input("Esta asegurado el carro?: ").capitalize()
        vehicle = Car(id=cedula, title=titulo, receipt=recibo,
                      insurance=seguro, brand=marca)
        informacion = input("Desea obtener el registro de su carro?: ").lower()
        if informacion == "si":
            pprint(vehicle.car_info(), width=1)
        elif informacion == "no":
            print("Esta bien...")
        else:
            print("No entiendo eso...")
        retry = input("Desea registrar otro vehiculo?: ").lower()
        if retry == "si":
            continue
        elif retry == "no":
            print("Esta bien... Hasta pronto!")
            quit()

    elif vehicle == "2":
        marca = input("Ingrese la marca de su lancha: ").capitalize()
        titulo = input(
            "Ingrese el nombre del cual esta la lancha: ").capitalize()
        licencia = input("Ingrese su numero de su licencia: ")
        recibo = input("Indique el costo de la lancha: ")
        seguro = input("Esta asegurado la lancha?: ").capitalize()
        vehicle = Boat(license=licencia, title=titulo,
                       receipt=recibo, insurance=seguro, brand=marca)
        informacion = input(
            "Desea obtener el registro de su lancha?: ").lower()
        if informacion == "si":
            pprint(vehicle.boat_info(), width=1)
        elif informacion == "no":
            print("Esta bien...")
        else:
            print("No entiendo eso...")
        retry = input("Desea registrar otro vehiculo?: ").lower()
        if retry == "si":
            continue
        elif retry == "no":
            print("Esta bien... Hasta pronto!")
            quit()

    elif vehicle == "3":
        marca = input("Ingrese la marca de su avion: ").capitalize()
        titulo = input(
            "Ingrese el nombre del cual esta el avion: ").capitalize()
        cedula = input("Ingrese su numero de su cedula: ")
        impuesto = input("Indique el costo de los impuestos sobre el avion: ")
        seguro = input("Esta asegurado el avion?: ").capitalize()
        vehicle = Plane(id=cedula, title=titulo, tax=impuesto,
                        insurance=seguro, brand=marca)
        informacion = input("Desea obtener el registro de su avion?: ").lower()
        if informacion == "si":
            pprint(vehicle.plane_info(), width=1)
        elif informacion == "no":
            print("Esta bien...")
        else:
            print("No entiendo eso...")
        retry = input("Desea registrar otro vehiculo?: ").lower()
        if retry == "si":
            continue
        elif retry == "no":
            print("Esta bien... Hasta pronto!")
            quit()

    elif vehicle == "4":
        print("En esta lista se pueden observar todos los registos realizados hasta este momento:")
        pprint(registros, width=1)
        retry = input("Desea registrar otro vehiculo?: ").lower()
        if retry == "si":
            continue
        elif retry == "no":
            print("Esta bien... Hasta pronto!")
            quit()
