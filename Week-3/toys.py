'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''

# write a function that adds 1
# to the input and prints the result
def inc(a):
    a=a+1
    print(a)


# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    a=a+1
    return a # hint this is incomplete


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    c=a+b
    print(c)
    return c

# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return

def sum_inc(a, b):
    c=sum(a,b)
    d=inc_return(c)
    return d



# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    status=(a%2==0)
    return status


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    sentence=''
    for i in range(repeat):
        sentence=(sentence+phrase)
    # hint: you can add strings together 
    # in order to concatenate them
    return sentence

