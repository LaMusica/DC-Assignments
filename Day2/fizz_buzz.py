number = int(input("Enter Number: "))

# if # divisible by 3 then FIZZ 

if number % 3 == 0:
    print("Fizz")

# if # divisible by 5 then FIZZ 
elif number % 5 == 0:
    print("Buzz")
# if # divisible by 3 & 5 then FIZZ Buzz

# elif number % 3 and 5 == 0:
#    print("Fizz Buzz")

elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")


else:
    print("Not Fizz Buzz")