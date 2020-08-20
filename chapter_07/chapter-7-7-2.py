# 7-2. Restaurant Seating:

number_people = input("\nHow many people are in the dinner group?\n")

if int(number_people) > 8:
    print("\nYou have to wait for a table. ")
else:
    print("\nTable ready!")