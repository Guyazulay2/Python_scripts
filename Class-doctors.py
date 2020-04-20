from time import sleep



class doctors:
    def __init__(self, doctor , available , place ):
        self.doctor = doctor
        self.available = available
        self.place = place

    def Schedule(self):
        print("The doctors Schedule is >>: " + str(self.available))
        sleep(1)

    def appointment(self):
        for i in self.available.values():
            while True:
                time = input("Enter the hour you'd like to schedule >>:")
                if time in i:
                    print("Checking...")
                    sleep(0.5)
                    print("-------------------")
                    print("Dear customer, Your appointment is set to >>: " + time)
                    sleep(0.5)
                    print("The Doctor is located at >>: " + str(self.place))
                    break
                else:
                    print("Enter en available hour !")


#################################
Guy = doctors("Eyes", {"Sunday" : [ "8:00" , "9:00" , "11:00" ]}, "Netanya" )
Idan = doctors("Arms", {"Monday": "14:00"}, "Holon")

def Menu():
    while True:
        print("""
******                    *******      
      Welcome To the clinic         
****                         ****
""")
        choose = input("Menu :\n(1) >> Invitation\n(2) >> exit\n Your Choose >>:")
        if choose == "1":
            while True:
                choose2 = input("Enter Which doctor - \n(1) >> idan for eyes\n(2) >> guy for Arms")
                if choose2 == "1" or choose2 == "idan" or choose2 == "IDAN":
                    Idan.Schedule()
                    Idan.appointment()

                elif choose2 == "2" or choose2 == "Guy" or choose2 == "GUY":
                    Guy.Schedule()
                    Guy.appointment()
                else:
                    print("Enter (Guy) or (Idan) only !")

        elif choose == "2":
            print("Thanks and bye (: ")
            break
        else:
            print("Enter 1-2 only !")

Menu()
