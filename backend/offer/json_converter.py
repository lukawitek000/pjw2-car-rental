

def car_to_dict(car):
    return {
        "car_id": car.car_id,
        "car_model": car.car_model,
        "car_make": car.car_make,
        "car_year": car.car_year,
        "fuel_type": car.fuel_type,
        "transmission": car.transmission,
        "owner_id": car.owner_id,
        "mileage": car.mileage,
        "additional_features": car.additional_features
    }


def offer_to_dict(offer):
    return {
        "user_id": offer.user_id,
        "offer_id": offer.offer_id,
        "car": car_to_dict(offer.car),
        "price_per_day": offer.price_per_day,
        "extra_features": offer.extra_features,
        "start_date_time": offer.start_date_time,
        "end_date_time": offer.end_date_time,
        "pickup_location": offer.pickup_location,
        "return_location": offer.return_location
    }

