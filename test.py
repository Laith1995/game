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
N=int(input("What do you choose ? Type 0 for rock ,1 for paper or 2 for scissors"))
if N>=0 and N<=2 :
    print(you[N])
    import random
    c=[rock,paper,scissors]
    x=random.choice(c)
    print("Computer choose :")
    print(x)
    if N==0 and x==rock or N==1 and x==paper or N==2 and x==scissors:
        print("It's a draw !")
    elif N ==0 and x==scissors or N==1 and x==rock or N==2 and x==paper:
        print("You won !")
    elif x==rock and N==2 or x==paper and N==0 or x==scissors and N==1:
        print("You lost !")

else:
    print("You typed an invalid number, you lose!")
