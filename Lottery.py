###### Simple lottery ######
import random
from time import sleep
print("""
           ********* Welcome to our lottery *********

""")

lotterynumbers = []
for i in range (0, 6):
    number = random.randint(1,30)
    while number in lotterynumbers:
        number = random.randint(1,30)
    lotterynumbers.append(number)
lotterynumbers.sort()

usernum = []
for i in range (0, 6):
    number = int(input("Enter a number between 1 to 30 >>:"))
    while number<1 or number>30:
        number = int(input("Try again !!\n Enter only number between 1 to 30 >>:"))
    usernum.append(number)
usernum.sort()
print("Today The lottery numbers are >>: ")
sleep(1)
print(lotterynumbers)
print("Your numbers >>:")
sleep(1)
print(usernum)

if usernum in lotterynumbers:
    print("Congratulation ! You won !")
else:
    print("Sry but You lose !", "Thanks for playing!")
