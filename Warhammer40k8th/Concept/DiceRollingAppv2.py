# An small application that allows the user to select a number of 6 sided dice and roll them
import random
quit = False
dice_rolled = 0
results = []

while(quit == False):
    # Taking User Input
    dice_rolled = dice_rolled
    dice_size = int(input("Enter the size of the dice you : "))
    dice_num = int(input("Enter the number of dice you want : "))
    print("You have selected " + str(dice_num) + " dice.")

    while(dice_num > 0):
        random_num = random.randint(1, dice_size)
    # make this random.randint(1,6) be assigned to a variable called random_num etc.
    # print(random_num)
        results.append(random_num)
        dice_num -= 1
        dice_rolled += 1
    print("Overall Dice Rolled : " + str(dice_rolled))
    print("|| Results table ||")

    while (dice_size > 0):
        count = results.count(dice_size)
        print(str(dice_size) + " was rolled : " + str(count))
        dice_size -= 1

    # Brief experiment with informing the user if the roll was above or below average.
    #average = 0
    # while(dice_rolled > 0):
    #    average += 3
    #    dice_rolled -= 1

    # if (sum(results) > average):
    #    print("total : " + str(sum(results)) + " above average roll")
    # else:
    #    print("total : " + str(sum(results)) + " below average roll")
    #print(str((sum(results)) - average) + " from the average")

    user_choice = str(
        input("|| Enter [Quit] to close the application : Press enter to perform another roll || "))
    if(user_choice == "Quit"):
        quit = True
    else:
        quit = False
# Make a better way of showing results
# Allow user to keep rolling new dice(reset old results etc)
# Allow the user to select the size of the dice
