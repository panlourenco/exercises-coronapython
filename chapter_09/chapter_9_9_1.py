# 9.1 Restaurant

class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine)

    def open_restaurant(self):
        print ("The restaurant is open!")

restaurant = Restaurant('DaGrasso', 'Italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()


