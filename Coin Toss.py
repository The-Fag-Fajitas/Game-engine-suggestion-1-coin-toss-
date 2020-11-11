import random as r

mode = input("Do you want to make the game endless?:")


def coin():
    tot = 0
    list1 = ["heads", "tails"]
    try:

        n = input("What is your guess?:\n ")
        if n == "quit":
            quit()
        while n not in ["heads", "tails", "Tails", "Heads"]:
            raise KeyError

        a = int(input("How rich are you?\n(How many coins can you flip?)\n "))
        for i in range(a):
            b = r.choice(list1)
            if n == b:
                tot += 1
            elif n.lower() == b:
                tot += 1
            else:
                tot = tot
    except ValueError:
        print("Please enter a valid number")
    except KeyError:
        print("Please write the guess properly in uppercase or lowercase")

    print(f"The game has ended. You got a score of {tot}.")


while mode in ["Yes", "yes"]:
    coin()
if mode in ["No", "no"]:
    coin()

