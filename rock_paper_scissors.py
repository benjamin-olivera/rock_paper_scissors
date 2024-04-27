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

#Write your code below this line 👇
import random
options = [rock, paper, scissors]
human_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
human_choice = int(human_input)
machine_choice = random.randint(0,2)

print("You Choice")
print(options[human_choice])
print("Computer Choice")
print(options[machine_choice])

if human_choice == machine_choice:
  print("Draw!")
elif (human_choice == 0 and machine_choice == 2) or (human_choice == 1 and machine_choice == 0) or (human_choice == 2 and machine_choice == 1 ):
  print("You Win!")
else:
  print("You Lose!")