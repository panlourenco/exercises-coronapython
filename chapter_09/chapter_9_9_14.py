# 9.14. Dice

from random import randint

class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint (1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
dice_6 = Die()
results= []

for roll_num in range(10):
    result = dice_6.roll_dice()
    results.append(result)

print("10 rolls of a" , dice_6.sides, "-sided die:")
print(results)   

# Make a 10-sided die, and show the results of 10 rolls.
dice_10 = Die(sides=10)
results= []

for roll_num in range(10):
    result = dice_10.roll_dice()
    results.append(result)

print("10 rolls of a" , dice_10.sides, "-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
dice_20 = Die(sides=20)
results= []

for roll_num in range(10):
    result = dice_20.roll_dice()
    results.append(result)

print("10 rolls of a" , dice_20.sides, "-sided die:")
print(results)