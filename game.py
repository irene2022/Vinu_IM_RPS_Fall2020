# import packages to extend Python.
from random import randint

#re-import our game variables 
from gameComponents import gameVars, winLose, compareGame


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

	if computer == gameVars.player:
		compareGame.game("tie")

	elif computer == "rock":
		compareGame.game("rock")

	elif computer == "paper":
		compareGame.game("paper")

	elif computer == "scissors":
		compareGame.game("scissors")

	else:
		print("Invalid option.")


# make the loop keep running by setting player back to False
# unset, so that the loop condition above will evaluate to True
gameVars.player = False

