'''
name=input("What is your name?")
print("Hello " + str(name))

import math
print(math.e)
print(math.pi)
radius=5
area=5*2*math.pi
print(area)


import random
while True:
    num=random.randint(1,5)
    ans=int(input("Enter a number between 1 and 5: "))
    state=ans==num
    print(state)

    while ans>5:
            ans=int(input("Sorry, your number is not between 1 and 5. Please try again: "))
    else:
        if ans == num:
            print("Congratulations. You won.")
        else:
            print("Sorry you lost.")


def Function(args):
    print('this function is running')

while True:
git config


while True:
    num1=input('Enter first number: ')
    num2=input('Enter second number: ')
    status=(num1==num2)
    print(status)

'''
num=1
while True:
    num=num+1
    print(num)