# Creating a program that checks the strength of a password, it must ne at least 10 characters long, have a lowercase letter, a uppercase letter, and a number.
String = "AaBbCcDe123"
Result = False
Error_Message = ""
Condition_Upper = False
Condition_Lower = False
Condition_Number = False
if (len(String) >= 10):
    for a in String:
        if (Condition_Upper == False and (a.isupper()) == True):
            Condition_Upper = True
        if (Condition_Lower == False and (a.islower()) == True):
            Condition_Lower = True
        if (Condition_Number == False and (a.isnumeric()) == True):
            Condition_Number = True
    if Condition_Upper == False:
        print("Password requires an uppercase letter")
    if Condition_Lower == False:
        print("Password requires an lowercase letter")
    if Condition_Number == False:
        print("Password requires an numerical character")
    if Condition_Upper == True and Condition_Number == True and Condition_Number == True:
        Result = True
else:
    print("Password needs to be at least 10 characters long")
print(Result)
