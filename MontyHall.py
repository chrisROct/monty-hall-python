#! sys/bin/python3
from random import randint
import sys

# method to clear the console
def clear(n):
    for i in range(n):
        print("")

# method that handles the logic of the monty hall problem
def montyhall():
    print("Welcome to the Monty Hall Problem! \nIn this game show, a contestant chooses one of three doors in hopes of winning a prize.\nBehind two of the doors, there is no prize. After our contestant has selected a door, \nthe host of our gameshow removes one of the losing doors.\n The Host then turns to you and asks:")
    clear(3)
    print("Would you like the contestant to flip a coin to randomly choose to switch or stay every time?\n0 = Yes, 1 = No.")
    random = int(input("Enter 0, or 1: " ))
    clear(2)
    # here we determine the values to decide which choice our contestant will make throughout. Switch? Stay? or Flip a Coin?
    if random == 0:
        random = 1
        switch = 0
    elif random == 1:
        print("Do you want the contestant to switch or stay every time? 1 = switch, 0 = stay.")
        switch = int(input("Enter 0, or 1: " ))
        if switch == 1:
            random = 1
        elif switch == 0:
            random = 0
        else:
            clear(8)
            print("you'll have to choose.")
            clear(2)
            montyhall()
    else:
        clear(8)
        print("you'll have to choose.")
        clear(2)
        montyhall()
    clear(2)
    print("Calculating...")
    #here we determine the count variables and we choose our range of how often the experiment will be repeated.
    #The higher the range, the more accurate our results.
    won = 0
    lost = 0
    for i in range(1000000):
        door = [0, 1, 2]   
        randomwin = randint(0,2) 
        randomchoice = randint(0,2) 
        winner = door[randomwin]#determines the winning door with a randint
        choice = door[randomchoice]# determines the opening contestant choice with a randint
        #print("you have chosen door", door[choice])
        #below, we impliment the logic to simulate our contestant being asked to switch and the resulting decision
        doorToShow = 0
        if (door[doorToShow] == door[winner]) or (door[doorToShow] == door[choice]):
            doorToShow += 1 #this little variable sneakily lets us choose a losing door every time.
        else:
            #print("Gate",door[doorToShow],"is not a winner. Switch chosen gate?")
            if randint(switch, random) == 1:
                door.remove(doorToShow)
                door.remove(choice)
                choice = int(door[0])
                #print("Yes, I will change my choice to gate", choice)
            #else:
                #print("No, I will not change my choice.")        
        if choice == winner:
            won += 1
            #print("you won choosing gate", choice)
            #print("(won", won,"times)")
            #clear()
        else:
            lost += 1
            #print("sorry, the winning gate would have been gate", winner)
            #print("(won", won,"times)")
            #clear()
    print("(won", won,"times)","/", "(lost", lost,"times)")
    print("This result occurs, because the original choice between three doors has a 2/3 probability of ending up as a loss.\nThe Host knowingly removes a losing door after the first choice, so the probability of choosing a losing door changes from 2/3 to 1/3 IF the contestant switches doors.\nInterestingly, the chances shift to a roughly 50% chance of winning or losing,\nif the contestant chooses to base whether they switch or not on chance (say a coin flip.)\nThis is evident with a sample size of one million iterations.")
    clear(2)
    print("Press any key and confirm with 'Enter' to return to Menu.")
    playerInput = input("Input: ")
    if playerInput != "":
        clear(10)
        menu()
    else:
        clear(10)
        menu()
# a method to display a link to the wikipedia page on the monty hall problem. Edumacation!
def whatIsIt():
    print("What is the Monty Hall Problem?\nSince this is a playful educational project, how about reading up on the Monty Hall Problem?\n\n[[https://en.wikipedia.org/wiki/Monty_Hall_problem| wikipedia knows best]] <=Click there!\nPress any Key to return to menu.")
    playerInput = input("Input:")
    if playerInput != "":
        clear(10)
        menu()
    else:
        clear(10)
        menu()
# a method to quit the program
def quitting():
    print("Quitting...")
    sys.exit()
# a method that handles our menu logic
def menu():
    print("--MENU--\nThe Monty Hall Problem\nPress 'P' to Play\nPress 'W' for 'WTF is the Monty Hall Problem??'\nPress 'Q' to Quit.")
    playerInput = input("Input:")
    if playerInput == 'p':
        clear(10)
        print("Starting Game!!!")
        montyhall()
    elif playerInput == 'w':
        clear(10)
        whatIsIt()
    elif playerInput == 'q':
        quitting()
    else:
        clear(3)
        print("no")
        clear(7)
        menu()
# this runs our program
if __name__ == "__main__":
    menu()