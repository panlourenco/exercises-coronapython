# 9.6 Ice Cream Stand
class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine)

    def open_restaurant(self):
        print ("The restaurant is open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ("chocolate", "vanilla", "strawberry")

    def display_flavors(self):
        print(self.flavors)

iceCreamStand = IceCreamStand("Da Grasso", "Italian")
iceCreamStand.display_flavors()