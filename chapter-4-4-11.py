# 4-11. My Pizzas, Your Pizzas:

pizzas = ['margherita', 'pepperoni', 'mozzarella']
friend_pizzas = pizzas[:]
friend_pizzas.append('NYC Style')
for pizza in pizzas:
    print ("My favorite pizzas are " + pizza)
for pizza in friend_pizzas:
    print ("My friend's favorite pizzas are " + pizza)

