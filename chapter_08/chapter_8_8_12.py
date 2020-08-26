# 8-12. Sandwiches

def make_sandwich(*items):
    for item in items:
        print ("You ordered " + item + " in your sandwich.")
        print(items)


make_sandwich('cheddar', ' lettuce', 'honey dijon')
make_sandwich('tomato', 'ham', 'mayonnaise', 'ketchup')
make_sandwich('hummus', 'tuna', 'lettuce')