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

## all functions were deleted....

#now, let's start the game...

print("Welcome to the Game of Luck!\n\nMini-game one:\nCoin Toss\n")

#Coin Toss

a1 = input("How rich are you?\n(How many coins can you flip?)\n ")
a2 = int(a1)

for i in range(a2):
    
    print(f"Round: {i + 1}\n")
    c = r.choice(list1)
    
    n = input("What is your guess?\n ")
    
    v = n.lower()

    done = False
    while not done:

        if v not in list1:
            n = input("Please, enter something valid:\n ")
            v=n.lower()

            # Fun
            if v == "something valid":
                n = input("No, really, enter something valid:\n ")
                v = n.lower()
                done1 = False
                while not done1:
                    if v == "something valid":
                        n = input("No more fun for you!\n ")
                        v = n.lower()
                    elif v != "something valid":
                        done1 = True
                            
        elif v in list1:
            done = True

    if v == c:
        tot1 += 1
        print("You guessed the coins's face!\n")
    elif v != c:
        print(f"Too bad:\nYou did not guess the coin's face.\nIt was {c}!\n")

if a2 > 0:
    print(f"Game one has ended.\nYou got a total score of {tot1} in this game.\n\nGame two: Guess my Secret Number\n" )
elif a2 == 0:
    print("Game two: Guess my Secret Number\n")

# Guess my number

a1 = input("How many secret numbers can you guess?\n(Remember, you have only 7 attempts to guess my number between 1 and 100)\n ")
a2 = int(a1)

for i in range(a2):
    
    print(f"Round: {i + 1}\n")
    b = r.randint(1, 101)
    print("I'm thinking of a secret number, can you guess it?\n")
    
    for _ in range(7):
        
        print(f"Attempt: {_ + 1}")
        
        s = input("What is your guess?\n ")
        l = int(s)
        
        done = False
        while not done:
            if l not in range(1, 101):
                s = input("Please, enter something valid:\n ")
                l = int(s)
                
                # Fun
                if s.lower() == "something valid":
                    s = input("No, really, enter something valid:\n ")
                    done1 = False
                    while not done1:
                        if s.lower() == "something valid":
                            s = input("No more fun for you!\n ")
                        elif s.lower() != "something valid":
                            done1 = True
                                
            elif l in range(1, 101):
                done = True

        l = int(s)
        
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

if a2 > 0:
    print(f"Game two has ended.\nYou got a total score of {tot2} in this game.\n\nGame three: Rock, Paper, Scissors\n")
elif a2 == 0:
    print("Game three: Rock, Paper, Scissors\n")

# Rock, Paper, Scissors

a1 = input("How many times do you want to play this game?\n ")
a2 = int(a1)

for i in range(a2):
    
    print(f"Round: {i + 1}\n")
    
    c = r.choice(list2)
    
    n = input("Enter is your choice:\n ")
    
    v = n.lower()

    done = False
    while not done:
        if v not in list2:
            n = input("Please, enter something valid:\n ")
            v = n.lower()
            
            # Fun
            if v == "something valid":
                n = input("No, really, enter something valid:\n ")
                v = n.lower()
                done1 = False
                while not done1:
                    if v == "something valid":
                        n = input("No more fun for you!\n ")
                        v = n.lower()
                    else:
                        done1 = True
                            
        elif v in list2:
            done = True
    
    done = False
    while not done:
        print("Rock, Paper, Scissors, SHOOT!")
        if v == c:
            c = r.choice(list2)
            n = input("It's a tie! Please, chose again:\n ")
            v = n.lower()
           
            done = False
            while not done:
                if v not in list2:
                    n = input("Please, enter something valid:\n ")
                    v = n.lower()
                    
                    # Fun
                    if v == "something valid":
                        n = input("No, really, enter something valid:\n ")
                        v = n.lower()
                        done1 = False
                        while not done1:
                            if v == "something valid":
                                n = input("No more fun for you!\n ")
                                v = n.lower()
                            else:
                                done1 = True
                                    
                elif v in list2:
                    done = True

        elif v != c:
            
            done = True
            
            if v == "rock" and c == "paper":
                print(f"The opponent chose {c}.\nYou lost.\n")
            elif v == "scissors" and c == "rock":
                print(f"The opponent chose {c}.\nYou lost.\n")
            elif v == "paper" and c == "scissors":
                print(f"The opponent chose {c}.\nYou lost.\n")
            # There must be a better way to express this
            
            else:
                tot3 += 1
                print(f"The opponent chose {c}.\nYou won!\n")

if a2 > 0:
    print(f"Game three has ended.\nYou got a total score of {tot3} in this minigame.\n\nGame four: Guessing a Ball Permuation")
elif a2 == 0:
    print("Game four: Guessing a Ball Permutation")

# Ball Permutaion

print("Discription: In this game, we have a specified number of identical urns - by you -\nfrom which we draw a ball wach round.\nThe balls in the urn are noted with a letter (a through c)\nand a number (1 through 5).\nYou have to guess it in three attempts!\n")

a1 = input("How many Urns do you wish us to summon to you?\n ")
a2 = int(a1)

for i in range(a2):
    print(f"Round: {i + 1}\n")
    
    b = r.choice(list4)   #or do : r.randint(1, 6)
    c = r.choice(list3)
    
    for _ in range(3):
        
        print(f"Attempt: {_ + 1}\n")
        
        n = input("What is the ball's letter?\n ")
        v = n.lower()
        done = False
        while not done:
            if v not in list3:
                n = input("Please, enter something valid:\n ")
                v = n.lower()
                
                # Fun
                if v == "something valid":
                    n = input("No, really, enter something valid:\n ")
                    v = n.lower()
                    done1 = False
                    while not done1:
                        if v == "something valid":
                            n = input("No more fun for you!\n ")
                            v = n.lower()
                        else:
                            done1 = True
                                
            elif v in list3:
                done = True
        
        s = input("What is the ball's number?\n ")
        l = int(s)

        done = False
        while not done:
            if l not in list4:
                s = input("Please, enter something valid:\n ")
                l = int(s)
                
                # Fun
                if s.lower() == "something valid":
                    s = input("No, really, enter something valid:\n ")
                    done1 = False
                    while not done1:
                        if s.lower() == "something valid":
                            s = input("No more fun for you!\n ")
                        elif s.lower() != "something valid":
                            done1 = True
                                
            elif l in list4:
                done = True
        
        l = int(s)
        
        if v == c and l == b:
        
            tot4 += 1
            print("You guessed the ball!\n")
            break
        
        elif v != c or l != b:
            
            if l < b:
                            
                print("(You guessed low for the number)\n")
                        
            elif l > b:
                            
                print("(You guessed high for the number)\n")
        
        if v == c and l != b:
                
            print("You got the letter right!\n")
            tot4 += (1 / 2)
                    
        elif v != c and l == c:
                
            print("You got the number right, but got the letter wrong.\n")
            tot4 += (1 / 2)
                
        elif v != c and l != b:        
                    
            print("You did not guess the ball.\n")
                
    if v !=c and l !=b:
        
        print(f"My ball was \'{b}{c}\'")
        
if a2 > 0:
    print(f"Game four has ended.\nYour total score in this game is {tot4}.\n\nThe Game of Luck has ended.\nYou got a total score of {tot1 + tot2 + tot3 + tot4}.\n\nBe on the look-out for a future update to the game because it will be updated.\nThank you for playing The Game of Luck!")
elif a2 == 0:
    print("You did not play the Game of Luck.")