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

audi = CarManufacturer("Audi", audi_models)
bmw = CarManufacturer("BMW", bmw_models)

car_manufacturers = [audi, bmw]