# Save rolls are for shots that have hit and successfully wounded the intended target, the enemy unit has a Save characteristic.
# For each successful wound a Save roll is made, if the rolls result is equal or greater than the units Save characteristic that model doesn't suffer a wound, but if the roll is less than the Save that unit suffers a wound.

import random

save_rolls = int(input("Enter the number of save rolls"))
save_stat = int(input("Enter the save characteristic of the target"))
ap_stat = int(input("Enter the ap stat of the attacking weapon"))
successful_damage = 0

while(save_rolls > 0):
    random_num = random.randint(1, 6)
    if(random_num >= (save_stat - ap_stat)):
        successful_damage += 1
    save_rolls -= 1
