import getpass
import time

print("Welcome to \"GUESS THE NUMBER\" game:")
print("Made by ShubhamProgmer, https://github.com/ShubhamProgmer")
print()
a = getpass.getpass(prompt="Please enter the password provided by Shubham to access the game: ")
if a == "1212":
	while 1:
		print()
		print("Welcome\nHow to play\n1.One player will activate a number from 1 to 100\n2.Other players will try to guess the number with the help of provided hints in 10 attemps only\nEnjoy!")
		print()
		input1 = getpass.getpass(prompt="Player 1 is requested to enter the number: ")
		while 1:
			if not input1.isnumeric():
				print("You have to provide a NUMBER")
				input1 = getpass.getpass(prompt="Player 1 is requested to enter the number: ")
				continue

			elif int(input1)<0 or int(input1)>100:
				print("You have to provide a number between 0 to 100")
				input1 = getpass.getpass(prompt="Player 1 is requested to enter the number: ")
				continue
			else:
				input2 = int(input1)
				break
		print()
		print("Now other player will guess the number entered by first one")
		print()
		i = 10

		print("Guess(es) left: ", i)
		input3 = input("Enter your guess: ")
		if input3 == "1001":
			print()
			print("Cheatcode activated - Get the chosen number")
			print(input1)
		elif input3 == "1212":
			print()
			print("Cheatcode activated - +10 guesses")
			i = i + 10
		while 1:
			input2 = int(input1)
			if input3.isnumeric():
				input4 = int(input3)
				while 1:
					if i == 1:
						print()
						print("GAME OVER\n\nChosen number was", input2)
						break
					elif input4 == input2:
						print()
						print("CONGRATULATIONS, The guessing team won!")
						break
					

					elif input4 > input2:
						i = i - 1
						print()
						print("WRONG GUESS\nHint: The right number is SMALLER than that you guessed\nGuess(es) left: ",i)
						print()
						input3 = input("Enter your guess: ")
						while 1:
							if input3.isnumeric():
								input4 = int(input3)
								break
							else:
								print("You are requested to enter a NUMBER")
								input3 = input("Enter your guess: ")
								continue
					elif input4 < input2:
						i = i - 1
						print()
						print("WRONG GUESS\nHint: The right number is GREATER than that you guessed\nGuess(es) left: ",i)
						print()
						input3 = input("Enter your guess: ")
						while 1:
							if input3.isnumeric():
								input4 = int(input3)
								break
							else:
								print("You are requested to enter a NUMBER")
								input3 = input("Enter your guess: ")
								continue
			else:
				print("You have to provide a NUMBER")
				input3 = input("Enter your guess: ")
				continue

			break
		lalchi = input("Do you want to play it again? (y/n) ")
		while lalchi != "y" and lalchi != "n":
			print("Enter a valid option please")
			lalchi = input("Do you want to play it again? (y/n) ")
		if lalchi == "y":
			continue
		else:
			print()
			print("Thank you for playing!\nExiting....")
			time.sleep(3)
			exit()
else:
	print("Kindly ask for password!")
	time.sleep(2)
	exit()

