import random

x = int(input("Guess the Number: "))
randomInt = random.randint(1, 100)
while True:
    if x > randomInt:
        print("Incorrect! Number Too High")
        x = int(input("Re-Enter Number: "))
    elif x < randomInt:
        print("Incorrect! Number Too Low")
        x = int (input("Re-Enter Number: "))
    else:
        print("Correct!")
        break