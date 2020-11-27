# import packages to extend Python.
from random import randint

player_lives = 3
computer_lives = 3
total_lives = 3
level = 1

choices = ["rock", "paper", "scissors"]

# game = input("Would you like to play RPS? \nEnter 'quit' if you want to exit from the game: ")
'''
	if game == "quit":
		print("You chose to quit.")
		exit()
'''

def winorlose(status):

	if status == "won":
		pre_message = "Congragulations! You have successfully defeated an AI."
	else:
		pre_message = "You lost to an AI! XD Better luck next time."
	print("\n==============/ GAME OVER /==============\n")

	print(pre_message + "Would you like to play again?")
	choice = input(" Y / N: ")

	if (choice == "N" or choice == "n"):
		print("You chose to quit!")
		exit()
	elif (choice == "Y" or choice == "y"):
		print("You chose to play again!")
		#reset player and computer lives
		#set player to False to reset the loop
		global player_lives
		global computer_lives
		global level
		global player

		player_lives = 3
		computer_lives = 3
		level = 1
		player = False

	else:
		print("Invalide option.")
		choice = input("Y / N: ")
		if (choice == "N" or choice == "n"):
			print("You chose to quit!")
			exit()
		else:
			player_lives = 3
			computer_lives = 3
			level = 1
			player = False

# True and False are Boolean data types -> they are the equivalent of on or off, 1 or 0
player = False

print("**************/ RPS GAME /**************")
print("Computer lives: ", computer_lives,"/",total_lives)
print("Player lives: ", player_lives,"/",total_lives)
print("*****************************************")

print("\n\n==============/ NEW GAME /==============\n")


while player is False:

	print("______________/ Round ",level,"/______________\n")

	#computer's choice
	computer = choices[randint(0, 2)]

	#player's choice
	print("Choose your weapon [rock, paper, scissors] ")

	player = input("or choose to 'quit': ")
	if player == "quit":
		print("You chose to quit")
		exit()
	# player = True -> it has a value (rock paper scissor)

	# show the player and computer choices
	print("Player choice: " + player)
	print("Computer chose: " + computer)


	# game conditions
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

	#player and computer lives displayed at the end of each round
	print("Player lives: ", player_lives,"/",total_lives)
	print("Computer lives: ", computer_lives,"/",total_lives)
	level += 1


	if player_lives is 0:
		winorlose("lost") #invokes the function here

	elif computer_lives is 0:
		winorlose("won")

	else:
		player = False
		# print("\n==============/ GAME OVER /==============\n")
		# print("Congragulations! You have successfully defeated an AI!")
		# choice = input("Would you like to play again? Y / N: ")

		# if (choice == "N" or choice == "n"):
		# 	print("You chose to quit!")
		# 	exit()
		# elif (choice == "Y" or choice == "y"):
		# 	print("You chose to play again!")
		# 	#reset player and computer lives
		# 	#set player to False to reset the loop
		# 	player_lives = 2
		# 	computer_lives = 2
		# 	level = 1
		# 	player = False

		# else:
		# 	print("Invalide option.")
		# 	choice = input("Y / N: ")
		# 	if (choice == "N" or choice == "n"):
		# 		print("You chose to quit!")
		# 		exit()
		# 	else:
		# 		player_lives = 2
		# 		computer_lives = 2
		# 		level = 1
		# 		player = False



# make the loop keep running by setting player back to False
# unset, so that the loop condition above will evaluate to True
	player = False