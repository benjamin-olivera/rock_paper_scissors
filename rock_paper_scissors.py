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
machine_choise = random.randint(0,2)
num_imput= input("Choose rock, paper or scissors:\nType 0 for rock , type 1 for paper and 2 for scissors \n" )
human_choise = int(num_imput)
if human_choise == "0":
  print(rock)
  print(machine_choise)
  if human_choise > machine_choise:
    print("You Win")
  else:
    print("You lose")
elif human_choise == "1":
  print(paper)
  print(machine_choise)
  if human_choise > machine_choise:
    print("You Win")
  else:
    print("You lose")
elif human_choise == "2":
  print(scissors)
  print(machine_choise)
  if human_choise > machine_choise:
    print("You Win")
  else:
    print("You lose")
else:
  print(human_choise)
  print(machine_choise)
  print("Is a Draw! try again")
