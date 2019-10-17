import math

def period(L,g):
    T=''
    try:
        T=2*math.pi*math.sqrt(L/g)
    except ValueError or TypeError or ZeroDivisionError:
        print('You did not enter a number. ')
    return T
