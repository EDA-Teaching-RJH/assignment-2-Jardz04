import random
correct_number = random.randint(1,100)
guess = None
print("Hello, welcome to the Guessing number game.")
print("I've picked a number between 1 and 100. Lets see if you can figure it out.")
while guess != correct_number:
    try:
        guess = int(input("Enter your guess: "))
        if guess < correct_number:
            print("Too low! Try again.")
        elif guess > correct_number:
            print("Too high! Try again.")
        else:
            print("Well done! You guessed the correct number.")
    except ValueError:
        print("Please enter a valid integer.")
        print("Thanks for playing!")
