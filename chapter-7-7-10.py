# 7-10. Dream Vacation:

polling_active = True
responses={}

while polling_active:
    name = input("\nWhat's your name?\n")
    response = input("\nIf you could visit one place in the world, where would you go?\n")

    responses[name] = response

    repeat = input("\n would you like to let another person respond? yes /no\n")
    if repeat == 'no':
        polling_active = False

print("\n *** Poll Results ***")
for name, response in responses.items():
    print(name + " would like to go to " + response + ".\n")