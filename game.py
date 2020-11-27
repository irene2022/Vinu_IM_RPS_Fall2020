from random import randint

player_lives = 3
computer_lives = 3
total_lives = 3

choices = ["rock", "paper", "scissors"]

computer = choices[randint(0, 2)]

player = input("Chose your weapon [rock, paper, scissors]: ")

print("Player choice: " + player)

print("Computer chose: " + computer)

if (computer == player):
	print("Tie!")

elif (computer == "rock"):
	if (player == "scissors"):
		print("Player -1")
		player_lives -= 1
	else:
		print("Computer -1")
		computer_lives -= 1

elif (computer == "paper"):
	if (player == "rock"):
		print("Player -1")
		player_lives -= 1
	else:
		print("Computer -1")
		computer_lives -= 1

elif (computer == "scissors"):
	if (player == "paper"):
		print("Player -1")
		player_lives -= 1
	else:
		print("Computer -1")
		computer_lives -= 1


print("Player lives: ", player_lives)
print("Computer lives: ", computer_lives)