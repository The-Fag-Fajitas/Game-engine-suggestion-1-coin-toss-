# Binary Search
import random

secret_nb = random.randint(1, 101)

the_list = range(1, 101)

i = 0

done = False
while not done:
     
    i += 1
    print(f"Attempt {i} :\n" )
       
    min_nb = the_list[0]
    
    max_nb = min_nb + the_list.index(the_list[len(the_list) - 1])
    
    guess = int((max_nb - min_nb) / 2) + min_nb
    print(f"Guessing... :  {guess}\n")

    guess_index = the_list.index(guess)

    if secret_nb < guess:
        
        print("The guess was high.\n")
        
        max_nb = the_list[guess_index - 1]
        the_list = range(min_nb, max_nb)
        
    elif secret_nb > guess:
        
        print("The guess was low.\n")
        
        min_nb = the_list[guess_index + 1]
        the_list = range(min_nb, max_nb + 1)
        
    else:
        
        print(f"The secret number {secret_nb} was found!\n")
        done = True
