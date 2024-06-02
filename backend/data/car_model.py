
class CarModel:
    def __init__(self, model):
        self.__model = model

    def __str__(self):
        return f'{self.__model}'

    def to_dict(self):
        return {
            "model": self.__model,
        }

#
# {
#     "cars": {
#         "manufacturer": "Toyota",
#         "models": [
#             {
#                 "model": "Corolla"
#             },
#             {
#                 "model": "Camry"
#             },
#             {
#                 "model": "Prius"
#             }
#         ]
#     }
#
# }