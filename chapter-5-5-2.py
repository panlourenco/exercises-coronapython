# 5-2. More Conditional Tests: 

name = 'Peter'

if name.lower() == 'peter' and name != 'peter':
    print("Equality and Inequality checked")

Peter_age = 20
Rudy_age = 10

if Peter_age > Rudy_age:
    print ("Peter is older than Rudy")

Peter_age = 20
Rudy_age = 30

if Peter_age < Rudy_age:
    print("Peter is younger than Rudy.")

party_list = ['Peter', 'Rudy', 'John', 'Josh']


if 'Marie' not in party_list:
    print( "Marie is not in the list.")

if 'Peter' in party_list:
    print( "Peter is in the list.")
