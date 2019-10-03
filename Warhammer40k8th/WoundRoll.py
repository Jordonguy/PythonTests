# A simple app that takes users input, rolls dice and informs the user the outcome. (Strength VS Toughness)
# If S if double or more than T - 2+
# If S>T - 3+
# If S=T - 4+
# If S<T - 5+
# If S half or less than T - 6+
# Every roll of 1 automatically fails.
# Wound rolls (StrengthVsToughness)

import random

dice_rolled = 0
successful_wounds = 0
failed_wounds = 0
successful_hits = int(
    input("Enter the number of successful hit rolls made : "))
wep_strength = int(input("Enter the attacking weapons Strength : "))
#ap_modifer = int(input("Enter any AP modifiers : "))
target_toughness = int(input("Enter the targets toughness : "))
print(f"{successful_hits} hits have been made against a target with {target_toughness} toughness with a weapon that has a strength of {wep_strength}")
print(f"Now rolling {successful_hits} dice!.....")

while(successful_hits > 0):
    random_num = random.randint(1, 6)
    print(f"{random_num} was rolled")
    if(random_num == 1):
        print("The hit failed to wound the target")
        failed_wounds += 1
    elif((wep_strength * 2 >= target_toughness) and (random_num >= 2)):
        print("The hit successfully wounded the target")
        successful_wounds += 1
    elif((wep_strength > target_toughness) and (random_num >= 3)):
        print("The hit successfully wounded the target")
        successful_wounds += 1
    elif((wep_strength == target_toughness) and (random_num >= 4)):
        print("The hit successfully wounded the target")
        successful_wounds += 1
    elif((wep_strength < target_toughness) and (random_num >= 5)):
        print("The hit successfully wounded the target")
        successful_wounds += 1
    elif((wep_strength <= (target_toughness / 2)) and (random_num >= 6)):
        print("The hit successfully wounded the target")
        successful_wounds += 1
    else:
        print("The hit failed to wound the target")
        failed_wounds += 1
    successful_hits -= 1
print(f"{successful_wounds} shots successfully wounded the target")
print(f"{successful_hits} failed to wound the target")
