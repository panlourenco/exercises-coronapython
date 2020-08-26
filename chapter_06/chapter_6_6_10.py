# 6-10. Favorite Numbers: 

favorite_numbers = {
    'raul': [42, 60, 30],
    'josh': [4, 60, 30],
    'alice': [42, 6, 30],
    'hank': [42, 60, 3],
    'maggie': [52, 60, 30],
    }


for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + "'s favorite numbers are: ") 
    for number in numbers:
        print(" " + str(number)) 