# import packages to extend Python.
from random import randint

#re-import our game variables 
from gameComponents import gameVars, winLose


print("\n**************/ RPS GAME /**************")
print("Computer lives: ", gameVars.computer_lives,"/",gameVars.total_lives)
print("Player lives: ", gameVars.player_lives,"/",gameVars.total_lives)
print("*****************************************")

print("\n\n==============/ NEW GAME /==============\n")


while gameVars.player is False:

	print("______________/ Round ",gameVars.level,"/______________\n")

	#computer's choice
	computer = gameVars.choices[randint(0, 2)]

	#player's choice
	print("Choose your weapon [rock, paper, scissors] ")


	gameVars.player = input("or choose to 'quit': ")
	if gameVars.player == "quit":
		print("You chose to quit")
		exit()

	# show the player's and computer's choices
	print("Player choice: " + gameVars.player)
	print("Computer chose: " + computer)


	# THE GAME CONDITIONS!!!
	if (computer == gameVars.player):
		print("Tie!")

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("Player -1")
			gameVars.player_lives -= 1
		else:
			print("Computer -1")
			gameVars.computer_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print("Player -1")
			gameVars.player_lives -= 1
		else:
			print("Computer -1")
			gameVars.computer_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("Player -1")
			gameVars.player_lives -= 1
		else:
			print("Computer -1")
			gameVars.computer_lives -= 1

	#player and computer lives displayed at the end of each round
	print("Player lives: ", gameVars.player_lives,"/",gameVars.total_lives)
	print("Computer lives: ", gameVars.computer_lives,"/",gameVars.total_lives)
	gameVars.level += 1


	if gameVars.player_lives is 0:
		winLose.winorlose("lost") #invokes the function here

	elif gameVars.computer_lives is 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False

# make the loop keep running by setting player back to False
# unset, so that the loop condition above will evaluate to True
	gameVars.player = False

