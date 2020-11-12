### This is not the smart version. It cannot detect any input error.

import random as r

#let's define all our variables here
list0 = []; list1 = ["heads", "tails"]; list2 = ["rock", "paper", "scissors"]; list3 = ["a", "b", "c"]; list4 = []
for i in range(5):
    list4.append(i + 1)
# lists

tot1 = 0; tot2 = 0; tot3 = 0; tot4 = 0; tot5 = 0   #totals
 
b = 0; s = 0; l = 0   #integers
c = 0; n = 0; v = 0   #strings

#now, let's define all our needed functions, or collections of code, here:

def add(tot5):
    return tot5 + 1

def add_half(tot5):
    return tot5 + (1 / 2)

def check_exist(l, list0):
    done = False
    while not done:
        if l not in list0:
            l = input("Please, enter something valid:\n ")
        elif l in list0:
            done = True

def check_face(v, b, tot5):
    if v == b:
        tot5 = add(tot5)
        return "You guessed the coins's face!\n"
    elif v != b:
        return "Too bad.\nYou did not guess the coin's face.\n"

def num_result(l, b, tot5):
    if l < b:
        return "You guessed low.\n"
    elif l > b:
        return "You guessed high.\n"
    else:         #or we can say: elif l == b:
        tot5 = add(tot5)
        return "You won the round!\n"

def check_result_ball(v, l, tot5):
    if v == c and l == b:
        tot5 = add(tot5)
        return "You won the round!\n"
    elif v != c or l != b:
        if v != c and l == b:
            return "You guessed the number.\n"
            tot5 = add_half(tot5)
        elif v == c and l != b:
            return "You guessed the letter.\nAs for the number,"
            tot5 = add_half(tot5)
            result(l, b, tot5)
        else:   #or do: elif v != c and l != b:
            return "You did not guess the ball.\n"


#now, let's start the game...

print("Welcome to the Game of Luck!\n\nMini-game one:\nCoin Toss\n")

#Coin Toss

a1 = 0
a1 = input("How rich are you?\n(How many coins can you flip?)\n ")
a2 = int(a1)

i = 0
for i in range(a2):
    
    print(f"Round: {i + 1}\n")
    c = r.choice(list1)
    
    n = input("What is your guess?\n ")
    
    v = n.lower()
    check_exist(v, list1)
    
    if v == c:
        tot1 += 1
        print("You guessed the coins's face!\n")
    elif v != c:
        print(f"Too bad:\n   You did not guess the coin's face.\n   It was {c}!\n")

print(f"Game one has ended.\nYou got a total score of {tot1} in this game.\n\nGame two: Guess my Secret Number\n" )

a1 = 0
a1 = input("How many secret numbers can you guess?\n(Remember, you have only 7 attempts to guess my number between 1 and 100)\n ")
a2 = int(a1)

i = 0
for i in range(a2):
    
    print(f"Round: {i + 1}\n")
    b = r.randint(1, 101)
    print("I'm thinking of a secret number, can you guess it?\n")
    
    for _ in range(7):
        
        print(f"Attempt: {_ + 1}")
        
        s = input("What is your guess?\n ")
        l = int(s)
        
        check_exist(l, range(1, 101))
        
        if l < b:
            print("You guessed low.\n")
        elif l > b:
            print("You guessed high.\n")
        else:         #or we can say: elif l == b:
            print("You won the round!\n")
            tot2 += 1
            break
        
    if l != b:
        print(f"My secret number was {b}.\n")

print(f"Game two has ended.\nYou got a total score of {tot2} in this game.\n\nGame three: Rock, Paper, Scissors\n")

