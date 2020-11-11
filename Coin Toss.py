import random as r

list1 = ["heads", "tails"]

tot = 0
try:

    n = input("What is your guess?:\n ")
    if type(n) != str:
        raise TypeError("Please write a word")
    if n not in ["heads", "tails", "Tails", "Heads"]:
        raise TypeError("Please write the guess properly")
    a = int(input("How rich are you?\n(How many coins can you flip?)\n "))
    # rn is the number of rounds
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
except TypeError:
    print("Please Enter A Word")

print(f"The game has ended. You got a score of {tot}.")

