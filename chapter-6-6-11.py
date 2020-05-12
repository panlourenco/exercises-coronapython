# 6-11. Cities:

cities = {
    'rio':['brazil', '200 millions', 'marvelous city'],
    'krakow':['poland', '40 millions', 'Dragon city'],
    'dublin':['ireland', '5 millions', 'bloomsday'],


}

for city, infos in cities.items():
    print("\n" + city.title() + " - Basic information: ")
    for info in infos:
        print("- " + info.title())