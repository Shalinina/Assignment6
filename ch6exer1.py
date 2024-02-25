import random
def num():
    return random.randint(1, 6)
output = 0
while output != 6:
    output = num()
    print("After Roll a dice we get: ", output)
