rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
you=[rock,paper,scissors]
try:
    N=int(input("What do you choose ? Type 0 for rock ,1 for paper or 2 for scissors"))
except:
    print("You typed an invalid number, you lose!")
    import sys
    sys.exit()
if N>=0 and N<=2 :
    print(you[N])
    import random
    x=random.choice(you)
    print("Computer choose :")
    print(x)
    z=you.index(x)

    if N==z :
        print("It's a draw !")
    elif N ==0 and z==2 or N==1 and z==0 or N==2 and z==1:
        print("You won !")
    elif z==0 and N==2 or z==1 and N==0 or z==2 and N==1:
        print("You lost !")

else:
    print("You typed an invalid number, you lose!")


