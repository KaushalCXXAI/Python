import random
# class Hat:
#     def __init__(self):
#         self.houses = ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))



# hat = Hat()
# hat.sort("Harry")


class Hat:
    houses = ["Griffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
Hat.sort("Heromioni")
Hat.sort("Ron")
Hat.sort("Draco")