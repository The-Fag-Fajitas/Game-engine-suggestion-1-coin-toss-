# testing sandbox #

import random as r

list3 = ["a", "b", "c"]; list4 = []
for i in range(5):
    list4.append(i + 1)
    
tot4 = 0

def check_exist(l, s, list0):
    done = False
    while not done:
        if l not in list0:
            s = input("Please, enter something valid:\n ")
            
            # Fun
            if s.lower() == "something valid":
                s = input("No, really, enter something valid:\n ")
                if s.lower() == "something valid":
                    done1 = False
                    while not done1:
                        if s.lower() == "something valid":
                            s = input("No more fun for you!\n ")
                        elif s.lower() != "something valid":
                            done1 = True
                            
        elif l in list0:
            done = True

# Ball Permutaion

print("Discription: In this game, we have a specified number of identical urns - by you -\nfrom which we draw a ball wach round.\nThe balls in the urn are noted with a letter (a through c)\nand a number (1 through 5).\nYou have to guess it in three attempts!")

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
        check_exist(v, n, list3)
        v = n.lower()
        
        s = input("What is the ball's number?\n ")
        l = int(s)
        check_exist(l, s, list4)
        l = int(s)
        
        if v == c and l == b:
        
            tot4 += 1
            print("You guessed the ball!\n")
        
        elif v != c or l != b:
            
            if l < b:
                            
                print("You guessed low for the number.\n")
                        
            elif l > b:
                            
                print("You guessed high for the number.\n")
        
        if v == c and l != b:
                
            print("You got the leter right!\n")
                    
        elif v != c and l == c:
                
                print("You got the number right, but got the letter wrong.\n")
                
        elif v != c and l != b:        
                    
            print("You did not guess the ball.\n")
                
    if v !=c and l !=b:
        
        print(f"My ball was \'{b}{c}\'")