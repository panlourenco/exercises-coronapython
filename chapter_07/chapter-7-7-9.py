# 7-9. No Pastrami:

sandwich_orders =['pastrami','ham and cheese', 'chicken', 'pastrami','salmon', 'vegan', 'vegetarian', 'tuna', 'pastrami']

finished_sandwiches =[]

print("Deli has run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)


