from gameComponents import gameVars, winLose

def game(compare):

	if compare == "tie":
		pre_message = "It's a Tie!"
	elif compare == "rock":
		if (gameVars.player == "scissors"):
			print("Player -1")
			gameVars.player_lives -= 1
		else:
			print("Computer -1")
			gameVars.computer_lives -= 1

	elif compare == "paper":
		if (gameVars.player == "rock"):
			print("Player -1")
			gameVars.player_lives -= 1
		else:
			print("Computer -1")
			gameVars.computer_lives -= 1

	elif compare == "scissors":
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

	#invokes the function here
	if gameVars.player_lives is 0:
		winLose.winorlose("lost") 

	elif gameVars.computer_lives is 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False

