# import random

# print('Welcome to Python!')

# print('This is a loop printing 5 times')
# for x in range(1, 6):
#     print(f'x is: {x}')

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
# day = random.choice(weekdays)

# print(f'Today is: {day}')

# if day == 'Monday':
#     print('It will be a long week!')
# elif(day == 'Friday'):
#     print('Woohoo, time for the weekend!')
# else:
#     print('Not quite there yet.')

#     name = "Zen"
# print(name)

# if 5 > 2:
#     print("Five is greater than two!")
# else: 
#     print("five is not greater than two!")
# fruits = ["apple", "banana", "cherry"]
# x, z, y = fruits
# print(y)
SumOfAll = 0
for i in range(0,5000001):
    if (i%2==1):
        SumOfAll = SumOfAll + i 
print(SumOfAll)