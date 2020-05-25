# 7-8. Deli:

sandwich_orders =['ham and cheese', 'chicken', 'salmon', 'vegan', 'vegetarian', 'tuna']
finished_sandwiches =[]

while sandwich_orders:
    sand = sandwich_orders.pop()
    finished_sandwiches.append(sand)
    print("\nI made your " + sand + " sandwich.")

print(finished_sandwiches)

