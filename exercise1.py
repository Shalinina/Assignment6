import random
total_dice = int(input("Enter the number of dice to roll: "))
total_sum = 0
for _ in range(total_dice):
    rolling_num = random.randint(1, 6)
    print("After rolling a dice we get:", rolling_num)
    total_sum += rolling_num
print("The total sum of all dices is:", total_sum)