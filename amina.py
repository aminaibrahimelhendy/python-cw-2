my_name = input("what is your name?")
my_age = int(input("how old are you?"))
print(f"My name is {my_name}, and I am {my_age} years old")

first_number = int(input("give me the first number")) 
second_number = int(input("give me the second number"))
operation = input("give me the operation you would like to make")
if operation == '+':
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    print(first_number / second_number) 
else:
    print("Invalid operation")

bus_capacity = 24
people_in_bus = int(input("how much people in the bus?"))
empty_seats = bus_capacity - people_in_bus
if empty_seats > 0:
    print(f"There are {empty_seats} seats empty in the bus")
else:
    print("There are no empty seats!")

   
