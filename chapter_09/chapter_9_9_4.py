# 9.4 Number Served

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



restaurant = Restaurant('DaGrasso', 'Italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(23500)
restaurant.increment_number_served(50)
print(restaurant.number_served)

