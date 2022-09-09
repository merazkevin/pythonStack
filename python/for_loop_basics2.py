#1Basic - Print all integers from 0 to 150.
for i in range(0,151):
    print(i)
#2Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001,5):
    if i % 5 ==0:
        print(i)
#3Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1,101):
    if i  % 10 == 0:
        print('coding')
    elif i % 5 == 0: 
        print('Coding Dojo')
    else:
        print(i)
print(i)
#4Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
num=0
for i in range(0,500000):
    num = i+num
print(f'dang!{num}')
#5Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018,0,-4):
    print(i)
#6Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNUm = 0
highnum = 10
mult = 3

for i in range(lowNUm,highnum):
    if i % mult ==0:
        print(i)

