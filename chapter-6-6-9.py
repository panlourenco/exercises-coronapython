# 6-9. Favorite Places:

# Make a dictionary called favorite_places.
favorite_places = {
    'josh': ['paris', 'marseille'], 'matt':['krakow', 'warsaw'], 'alice': ['rio', 'buzios']
}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are: ")
    for place in places:
        print("- " + place.title())
