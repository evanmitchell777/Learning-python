import random


choices=['rock','paper','scissors']
uc=input("enter: rock, paper or scissors: ")
cc=random.choice(choices)

print("I choose",cc)

if uc == 'rock' and cc == 'rock':
    print("tie")
elif uc == 'rock' and cc =='paper':
    print('you lose')
elif uc== 'rock' and cc=='scissors':
    print("you win!")
elif uc=='paper' and cc=='paper':
    print("tie")
elif uc=='paper' and cc=='rock':
    print("you win!")
elif uc=='paper' and cc=='scissors':
    print("you lose")
elif uc == 'scissors' and cc== 'scissors':
    print("tie")
elif uc=='scissors' and cc=='rock':
    print("you lose")
elif uc== 'scissors' and cc=='paper':
    print("you win!")

else:
    print("enter a valid choice")
