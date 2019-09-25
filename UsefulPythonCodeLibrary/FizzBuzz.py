# Multiples of 3 = Fizz Multiples of 5 = Buzz Multiples of 3 AND 5 = FizzBuzz
list = []
for num in range(1, 100):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)
    list.append(string)
print(list)
