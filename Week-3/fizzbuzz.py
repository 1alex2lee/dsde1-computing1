num=1
while num<101:
    if (num/3).is_integer():
        if (num/5).is_integer():
            print('FizzBuzz')
            num=num+1
        else:
            print('Fizz')
            num=num+1
    elif (num/5).is_integer():
        print('Buzz')
        num=num+1
    else:
        print(num)
        num=num+1
        