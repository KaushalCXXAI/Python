class Microwave:
    def __init__(self,brand,power_rating)-> None:
        self.brand = brand
        self.power_rating = power_rating

smeg = Microwave("nano","24W")
print(smeg.brand)
print(smeg.power_rating)