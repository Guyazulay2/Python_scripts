print("""
   **** WELCOME TO THE HOTEL **** 
""")
print("First enter your details :")
class Guest():
    def __init__(self):
        self.name = ''
        self.id = ''
        self.members = 0
        self.duration = 0

    def Fullname(self):
        self.name = input("Your Full Name >>:")

    def Id(self):
        id = input("Enter your ID >>:")
        self.id = id

    def Members(self):
        p = int(input("Enter how many people are you? >>:"))
        self.members = p

    def Duration(self):
        d = int(input("Enter the duration of your stay in Days >>:"))
        self.duration = d

class Add():
    def __init__(self):
        self.charge = 0

    def Food(self):
        z = int(input("Please Select Your Choice:\n(1)>> Just Breakfast (20 Dollar for each person)\n(2)>> All meals Included (50 Dollar for each person)\n   Your Choice >>:"))
        if z == 1:
            self.charge = self.charge + 20
        else:
            self.charge = self.charge + 50

    def Pool(self):
        self.charge = self.charge + 10

    def CarRental(self):
        dis = int(input("Enter the distance to be covered by the car in Kms (Every mile 5 Dollars !) >>:"))
        self.charge = self.charge + (dis * 5)

class HotelReservation(Add):
    def __init__(self):
        Add.__init__(self)
        self.choice = ''
        self.cost = ''

    def singleRoom(self):
        self.choice = "Single Room"
        self.cost = 700

    def DoubleRoom(self):
        self.choice = "Double Room"
        self.cost = 1500

    def TripleRoom(self):
        self.choice = "Triple Room"
        self.cost = 2500

    def KingRoom(self):
        self.choice = "King Sized Room"
        self.cost = 3500

    def MasterSuite(self):
        self.choice = "Master Suit"
        self.cost = 5000

G = Guest()
G.Fullname()
G.Id()
G.Members()
G.Duration()
y = G.members
g = G.duration
while True:
    x = int(input("Please Select Your Type of Room :\n(1)>> Single Room\n(2)>> Double Room\n(3)>> Triple Room\n(4)>> King Room\n(5)>> Master Suite\n   Your Choice >>:"))
    Reserve = HotelReservation()
    if x == 1:
        if y != 1:
            print("This room is for one person only !")
            continue
        else:
            Reserve.singleRoom()
            break
    elif x == 2:
        if y > 2:
            print("This room is for two people only !")
            continue
        else:
            Reserve.DoubleRoom()
            break

    elif x == 3:
        if y > 3:
            print("This room is for three people only!")
        else:
            Reserve.TripleRoom()
            break

    elif x == 4:
        Reserve.KingRoom()
        break

    elif x == 5:
        Reserve.MasterSuite()
        break

    else:
        print("*** Wrong Choice ***")
        continue


z = input('Want to add something more? Example :[Food, Pool, Car]  Enter y/n >>:')
if z == "y" or z == "yes" or z == "YES":
    choose = int(input("PLease Select \n(1)>> Food\n(2)>> Pool (10 Dollar for each person)\n(3)>> Car Rental \n   Your Choice >>:"))
    if choose == 1 or choose == "Food" or choose == "FOOD":
        Reserve.Food()
    elif choose == 2 or choose == "Pool" or choose == "POOL":
        Reserve.Pool()
    elif choose == 3 or choose == "Car" or choose == "CAR":
        Reserve.CarRental()
    else:
        print("Enter 1 to 3 only ! ")

elif z == "N" or z == "no" or z == "NO":
    print("Bye Bye")
else:
    print("Enter only Yes/No !")


total = (Reserve.charge + Reserve.cost)*g
print("The Total Bill Amount is : {}".format(total), "Dollar.")
