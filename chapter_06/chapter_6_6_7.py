# 6-7. People:

# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person = {
    'first_name': 'eric',
    'last_name': 'smith',
    'age': 43,
    'city': 'krakow',
    }
people.append(person)

person = {
    'first_name': 'josh',
    'last_name': 'smith',
    'age': 5,
    'city': 'krakow',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 8,
    'city': 'krakow',
    }
people.append(person)

# Display all of the information in the dictionary.
for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    
    print(name + ", of " + city + ", is " + age + " years old.")
