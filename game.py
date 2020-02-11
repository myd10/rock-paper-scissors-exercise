#rock-paper-scissors-exercise

import random

print("Welcome to Python's Rock, Paper, Scissors, Shoot!")

#while still_playing = "Yes":
#question = ("Do you want to play again?")

valid_options = ["Rock", "Paper", "Scissors"] #list data type

print("Please enter either Rock, Paper, or Scissors")
your_choice = (input("Choose either Rock, Paper, or Scissors: ").lower().title())

if your_choice in valid_options: #searching the list for a variable
    pass
else:
    print("Restart with a different fighter!")
    quit()


CPU_choice = random.choice(valid_options)


print("------------------")
print("You chose", your_choice, "as your fighter")
print("Computer chose", CPU_choice)
print("-------------------")

#choosing Rock
if your_choice == "Rock" and CPU_choice == "Paper":
    print("You lose :( ")
elif your_choice == "Rock" and CPU_choice == "scissors":
    print("You win!!")
elif your_choice == "Rock" and CPU_choice == "Rock": 
    print("You tied :/")
#Choosing Paper
elif your_choice == "Paper" and CPU_choice == "Rock": 
    print("You win!!")
elif your_choice == "Paper" and CPU_choice == "Scissors": 
    print("You lose :(")
elif your_choice == "Paper" and CPU_choice == "Paper": 
    print("You tied :/")
#Choosing Scissors
elif your_choice == "Scissors" and CPU_choice == "Rock": 
    print("You lose :(")
elif your_choice == "Scissors" and CPU_choice == "Scissors": 
    print("You tied :/")
elif your_choice == "Scissors" and CPU_choice == "Paper": 
    print("You Win!!")


print("Please play again!")

#still_playing = input("Do you want to play again? Yes or No").lower().title()