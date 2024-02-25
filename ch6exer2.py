import random
def roll_dice(num_side):
    return random.randint(1, num_side)
greatest_num = int(input("Enter the greatest number to find: "))
num_side = int(input("Enter the number of sides of a rolling dice: "))
output = 0
while output != greatest_num:
    output = roll_dice(num_side)
    print("After rolling the dice, we get:", output)

print("The greatest number", greatest_num, "is rolled!")