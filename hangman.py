## Hangman game ##
import random #This is a built in function that had the random function within

def get_random_word():  #Pick a random word from the list words
	words = ["pizza", "cheese", "apples", "avocado", "sponge", "spongebob"]
	word = words[random.randint(0, len(words) -1)]
	return word

def show_word(word):	
	for character in word:
		print(character, " ", end="")
	print("")

def get_guess():
	print("Take your guess, enter a letter")
	return input()

def process_letter(letter, secret_word, blanked_word):
	result = False

	for i in range(0, len(secret_word)):
		if secret_word[i] == letter:
			result = True
			blanked_word[i] = letter

	return result


def print_strikes(number_of_strikes):
	for i in range(0, number_of_strikes):
		print("X ", end="")
	print("")

def play_word_game(): # This is where the actual game is run
	strikes = 0
	max_strikes = 3
	playing = True

	word = get_random_word()
	blanked_word = list("_" * len(word))

	while playing:
		show_word(blanked_word)
		letter = get_guess()
		found = process_letter(letter, word, blanked_word)

		if not found:
			strikes += 1
			print_strikes(strikes)

		if strikes >= max_strikes:
			playing = False

		if not "_" in blanked_word:
			playing = False
	
	if strikes >= max_strikes:
		print("You lost")
	else:
		print("We have a Winner!")
	

print("Let the game begin")
play_word_game() # Call the game function above
print("Game Over!") # If you run out of lives end game here
