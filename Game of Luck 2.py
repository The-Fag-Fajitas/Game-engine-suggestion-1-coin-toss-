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
def check_int(s):
    done = False
    while not done:
        if type(s) != 'int':
            s = input("Please, reenter your number:\n ")
        else:
            done = True

def check_str(n):
    done = False
    while not done:
        if type(n) != "str":
            n = input("Please, reenetr your choice:\n ")
        elif type(n) == "str":
            done = True

def add(tot5):
    return tot5 + 1

def add_half(tot5):
    return tot5 + (1 / 2)

def check_exist(l, list0):
    done = False
    while not done:
        if l not in list0:
            if type(l) == "int":
                s = input("Please, reenter your number:\n ")
                check_int(s)
                l = int(s)
            elif type(l) == "str":
                l = input("Please, reenter your choice:\n ")
                check_str(l)
                v = l.lower()
            else:
                l = input("Please, enter something valid:\n ")
        elif l in list0:
            done = True

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

a1 = input("How rich are you?\n(How many coins can you flip?)\n")
check_int(a1)
a2 = int(a1)
for i in range (a2):
    print(f"Round: {i + 1}\n")
