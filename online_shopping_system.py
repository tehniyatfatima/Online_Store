name=input("please enter your name")
print("\t","\t","\t","----------WELCOME"+name+"to Galaxy store--------")

print('hello', name, 'what do you like to purchase from Galaxy store')
#print(x)
print("Available categerries are given bellow","\n","1.laptops","\n","2.Accessories","\n","3.Desktop Computers")
user_ask=int(input("plese enter no of categery"))


class laptop():
    def __init__(self,processor,RAM,laptop_size,prize):
        self.processor=processor
        self.RAM=RAM
        self.laptop_size=laptop_size
        self.prize=prize

    def laptop_details(self):
        print("processor :",self.processor,'\n',"RAM :",self.RAM,"\n","laptop_size :",self.laptop_size,"\n","prize",self.prize)

laptop1=laptop("core i3 3rd generation","2GB","12.5 inches",30000)
laptop2=laptop("core i5 3rd generation","4GB","12.5 inches",35000)
laptop3=laptop("core i5 7th generation","8GB","14 inches",45000)
laptop4=laptop("core i7 9th generation","1TB","15.6 inches",60000)

def l_details():
        print("--------AVAILABLE LAPTOP DETAILS ARE GIVEN BELLOW---------")
        print("\t","first available laptop details are given below")
        laptop1.laptop_details()
        print("\t","second available laptop details are given below")
        laptop2.laptop_details()
        print("\t","Third available laptop details are given below")
        laptop3.laptop_details()
        print("\t","fourth available laptop details are given below")
        laptop4.laptop_details()


class Accessories():
    def __init__(self,name,prize,waranty):
        self.name=name
        self.prize=prize
        self.waranty=waranty

    def Accessores_details(self):
        print("name :",self.name,"\n","prize :",self.prize,"\n","waranty :",self.waranty)

A1=Accessories("hand free","250","6 months")
A2 = Accessories( "USB", "2000", "2 years")
A3 = Accessories( "wire less keyboard", "3000", "1 year")
A4 = Accessories( "data cable", "500", "6 months")

def A_details():
        print("--------AVAILABLE ACCESSORIES DETAILS ARE GIVEN BELLOW---------")
        print("\t", "first  Available Accessories details are given below")
        laptop1.laptop_details()
        print("\t", "second Available Accessories details are given below")
        laptop2.laptop_details()
        print("\t", "Third Available Accessories details are given below")
        laptop3.laptop_details()
        print("\t", "fourth Available Accessories details are given below")
        laptop4.laptop_details()


class Desktop_Computer():
    def __init__(self,condition,prize,waranty):
        self.condition=condition
        self.prize=prize
        self.waranty=waranty

    def DC_details(self):
        print("condition :",self.condition,"\n","prize :",self.prize,"\n","waranty :",self.waranty)

DC1=Desktop_Computer("brand new",25000,"2 years")
DC2=Desktop_Computer("used",15000,"2 years")
DC3=Desktop_Computer("used",15000,"1 years")
DC4=Desktop_Computer("brand new",22000,"2 years")

def D_details():
    print("--------AVAILABLE DESKTOP COMPUTERS DETAILS ARE GIVEN BELLOW---------")
    print("\t", "first  Available desktop computer details are given below")
    DC1.DC_details()
    print("\t", "second Available desktop computer details are given below")
    DC2.DC_details()
    print("\t", "Third Available desktop computer details are given below")
    DC3.DC_details()
    print("\t", "fourth Available desktop computer details are given below")
    DC4.DC_details()

if user_ask==1:
    l_details()

if user_ask==2:
    A_details()

if user_ask==3:
    D_details()


n=input("press enter to close program")









