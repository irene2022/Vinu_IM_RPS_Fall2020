from gameComponents import gameVars

#define win/lose function and refer to it (invoke it) in our game loop
def winorlose(status):

#print ("called winorlose", status)
	if status == "won":
		pre_message = "Congragulations! You have successfully defeated an AI. =D "
	else:
		pre_message = "You lost to an AI! XD Better luck next time. "
	print("\n==============/ GAME OVER /==============\n")

	print(pre_message + "Would you like to play again?")
	choice = input(" Y / N: ")

	if (choice == "N" or choice == "n"):
		print("Thank you for playing RPS! I hope you have a great rest of the day. :)")
		exit()
	elif (choice == "Y" or choice == "y"):
		print("So you've decided to play again? Awesome!\n")
		print("\n\n==============/ NEW GAME /==============\n")
		#reset player and computer lives
		#set player to False to reset the loop
		
		gameVars.player_lives = 3
		gameVars.computer_lives = 3
		gameVars.level = 1
		gameVars.player = False

	else:
		print("Invalide option. I'll ask you once more. ")
		choice = input("Y / N: ")
		if (choice == "N" or choice == "n"):
			print("Thank you for playing RPS! I hope you have a great rest of the day. :)")
			exit()
		else:
			print("So you've decided to play again? Awesome!")
			print("\n\n==============/ NEW GAME /==============\n")
			gameVars.player_lives = 3
			gameVars.computer_lives = 3
			gameVars.level = 1
			gameVars.player = False

