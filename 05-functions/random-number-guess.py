import random

number = random.randint(1, 20)
attempts = 0

while attempts < 7:
    guess = int(input("Enter a number betwee 1 to 20: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("You guessed it!")
        break
    attempts += 1

if attempts == 7:
    print(f"You lost! The number was {number}")