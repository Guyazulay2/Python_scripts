import random
from time import sleep
import datetime

x = datetime.datetime.now()
print("Year : ",x.year)
print("Time : ",x.strftime("%R"))
sleep(0.5)

def Convert():
    print("Press (1) Shekels to USD\nPress (2) USD to Shekels\nPress (3) Shekels to Euro\nPress (4) Euro to Shekels\nPress (5) Euro to USD\nPress (6) USD to Euro")
    number=(input("Enter 1 - 6 :"))
    if number == "1":
        a = int(input("How many Shekels? :"))
        sleep(0.5)
        print("You got :",a/3.42,"USD")
    if number == "2":
        b = int(input("How many USD? :"))
        sleep(0.5)
        print("You got :",b*3.42,"Shekels")
    if number == "3":
        c = int(input("How many Shekels? :"))
        sleep(0.5)
        print("You got :",c/3.71,"Euro")
    if number == "4":
        d = int(input("How many Euro? :"))
        sleep(0.5)
        print("You got :",d*3.71,"Shekels")
    if number == "5":
        e = int(input("How many Euro? :"))
        sleep(0.5)
        print("You got :",e/0.92,"USD")
    if number == "6":
        e = int(input("How many USD? :"))
        sleep(0.5)
        print("You got :",e*0.92,"Euro")
##############
def Cubes():
    prize = 0
    for i in range(1,10):
        cube1=random.randint(1,6)
        cube2=random.randint(1,6)
        print("First Cube >>: " + str(cube1) + "\nSecond Cube >>: " + str(cube2) + "\n")
        sleep(1)
        if cube1 == cube2:
            if cube1 == 6:
                prize=prize + 1000
                print("in the " + str(i) + " time you won 1000$")
            else:
                prize=prize + 100
                print("in the " + str(i) + " time you won 100$")
        elif cube1 == 1 or cube2 == 1:
            prize=prize + 10
            print("in the " + str(i) + " time you won 10$")
            sleep(1)
        elif cube1 == 2 or cube2 == 2:
            print("in the " + str(i) + " time you won 5$")
            prize=prize + 5
        else:
            print("in the " + str(i) + " time you won 0$\nTry next time...\n")
            sleep(2)
        print("Total Money >>:", prize)
    print("You won : ", prize , "Dollar ")

###############

def Guess():
    print('You need to guess a number from 1 to 6 >>')
    numbers = list(range(1,6))
    guess = input("Enter 1 until 6: ")
    guess = guess.split()
    guess = [int(d)for d in guess]
    guess.sort()

    result = random.sample(numbers, 1)
    result.sort()
    print("result: ",result)
    if result == guess:
        print(">> You win 100,000 Dollar << ")
    else:
        print("*** You lose *** ")

        numbers = list(range(1, 6))
        guess = input("We giving you another chance to win, Enter 2 numbers until 6 : ")
        guess = guess.split()
        guess = [int(d) for d in guess]
        guess.sort()

        result = random.sample(numbers, 2)
        result.sort()
        sleep(2)
        print("result: ", result)
    if result == guess:
        print("You win!! ")
    else:
        sleep(2)
        print("*** You lose, Try next time (: *** ")

###############

def menu():
    while True:
        print("""
        ******        ******
        **** Casino Menu ****
        ******        ******
          """)
        print("(1) >> Money conversion\n(2) >> Throw a cubes\n(3) >> Guess a number\n(4) >> Exit")
        num=input("Enter 1 To 4 >>:\n")
        if num == "1":
            Convert()
        if num == "2":
            Cubes()
        if num == "3":
            Guess()
        if num == "4":
            print("See you next time, bye (:")
            break
        else:
            print("Enter only 1 To 4 !")

menu()
