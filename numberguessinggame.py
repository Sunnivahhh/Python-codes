import random
count = 0

def code(tries, level_num):
    count = 0
    random_number = random.randint(1, level_num)
    while count < tries:
        num = int(input(f"Enter a number from 1 to {level_num}: "))
        count += 1
        difference = random_number - num  

        if num == random_number:
            print("You have guessed it correctly!")
            return
        elif random_number > num:
            print(f"Hint: The number is greater than {num}")
            if difference <= 5:
                print("Hint: You are within the range of 5!")
            elif difference <= 10:
                print("Hint: The number you are guessing is within the range of 10.")
            else:
                print("Hint: You are far away.")
            print(f"You still have {tries - count} attempts left!")

        elif random_number < num:
            print(f"Hint: The number is less than {num}")
            if -difference <= 5:
                print("Hint: The number is within the range of the difference 5")
            elif -difference <= 10:
                print("Hint: The number is within the range of the difference 10")
            else:
                print("Hint: You are far away.")
            print(f"You still have {tries - count} attempts left!")
        else:
            print("Incorrect! Try again.")
            print(f"You still have {tries - count} attempts left!")
    print(f"Out of tries! The number was {random_number}")


while True:
    a = input("Enter what level you want to play (easy/medium/hard): ")
    if a.lower() == "easy":
        tries = 5
        level_num = 20
        code(tries, level_num)

    elif a.lower() == "medium":
        code(5, 50)

    elif a.lower() == "hard":
        code(3, 100)

    else:
        print("Error! Please try again")

    decision = input("Would you like to continue? (y/n): ").lower()
    if decision == "n":
        print("Thank you for playing the number guessing game!")
        break
    elif decision == "y":
        continue
    else:
        print("Error! Please enter 'y' or 'n'")










