count_even = 0
count_odd = 0
# Range to 101 because it doesn't include 101 it will only include upto 100
for number in range(1, 101):
    if number % 2 == 0:
        count_even += 1
        print(number)
    else:
        count_odd += 1
        print(number)
print(f"We have {count_even} even numbers")
print(f"We have {count_odd} odd numbers")
