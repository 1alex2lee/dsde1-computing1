'''
fuzzy.py

Lint this file using PyLint.
'''

# This function does some maths on three numbers.
def maths(input_a, input_b, input_c):
    '''3a - b + c'''
    result = input_a * 3 - input_b + input_c
    return result

# This function returns True or False.
def choices(question):
    '''checks if question is true'''
    if question is True:
        return True
    return False

def main():
    '''runs first function'''
    # first function takes three numbers
    answer = maths(3, 9, 2.3)
    print(answer)

    # second function takes a True or False
    newanswer = choices(True)
    print(newanswer)

if __name__ == '__main__':
    main()
