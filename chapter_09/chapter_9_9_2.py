# 9.2 Three Restaurants

class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine)

    def open_restaurant(self):
        print ("The restaurant is open!")

restaurant_1 = Restaurant('DaGrasso', 'Italian')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant('Spaghetteria', 'Italian')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3 = Restaurant('Outback', 'Australian')
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()