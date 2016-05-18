import random

user_guess = int(input("You have five chances to choose a number"
                       " between 1 and 100 and enter a guess "))
computer_guess = int(random.randint(1, 100))
counter = 0
computer_guess = 67

if user_guess == computer_guess:
    print("You are the numerical ward of the north")
    exit()

while user_guess != computer_guess:
    if user_guess > computer_guess:
        print("Your number is more than right John snow")

        counter += 1
        if counter ==5:
            print("You know nothing John Snow")
            break
        user_guess = int(input("Choose a number between 1 and 100 and enter a guess"))

    elif user_guess < computer_guess:
        print("Your number is less than right John snow")

        counter += 1
        if counter ==5:
            print("You know nothing John Snow")
            break
        user_guess = int(input("Choose a number between 1 and 100 and enter a guess"))


    else:
        print("You guessed correctly")
        print("You guessed in " + str(counter + 1) + " turns")



