# 8-6. City Names:

def city_country(city, country):
    print(city.title() + ", " + country.title())

i = 0
while i < 3:
    city = input("Enter a city: \n")
    country = input("Enter a country: \n")
    city_country(city, country)
    i += 1
