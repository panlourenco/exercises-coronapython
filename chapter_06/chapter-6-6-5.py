# 6-5. Rivers:

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'seine': 'france',
    'vistula': 'poland',
    'Amazonas': 'brasil',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())