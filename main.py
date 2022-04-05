import random
number = random.randint(1,10)
guesses = 5
while guesses != 0:
	print("Guesses Left: " + str(guesses))
	guess = int(input("Guess: "))

	if guess == number:
		print("Yay! You won!")
		exit()
	
	elif guess > number:
		print("Guess is too high!")

	elif guess < number:
		print("Guess is too low!")

	guesses -= 1
print("You ran out of guesses!")
  

        
        
