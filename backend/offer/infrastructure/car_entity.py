from peewee import *

from authentication.infrastructure.entities import User
from database import BaseModel
from offer.domain.car import Car


class CarEntity(BaseModel):
    car_id = AutoField()
    car_model = CharField()
    car_make = CharField()
    car_year = IntegerField()
    fuel_type = CharField()
    transmission = CharField()
    owner = ForeignKeyField(User, backref='cars')
    mileage = IntegerField()
    additional_features = TextField()

    def to_domain_model(self):
        return Car(
            car_id=self.car_id,
            car_model=self.car_model,
            car_make=self.car_make,
            car_year=self.car_year,
            fuel_type=self.fuel_type,
            transmission=self.transmission,
            owner_id=self.owner_id,
            mileage=self.mileage,
            additional_features=self.additional_features
        )

    @staticmethod
    def from_domain_model(car, owner):
        return CarEntity(
            car_model=car.car_model,
            car_make=car.car_make,
            car_year=car.car_year,
            fuel_type=car.fuel_type,
            transmission=car.transmission,
            owner=owner,
            mileage=car.mileage,
            additional_features=car.additional_features
        )
