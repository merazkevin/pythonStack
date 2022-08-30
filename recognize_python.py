num1 = 42 #variable Declaration
num2 = 2.3 #variable declaration 
boolean = True #operations
string = 'Hello World' 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
    #prints it's lower    

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

    #prints its a long WOrd

for x in range(5):
    print(x)
    # returns 0-4
for x in range(2,5):
    print(x)
    #returns 2-4
for x in range(2,10,3):
    print(x)
    #returs  2-10 not including 3?
x = 0
while(x < 5):
    print(x)
    x += 1
# returns 0-4
pizza_toppings.pop()
#removes last element of pizza toppings
pizza_toppings.pop(1)
#removes element at index 1
print(person)
#prints out whole person list
person.pop('eye_color')
# revomes last eelement of person\eye_color

print(person)
# person['name'] = 'George'


for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
    #after 1st

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
#prints hello

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#prints hellox10
print_hello_x_or_ten_times()
#prints hellox10
print_hello_x_or_ten_times(4)
#prints hellox10 * 4?

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)