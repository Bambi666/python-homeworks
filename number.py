import random

random_number = random.randint(1, 100)
print(random_number)

takes = 7

print("Guess the number from 1 to 100, you have 7 takes!")

while takes > 0:

    takes -= 1
    guess = int(input("Your number: "))

    if random_number == guess:
        print("You're god damn right!")
        break

    else:

        if random_number > guess:
            print("Number too low")
        else:
            print("Number too high")

        print("Loser!")
