carbrands = ["Toyota car", "Harley Davidson motorcycle", "Land-Rover jeep"]
carbrands.insert(0,'suzuki')
message = "I would like to own a "
print(message + carbrands[0] + ".")
print(message + carbrands[1] + ".")
print(message + carbrands[2] + ".")
carbrands.append('ducatti')
popped_carbrands = carbrands.pop()
print(carbrands)
print(popped_carbrands)