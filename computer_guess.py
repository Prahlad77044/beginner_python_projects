import random
print(f"Lets make computer guess a number between 1 and y")
y=int(input('y='))
def computer_guess(y):
    low=1
    high=y
    feedback=''
    while feedback!='C':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high(H),too low(L) or correct(C): ")
        if feedback=='H':
            high=guess-1
        elif feedback=='L':
            low=guess+1
    print(f"The correct number was {guess}")        
        
computer_guess(y)            


   