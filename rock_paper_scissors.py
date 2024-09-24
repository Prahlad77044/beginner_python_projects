import random
print("Lets play rock paper scissors:")
user=input("input rock paper or scissors:")
def game(user):
    guess=random.choice(['rock','paper','scissors'])
    print(f"computers choice:{guess}")    
    if (user==guess):
        print("It's a tie")
    elif (user=='rock'and guess=='paper') or (user=='paper'and guess=='scissors') or (user=='scissors'and guess=='rock'):
        print('You lose')
    else:
        print('You won!!!')    
game(user)        