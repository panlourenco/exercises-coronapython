# 7-4. Pizza Toppings: 

pizza_toppings = []

active = True
while active:
    message = input("\nPlease enter pizza toppings: \n")
    if message == 'quit':
        active = False
        
    else:
        pizza_toppings.append(message)
        
print(pizza_toppings)