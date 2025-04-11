##This is a code where the user inputs two numbers to define a range where the computer randomly generates a number
## and the use has to attempt and guess the number in as little attempts as possible

##Here we import the ability to use random
import random

##x will store the minumum value
x = int(input("Welcome to the Number Guesser Game! Please input the minimum value for the Guesser: "))

##This is a validation loop where y will store the maximum as long as it is greater than the minumum
while True:
    y = int(input("Now input the maximum value: "))
    if y>x:
        break
    else:
        print("The maximum cannot be less than or equal to the minumum, please input a new maximum: ")

## setting guess and attempts for later when the user attempts to guess
guess = 0
attempts = 0

##Code generates a random number using Random import
random_number = random.randint(x, y)

##Below is a while loop that recieves an input from the user and lets them know if they were too high, low or correct and records
## and exports their attempts and final guess
while guess!= random_number:
    print(attempts)
    guess = int(input(f"Guess a number between {x} and {y}: "))
    attempts += 1

    if guess < random_number:
        print("Too Low")
    elif guess > random_number:
        print("Too High")
    else:
        print(f"Congratulation! You guessed it right, {guess} was the correct number. It took you {attempts} attempts")




