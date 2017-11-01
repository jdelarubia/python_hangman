
import random
import sys

#TODO: LET USE CHOOSE DIFFICULTY



#Global Game Vars
chances = 6
missed = []
discovered = []
display = ""


#set up game by choosing the target word from a file

def game_setup():
	#read in options
	with open('hang_words.txt', 'r') as open_file:
	    all_text = open_file.read()

	word_list = all_text.split("\n")
	#choose random word
	target = word_list[random.randrange(0,len(word_list))]
	print target
	return target

"""Lets the user submit a letter guess, validates the input,
shows the letters they missed or reveals the word with the letters
they correctly guessed

"""

def guess_letter(target_word):
	correct_guess_text = ["You guessed it!", "Nice job!","That's right!","I see what you did there.", "Keep it up!", "Just a few more to go!"]
	global chances 
	global display
	target = target_word
	display = ""

	guess = raw_input("Guess a letter: ")


	if guess.isalpha():
		#TODO add a way to exit the game
		if len(guess) ==1:
			guess = guess.lower()
			#print "You guessed:  %s" % guess 
			if guess not in target:
				if guess not in missed:
					missed.append(guess)
					print "That's not right. Try again"
					chances -=1
				else:
					print "You already guessed that. Try again"
				print "Missed Letters: ",				
				print missed
			else:
				if guess not in discovered:
					discovered.append(guess)

					#TODO choose a random confirm test string
					print correct_guess_text[random.randrange(0, len(correct_guess_text))]
					#print "That's right!"
				else:
					print "You already guessed that. Try again"



		else:
			if guess == "exit" or guess == "quit":
				sys.exit()
			else:
				print "You can only guess one letter at a time"
	else:
		print "Try guessing a letter"

	for n in target:
		if n in discovered:
			display+= n
		else:
			display+='_'
	print display #testing the placement of this
	

	
#starts the game and shares the victory or defeat message

def play():

	target = game_setup()
	while chances >0:
		guess_letter(target)
		print "You hace %s gueeses remaining." % chances
		if display == target:
			print "You win!"
			break	
	else:
		print "Game Over! You Lose"



play()
