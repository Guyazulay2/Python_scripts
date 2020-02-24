import random
from time import sleep
import datetime


################### Main Menu #########################
def menu():
    form=[]
    cost=0
    double=0
    while 1:
        choice=input("Lottery Menu :\n1)Manually Add rows.\n2)Automatically Add rows.\n3)Check winnings.\n4.Enter the Double Lottery enrollmen.\nEnter 1-4  :")
        if choice == "1":
            rows=int(input("How manny rows would you like to manually add to your form?"))
            while rows < 1 :
                rows=int(input("Invalid Input, please enter how many rows again."))
            fill_form(form,rows,0)
            cost=cost+rows*3
            print("Your form: ")
            print_form(form)

        elif choice == "2":
            rows=int(input("How manny rows would you like to automatically add to your form?"))
            while rows < 1 :
                rows=int(input("Invalid Input, please enter how many rows again."))
            fill_form(form,rows,1)
            print("Your form: ")
            print_form(form)
            cost=cost+rows*3

        elif choice == "3":
            if double == 1:
                cost=cost*2
            print("Your form: ")
            print_form(form)
            approval=input("Form total cost is " + str(cost) + " Shekels, Please approve purchase:(yes/no)")
            if approval == "yes":
                winning_list=auto_fill()
                print("The winning numbers are: " + str(winning_list))
                won=prize(winning_list,form,double)
                if won == 0:
                    print("Sorry, you haven't won this time.")
                else:
                    print("Congratulations! You've won a tottal sum of: " + str(won) + " Shmekels!")
            break
        elif choice == "4":
            print("You've entered the Double Lottery enrollemnt.")
            double=1

################## Fills the form  #########################
def fill_form(form,rows,auto):
    for i in range(rows):
        if auto == 0:
            print("Manually adding row number:" + str(i+1))
            form.append(manual_fill())
        else:
            print("Automatically adding row number:" + str(i+1))
            form.append(auto_fill())
    return form
######################### Automatly fill 1 row  #########################
def auto_fill():
    row=[]
    for i in range(6):
        new = (random.randrange(1, 38, 1))
        while new in row:
            new = (random.randrange(1, 38, 1))
        row.append(new)
    return row
########################## Manually fill 1 row ############################
def manual_fill():
    row=[]
    for i in range(6):
        num=int(input("please enter number: "))
        while (num in row) or num < 1 or num >37:
            num = int(input("Invalid input, Please enter a NEW number between 1 and 37: "))
        row.append(num)
    return row
######################### Prize #########################
def prize(win_list,form,double):
    money=0
    for i in range (len(form)):
        counter = 0
        for j in range(6):
            if (form[i])[j] in win_list:
                counter=counter+1
        if counter == 6:
            money=money+1000000
        elif counter == 5:
            money=money+5000
        elif counter == 4:
            money = money + 250
        elif counter == 3:
            money=money+10
    if double == 1:
        return money*2
    else:
        return money

def print_form(form):
    for i in range(len(form)):
        print (form[i])

print("\n***Welcome to the Lottery!***")
x = datetime.datetime.now()
print("Year :", x.year)
print("Time :", x.strftime("%R"),"\n------------------------------")
sleep(0.5)
menu()
print("Thanks for playing!")
