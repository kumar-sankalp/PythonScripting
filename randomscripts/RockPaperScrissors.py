import random
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
choice=int(input("what do you choose ? Type 0 for Rock 1 for Paper 2 for scissors" ))
comp_choice=random.randint(0,2)
if choice == 0 && comp_choice == 1:
    print('You Win')
if choice == 0 && comp_choice == 2:
    print('You Win') 
if choice == 1 && comp_choice == 2:
    print('You Lose')        
if choice == comp_choice:
    print('Game Draw')

