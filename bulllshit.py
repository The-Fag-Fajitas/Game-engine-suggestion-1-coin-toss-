import random as r
tot = 0
v = 0
n = 0
done = 0
b = 0
list1 = ["tails", "heads"]
def add():
    return tot + 1
def put():
    n = input("What is your guess?\n ")
    v = n.lower()
    b = r.choice(list1)
def check():
    if v == b:
        return "You won the round!"
        tot = add()
    elif v != b:    #or do this: else:    lose()
        return "You lost the round!"
a = int(input("How rich are you?\n(How many coins can you flip?)\n "))
for i in range(a):
    print(f"Round{i + 1}:\n")
    put()
    check()
print(f"The game has ended. You got a score of {tot}.")