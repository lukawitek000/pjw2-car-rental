class Car:
    def __init__(self, car_model, car_make, car_year, fuel_type, transmission, owner_id, mileage,
                 additional_features, car_id=None):
        self.car_id = car_id
        self.car_model = car_model
        self.car_make = car_make
        self.car_year = car_year
        self.fuel_type = fuel_type
        self.transmission = transmission
        self.owner_id = owner_id
        self.mileage = mileage
        self.additional_features = additional_features

    def __str__(self):
        return f"Car ID: {self.car_id}, Car Model: {self.car_model}, Car Make: {self.car_make}," \
               f" Car Year: {self.car_year}, Fuel Type: {self.fuel_type}, Transmission: {self.transmission}, " \
               f"Owner ID: {self.owner_id}, Mileage: {self.mileage}, Additional Features: {self.additional_features}"
