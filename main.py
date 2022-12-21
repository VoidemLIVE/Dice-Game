# Dice game
# Callum 18/07/22 OCR GCSE Computer Science Python Project

import time
import random


# Variables
loginTries = 0
p1logged = False
p2logged = False
p1user = ''
p2user = ''
p1total = 0
p2total = 0
p1rolls = 0
p2rolls = 0

# Decide whether to log in or register
def decideLogin(p1logged, p2logged, p1user, p2user):
    if p1logged == False or p2logged == False:
        print("Please pick an option:")
        print("1. Register")
        print("2. Login")
        print(" ")
        decision = input("Option: ")
        if decision == "1":
            register()
        elif decision == "2":
            login(loginTries, p1logged, p2logged, p1user, p2user)
        elif decision == "3":
            testingLogin(p1user, p2user)

    else:
        pass

#Register
def register():
    print("Register")
    user = input("Enter a username: ")
    pword = input("Enter a password: ")
    file = open("users.txt", "a")

    if len(pword) <= 4:
        print("Password must be at least 5 characters")
        register()
    elif len(pword) >= 4:
        file.write(user)
        file.write(" ")
        file.write(pword)
        file.write("\n")
        file.close()
        decideLogin(p1logged, p2logged, p1user, p2user)

#Easier login for when testing the program
def testingLogin(p1user, p2user):
    user1 = "TestUser"
    pword1 = "TestPass"
    user2 = "TestUser2"
    pword1 = "TestPass2"
    p1user = user1
    p2user = user2
    start(p1user, p2user)
    return p1user
    return p2user

#Login
def login(loginTries, p1logged, p2logged, p1user, p2user):
    if loginTries == 3:
        print("Too many login attempts. Please try again later")
        exit()
    if p1logged == False:
        print("Player 1 Login")
    else:
        print("Player 2 Login")
    user = input("Username: ")
    pword = input("Password: ")
    print("Loading...")
    time.sleep(1.5)
    for line in open("users.txt", "r").readlines():
        usersfile = line.split()
        if user == usersfile[0] and pword == usersfile[1]:
            print("Welcome!")
            if p1logged == False:
                print("Player 1 Logged in")
                p1logged = True
                p1user = user
                decideLogin(p1logged, p2logged, p1user, p2user)
                return p1user
            else:
                print("Player 2 Logged in")
                p2logged = True
                p2user = user
                start(p1user, p2user)
                return p2user
            return True
    print("Your username/password is incorrect, try again")
    loginTries = loginTries + 1
    login(loginTries, p1logged, p2logged, p1user, p2user)
    return loginTries
    return False

#Player 1 roll
def p1roll(p1user, p1total, p1rolls, p2user, p2rolls, p2total):
    print(p1user + "'s turn")
    print("--------------------------------")
    if p1rolls != 5:
        rolled = input(p1user + ", Type 'roll' to roll the dice: ")
        print("Amount rolled: ", p1rolls)
        if rolled == "roll":
            print("Rolling.")
            time.sleep(0.8)
            print("Rolling..")
            time.sleep(0.8)
            print("Rolling...")
            time.sleep(0.8)
            rolloutput = random.randint(1, 6)
            rolloutput2 = random.randint(1, 6)
            print("You rolled a ", rolloutput)
            print("And a ", rolloutput2)

            p1score = rolloutput + rolloutput2
            if rolloutput == rolloutput2:
                print("Rolled a double, rolling 1 dice again!")
                print("Rolling.")
                time.sleep(0.8)
                print("Rolling..")
                time.sleep(0.8)
                print("Rolling...")
                time.sleep(0.8)
                rolloutput3 = random.randint(1, 6)
                print("You rolled a ", rolloutput3)
                p1score = p1score + rolloutput3

            if p1score % 2 == 0:
                #even
                p1score = p1score + 10
                p1total = p1total + p1score
                print("You rolled an even number so + 10 to your score!")
            else:
                #odd number
                p1score = p1score - 5
                p1total = p1total + p1score
                print("You rolled an odd number so - 5 to your score!")
            if p1score <0:
                p1score = 0
                print("Your score went into minus numbers! It has been set to 0")
            p1total = p1total + p1score
            print(p1user + "'s Total points: ", p1score)
            p1rolls = p1rolls + 1
            p1score = 0
            print("--------------------------------")
            p2roll(p2user, p2total, p2rolls, p1user, p1rolls, p1total)
        else:
            "Please enter 'roll' "
            p1roll(p1user, p1total, p1rolls, p2user, p2rolls)
    else:
        p2roll(p2user, p2total, p2rolls, p1user, p1rolls, p1total)
    return p1total
    return p1rolls


#Player 2 roll
def p2roll(p2user, p2total, p2rolls, p1user, p1rolls, p1total):
    print(p2user + "'s turn")
    print("--------------------------------")
    if p2rolls != 5:
        rolled = input(p2user + ", Type 'roll' to roll the dice: ")
        print("Amount rolled: ", p2rolls)
        if rolled == "roll":
            print("Rolling.")
            time.sleep(0.8)
            print("Rolling..")
            time.sleep(0.8)
            print("Rolling...")
            time.sleep(0.8)
            rolloutput = random.randint(1, 6)
            rolloutput2 = random.randint(1, 6)
            print("You rolled a ", rolloutput)
            print("And a ", rolloutput2)

            p2score = rolloutput + rolloutput2
            if rolloutput == rolloutput2:
                print("Rolled a double, rolling 1 dice again!")
                print("Rolling.")
                time.sleep(0.8)
                print("Rolling..")
                time.sleep(0.8)
                print("Rolling...")
                time.sleep(0.8)
                rolloutput3 = random.randint(1, 6)
                print("You rolled a ", rolloutput3)
                p2score = p2score + rolloutput3

            if p2score % 2 == 0:
                #even
                p2score = p2score + 10
                p2total = p2total + p2score
                print("You rolled an even number so + 10 to your score!")
            else:
                #odd number
                p2score = p2score - 5
                p2total = p2total + p2score
                print("You rolled an odd number so - 5 to your score!")
            if p2score <0:
                p1score = 0
                print("Your score went into minus numbers! It has been set to 0")
            p2total = p2total + p2score
            print(p2user + "'s Total points: ", p2score)
            p2rolls = p2rolls + 1
            p2score = 0
            print("--------------------------------")
            p1roll(p1user, p1total, p1rolls, p2user, p2rolls, p2total)
        else:
            "Please enter 'roll' "
            p2roll(p2user, p2total, p2rolls, p1user, p1rolls)
    elif p2rolls == 5:
        stats(p1user, p2user, p1total, p2total)
    return p2total
    return p2rolls

# Runs after both players logged in
def start(p1user, p2user):
    print("Player 1: ", p1user)
    print("Player 2: ", p2user)
    p1roll(p1user, p1total, p1rolls, p2user, p2rolls, p2total)

#Runs after the game finishes
def stats(p1user, p2user, p1total, p2total):

    winner = ''

    if p1total > p2total:
        winner = p1user
    elif p2total > p1total:
        winner = p2user
    elif p1total == p2total:
        winner = "It was a draw"
    print("\n" * 3)
    print("--------------------------------")
    print("   _____ _        _       ")
    print("  / ____| |      | |      ")
    print(" | (___ | |_ __ _| |_ ___ ")
    print("  \___ \| __/ _` | __/ __|")
    print("  ____) | || (_| | |_\__ \ ")
    print(" |_____/ \__\__,_|\__|___/")
    print("--------------------------------")
    print("WINNER:")
    print(winner)
    print("--------------------------------")
    print( p1user," total: ", str(p1total))
    print( p2user," total: ", str(p2total))
    pass

decideLogin(p1logged, p2logged, p1user, p2user)
