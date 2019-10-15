import random


num=random.randint(1,5)
print(num)
ans=int(input("Enter a number between 1 and 5: "))
attempt=1

while True:
    if ans>5 or ans<1:
        ans=int(input("Sorry, your number is not between 1 and 5. Please try again: "))
    else:
        if ans == num:
            print("Congratulations. You won.")
            break
        elif ans!=num and attempt<3:
            ans=int(input("Sorry you lost. Please try again: "))
            attempt = attempt + 1
        else:
            print('Sorry, Out of guesses.')
            break

