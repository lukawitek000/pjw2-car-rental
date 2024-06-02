

class CarManufacturer:
    def __init__(self, manufacturer, models):
        self.manufacturer = manufacturer
        self.models = models

    def to_dict(self):
        return {
            "manufacturer": self.manufacturer,
            "models": [model.to_dict() for model in self.models]
        }
