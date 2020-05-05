# Changing Guest list
# Add a print statement at the end of your program stating the name of the guest who can’t make it
guests= ['Paulina', 'Jorge', 'Peter']

print("I'm sorry Rodrigo. " + guests[1] + " can't make the dinner")

# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting
del(guests[1])
guests.insert(1, 'Ania')

# Print a second set of invitation messages, one for each person who is still in your list.
print("Hi, " + guests[0] + "!" + " Would you like to get together for dinner?")
print("Hi, " + guests[1] + "!" + " Would you like to get together for dinner?")
print("Hi, " + guests[2] + "!" + " Would you like to get together for dinner?")

