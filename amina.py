my_name = (input("what ia your name?"))
my_age =int(input("how old are you?"))
print(f"my name is {my_name} , and i am {my_age} years old")

first_number=int(input("give me the first number"))
second_number=int(input("give me the second number"))
operation=(input("give me the operation you would like to make"))
if operation == "+":
    print( first_number+second_number)
elif operation == "-":
    print( first_number-second_number)
elif operation == "*":
    print(first_number*second_number)
elif operation == "/":
    print(first_number/second_number)
else:
    print("the operation is not valid")

bus_capacity =24
people_inbus =int(input("how many people in the bus?"))
people_outside=int(input("how many people want to enter the bus?"))
empty_seats = bus_capacity - people_inbus
if empty_seats>people_outside:
    print(f"there is {empty_seats} empty seats")
elif empty_seats<people_outside or empty_seats==people_outside:
    print("there is no empty seats")
    
    
