my_name = (input("what is your name?"))
my_age =int(input("how old are you?"))
print(f"My name is {my_name} , and i am {my_age} years old")

first_number=int(input("give me the first number")) 
second_number=int(input("give me the second number "))
operation=(input("give me the operation you would like to make"))
if operation == '+':
    print(first_number+second_number)
if operation == "-":
    print(first_number-second_number)
if operation == "*":
    print(first_number*second_number)
if operation == "/":
    print(first_number/second_number) 
if operation == "+,-,/,*":
    print("the operation is not valid")

bus_capacity = 24
people_inbus =int(input("how much people in the bus?"))
empty_seats =int(input("how many people want to enter the bus?" ))
empty_seats = bus_capacity-people_inbus
if empty_seats<24:
    print(f"there are {empty_seats} seats are empy in the bus")
else:
    print("there are no empty seats!")
   
