from data.car_manufacturer import CarManufacturer
from data.car_model import CarModel

audi_models = [
    CarModel("A3"),
    CarModel("A4"),
    CarModel("A5"),
    CarModel("A6"),
    CarModel("A7"),
    CarModel("A8"),
    CarModel("Q3"),
    CarModel("Q5"),
    CarModel("Q7"),
    CarModel("Q8"),
    CarModel("R8"),
    CarModel("TT"),
    CarModel("e-tron"),
]
audi = CarManufacturer("Audi", audi_models)

bmw_models = [
    CarModel("1 Series"),
    CarModel("2 Series"),
    CarModel("3 Series"),
    CarModel("4 Series"),
    CarModel("5 Series"),
    CarModel("6 Series"),
    CarModel("7 Series"),
    CarModel("8 Series"),
    CarModel("X1"),
    CarModel("X2"),
    CarModel("X3"),
    CarModel("X4"),
    CarModel("X5"),
    CarModel("X6"),
    CarModel("X7"),
    CarModel("Z4"),
    CarModel("i3"),
    CarModel("i8"),
]
bmw = CarManufacturer("BMW", bmw_models)

tesla_models = [
    CarModel("Model S"),
    CarModel("Model 3"),
    CarModel("Model X"),
    CarModel("Model Y"),
]
tesla = CarManufacturer("Tesla", tesla_models)

toyota_models = [
    CarModel("Corolla"),
    CarModel("Camry"),
    CarModel("Prius"),
]
toyota = CarManufacturer("Toyota", toyota_models)

mercedes_models = [
    CarModel("A-Class"),
    CarModel("B-Class"),
    CarModel("C-Class"),
    CarModel("E-Class"),
    CarModel("S-Class"),
]
mercedes = CarManufacturer("Mercedes", mercedes_models)

seat_models = [
    CarModel("Ibiza"),
    CarModel("Leon"),
    CarModel("Arona"),
    CarModel("Ateca"),
]
seat = CarManufacturer("Seat", seat_models)

renault_models = [
    CarModel("Clio"),
    CarModel("Megane"),
    CarModel("Captur"),
    CarModel("Kadjar"),
]
renault = CarManufacturer("Renault", renault_models)

ford_models = [
    CarModel("Fiesta"),
    CarModel("Focus"),
    CarModel("Mustang"),
    CarModel("Explorer"),
    CarModel("F-150"),
]
ford = CarManufacturer("Ford", ford_models)

peugeot_models = [
    CarModel("208"),
    CarModel("308"),
    CarModel("508"),
    CarModel("2008"),
    CarModel("3008"),
]
peugeot = CarManufacturer("Peugeot", peugeot_models)

citroen_models = [
    CarModel("C1"),
    CarModel("C3"),
    CarModel("C4"),
    CarModel("C5"),
    CarModel("Berlingo"),
]
citroen = CarManufacturer("Citroën", citroen_models)

fiat_models = [
    CarModel("500"),
    CarModel("Panda"),
    CarModel("Tipo"),
    CarModel("Punto"),
    CarModel("Ducato"),
]
fiat = CarManufacturer("Fiat", fiat_models)

car_manufacturers = [audi, bmw, tesla, toyota, mercedes, seat, renault, ford, peugeot, citroen, fiat]
