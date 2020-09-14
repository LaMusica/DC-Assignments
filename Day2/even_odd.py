#even_orodd = input("Enter number:  ")

#if even_orodd type == int() or float():
#    return 



#Does nesting the input() method inside of the int() method:

# 1. Convert the user (String) input into a type of int? (Y)

# 2. Check to make sure the user enters a number (Doesen't appear so) [This would require a conditional {if} statement]



number = int(input("Provide a number: ")) # any other data type asside from int - would likely cause and error in the program

if number % 2 == 0:
    print(f"{number} is Even")

else:
    print("ODD")