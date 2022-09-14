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
user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_selection > 2 or user_selection < 0 :
  print("You entered an invalid input!")
  
computer_selection = random.randint(0,2)
if user_selection == 0 and computer_selection == 2:
  print(f"You chose: rock\n{rock}")
  print(f"Computer chose: scissor\n{scissors}")
  print("You won")
elif user_selection == 0 and computer_selection == 1:
  print(f"You chose: rock\n{rock}")
  print(f"Computer chose: paper\n{paper}")
  print("You lose")
elif user_selection == 0 and computer_selection == 0:
  print(f"You chose: rock\n{rock}")
  print(f"Computer chose: rock\n{rock}")
  print("You draw")
elif user_selection == 1 and computer_selection == 0:
  print(f"You chose: paper\n{paper}")
  print(f"Computer chose: rock\n{rock}")
  print("You won")
elif user_selection == 1 and computer_selection == 1:
  print(f"You chose: paper\n{paper}")
  print(f"Computer chose: paper\n{paper}")
  print("You draw")
elif user_selection == 1 and computer_selection == 2:
  print(f"You chose: paper\n{paper}")
  print(f"Computer chose: scissor\n{scissors}")
  print("You lose")
elif user_selection == 2 and computer_selection == 0:
  print(f"You chose: scissor\n{scissors}")
  print(f"Computer chose: rock\n{rock}")
  print("You lose")
elif user_selection == 2 and computer_selection == 1:
  print(f"You chose: scissor\n{scissors}")
  print(f"Computer chose: paper\n{paper}")
  print("You won")
elif user_selection == 2 and computer_selection == 2:
  print(f"You chose: scissor\n{scissors}")
  print(f"Computer chose: scissor\n{scissors}")
  print("You draw")
