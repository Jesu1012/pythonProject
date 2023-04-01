"""TODO : 17"""
# Time with 'for'
"""import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    #print(f'{seconds:02}')
    time.sleep(1)

print("TIME'S UP!")
"""

"""TODO : 16"""
# nested loop(outer, inner)
"""rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
   for y in range(columns):
       print(symbol, end="")
   print()
"""

"""TODO : 15"""
# for loops = range, string, sequence, etc.
# EXAMPLE 1
"""for x in range(1, 11):
   print(x)
"""
# EXAMPLE 2
"""for x in reversed(range(1, 11)):
   print(x)

print("Happy New Year!")
"""
# EXAMPLE 3
"""for x in range(1, 11, 2):
   print(x)
"""
# EXAMPLE 4
"""credit_card = "1234-5678-9012-3456"

for x in credit_card:
   print(x)
"""
# CONTINUE
"""for x in range(1, 21):
   if x == 13:
       continue
   else:
       print(x)
"""
# BREAK
"""for x in range(1, 21):
   if x == 13:
       break
   else:
       print(x)
"""

"""TODO : 14"""
# Python compound interest calculator
"""
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
"""

"""TODO : 13"""
#while loop
# EXAMPLE 1
"""name = input("Enter your name: ")

while name == "":
   print("You did not enter your name!")
   name = input("Enter your name: ")

print(f"Hello {name}")
"""
# EXAMPLE 2
"""age = int(input("Enter your age: "))

while age < 0:
   print("Age can't be negative")
   age = int(input("Enter your age: "))

print(f"You are {age} years old")
"""
# EXAMPLE 3
"""food = input("Enter a food you like (q to quit): ")

while not food == "q":
   print(f"You like {food}")
   food = input("Enter another food you like (q to quit): ")

print("bye")
"""
# EXAMPLE 4
"""num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"You picked the number {num}")
"""

"""TODO : 12"""
# format specifiers
"""
# format specifiers = {:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (1)
# :(number) = allocate that many spaces (2)
# :0(number) = allocate and zero pad that many spaces (3)
# :< = left justify (4)
# :> = right justify (5)
# :^ = center align (6)
# :+ = use a plus sign to indicate positive value (7)
# := = place sign to leftmost position (8)
# :  = insert a space before positive numbers (9)
# :, = comma separator (10)
# :% = percentage format (11)

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 10.3
price5 = 2.0986
price6 = 7.452
price7 = 1.182
price8 = -6.279
price9 = 70.4234
price10 = 1982.293
price11 = 982.172
price12 = 1292.1723246
price13 = 15734232.1723246
print(f"price1 is: ${price1:.2f}")
print(f"price2 is: ${price2:10}")
print(f"price3 is: ${price3:06}")
print(f"price4 is: ${price4:<10}")
print(f"price5 is: ${price5:>10}")
print(f"price6 is: ${price6:^14}")
print(f"price7 is: ${price7:+}")
print(f"price8 is: ${price8:=20}")
print(f"price9 is: ${price9: }")
print(f"price10 is: ${price10:,}")
print(f"price11 is: ${price11:%}")
print(f"price12 is: ${price12:,.2f}")
print(f"price13 is: ${price13:+,.2f}")
"""

"""TODO : 11"""
# Application of Indexing
"""
email = input("Enter your email: ")
username = email[:email.find("@")]
domain = email[email.find("@")+1:]
print(f'Your username is {username} and domain is {domain}')
"""

"""TODO : 10"""
# Indexing [start : end : step]
"""credit_number = "1234-5678-9012-3456"

print(credit_number[0])
print(credit_number[0:4])
print(credit_number[:4])
print(credit_number[4:8])
print(credit_number[4:])
print(credit_number[-1])
print(credit_number[-4:])
print(credit_number[::2])
print(credit_number[::3])
"""
# EXERCISE 1
"""
credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
"""
# EXERCISE 2
"""
credit_number = "1234-5678-9012-3456"
credit_number = credit_number[::-1]
print(credit_number)

"""

"""TODO : 9"""
# STRING METHODS
"""
# name = input("Enter your name: ")
# phone_number = input("Enter your phone #: ")

# length = len(name)
# index = name.find(" ") #num
# name = name.capitalize() # The first letter change a capital
# name = name.upper() # lowercase to uppercase
# name = name.lower() # uppercase to lowercase
# result = name.isdigit()
# result = name.isalpha() # si el nombre esta vacio False sino True y si solo es palabra sin numero
# result = phone_number.count(" ") # Cuenta cuanto hay
# phone_number = phone_number.replace("-", "") # Reemplaza
# print(result)
"""
# EXERCISE
"""username = input("Enter a username: ")

if len(username) > 12:
   print("Your name can't be more than 12 characters")
elif not username.find(" ") == -1:
   print("Your username can't contain spaces")
elif not username.isalpha():
   print("Your username can't contain digits")
else:
   print(f"Welcome {username}!")
"""

"""TODO : 8"""
#and-or-not
"""
temp = 20
sunny = True

if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

if not sunny:
    print("It is cloudy")
else:
    print("It is sunny")
"""

"""TODO : 7"""
# Calculator
"""operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1sd number: "))
num2 = float(input("Enter the 2nd number: "))
result = 0
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = round(num1 / num2)
else:
    print(f"'{operator}' is not a valid operator")
    exit()
print(f'The result is {result}')
"""
# Conversion weight
"""# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")
"""
# Conversion temperature
"""
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temp}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
"""

"""TODO : 6"""
# if-elif-else
"""age = int(input("Enter your age: "))
if age >= 100:
    print("You are too old to sign")
elif age >= 18:
    print('You are now signed up!')
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up")
    """
"""response = input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you!")
else:
    print("Error")
"""
"""name = input("Whats your name?: ")
if name == "":
    print("You did not type in your name!")
else:
    print(f'Hello {name}')
"""
"""online = True
if online:
    print("The use is online")
else:
    print("The user is offline")
"""

"""TODO : 5"""
# Math
"""import math
num = math.pi
print(num)
"""
"""# friends = 9
# friends += 1
# friends -= 2
# friends *= 3
# friends /= 2
# friends **= 2
# friends %= 2
#print(friends)
"""
"""# x = 3.14
# y = -4
# z = 5
# result = round(x) #Redondear
# result = abs(y) #valor absoluto
# result = pow(4,2) #el primer valor a la potencia del segundo valor
# result = max(x,y,z) #maximo valor
# result = min(x,y,z) #minimo valor
# print(result)
"""
# import math
"""# x = 9.4
# print(math.pi) #Value of pi
# print(math.e) #Value of e
# result = math.sqrt(x) #Square Root
# result = math.ceil(x) # Round up
# result = math.floor(x) # Round down (Si por mas que el valor este 9.5 redondea a 9)
# result = math.log(2) #Logarithms
# print(result)
"""
"""
# Circumference del circle
radius = float(input('Enter the radius of a circle: '))
circumference = math.pi * (2 * radius)
print(f'The circumference is: {round(circumference,2)}')
"""
"""
# Area del circle
radius = float(input('Enter the radius of circle: '))
result = math.pi * (math.pow(radius,2))
print(f'The area of a circle is: {round(result,2)cm^2}')
"""
"""# Calculator Hypotenuse
a,b = float(input("Enter the value 'a': ")),float(input("Enter the value 'b': "))
hypotenuse = math.sqrt(math.pow(a,2) + math.pow(b,2))
print(f'The hypotenuse is: {round(hypotenuse,2)}')
"""

"""TODO : 4"""
# Input
"""
#Basic
input("Whats your name: ")
"""
"""name = input("Enter your name: ")
age = int(input("Enter your name: ")) # int or float
age = age + 1
print(f"Hello {name}")
print(f"You are {age} years old")
"""
"""length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))
area = length * width * height
print(f"The volume is : {area} cm^3")
"""
"""item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total,0)}") # Round decimals with respect to what you indicate: 0,1,2
"""

"""TODO: 3"""
# Casting Explicit and Implicit
"""name = 'Jesus'
age = 0
gpa = 1.9
student = True
"""
"""#type
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))
"""
# Explicit
"""
age = float(age)
print(type(age)) #Response: <class 'float'>
"""
"""gpa = int(gpa)
print(gpa) #Response: 1
"""
"""student = str(student)
print(student)
print(type(student)) #Response:<class 'str'>
"""
"""age = bool(age)
print(age) #age!=0 <> true  <::> age = 0 <> false
"""
"""name = bool(name)
print(name) # age!="" <> true  <::> age = "" <> false
"""
# Implicit
"""x = 2
y = 2.0

x = x / y
print(x) #Response: 1.0
"""

"""TODO: 2"""
# Variables
"""Print 2
    age = 20
    # print("I am  " + age +" years old")❌
    # print("I am "+str(age)+" years old")
    # print("I am", age, "years old")
    # print(f"I am {age} years old")
"""
# Integer
"""
age = 21
players = 2
quantity = 5

print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

"""
# Float
"""
gpa = 3.0
distance = 2.5
price = 10.99
print(f"Your gpa is {gpa}")
print(f"Your run {distance}Km")
print(f"The price is ${price}")
"""
# Strings
"""
name = 'Jesus'
food = "Pizza"
email = "coronel12jesus@gmail.com"
print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is:{email}")
"""
# Boolean
"""


online = True
for_sale = False
running = False

if running :
    print("The game is running")
else:
    print("The game is over")
"""
# tips
"""
# x,y,z = 1,2,3
# x = y = z = 1
# print(x)
# print(y)
# print(z)
"""

"""TODO: 1"""
# Introductory
"""
Print 1
    # print("My Cat is beautiful")
    # print("That Good")
"""

#Documentation Python