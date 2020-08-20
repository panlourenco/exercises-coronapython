#You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#Add a new line that prints a message saying that you can invite only two people for dinner.

guests=['John', 'Paulina', 'Rafal', 'Jorge', 'Peter', 'Rafal']
print("Sorry, we can only invite two people for dinner.")

#Use pop() to remove guests from your list

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

# Print a message to each of the two people still on your list, letting them know they’re still invited.
print("Hi, " + guests[0] + "!" + " Would you still like to get together for dinner?")
print("Hi, " + guests[1] + "!" + " Would you still like to get together for dinner?")

del(guests[0])
# there's only one element left
del(guests[0]) 
print(guests)
