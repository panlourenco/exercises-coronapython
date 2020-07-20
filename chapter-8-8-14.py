# Chapter 8-8-14 User profile

def make_car(manufacturer, model, **options):
    car_dict ={
        'manufacturer':manufacturer.title(),
        'model': model.title(),
    }

    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_car_01=make_car('subaru', 'outback', color = 'blue', tow_package =True)
print(my_car_01)