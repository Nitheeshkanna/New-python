print("_________________________________________________________________________________________________________")
print()
print("HAVE A NICE DAY AHEADE")
print()
print("\t\"AN APPLE A DAY KEEPS THE DOCTOR AWAY\"")
print()
from tqdm import tqdm
import time
n=100
for i in tqdm (range (n),desc="Loading…"):
    time.sleep(0.10)
print()
print("!! WELCOME TO  OUR WEBSITE !!") 
print()
print(" \t -->\"BIG BAZAAR SHOP\"<--")
print()
print("\tPONGAL SALE '20%' Offer...!!!")
print()
tot=[]
c=0
print("PRODUCT LIST: ")
print()
m=[" 1=Milk , 2=Egg , 3=Fish , 4=Chicken , 5=Bread , 6=Sugar , 7=Iodized Salt , 8=DryChilli ,"]
n=["9=RockSalt , 10=Butter , 11=Laptop , 12= Iphone 14 pro max"]
print(m)
print(n)
print()
print("-->Just Click a Number to Buy Your Product <--")
print()
while c <=3:
    m={"1":["Milk",10],"2":["Egg",3],"3":["Fish",60],"4":["Chicken",150],"5":["Bread",40],"6":["Sugar",20],"7":["Iodized Salt",50],
       "8":["DryChilli",30],"9":["RockSalt",30],"10":["Butter",51],"11":["Laptop",20000],"12":["Iphone 14 pro max",1400000]}
    a=input("Enter your product no is mention above :")
    k=0
    if a in m:
      print()
      print(m[a][0]," is available")
      print()
      print(m[a][0],"price=",m[a][1])
      print()
      q=int(input("Enter a quantity :"))
      print()
      #print(m[a][0],"x",q,"=",q*m[a][1])
      print("Your Bill is=",q*m[a][1])
      tot.append(q*m[a][1])
      
      for i in tot:
        k=k+i
    else:
        print("Sorry Sir/Mam your product is Not Available ")
        print()
        print("Please Select Any Other Iteam You Want")
        c=c+1
    m=input("Do you Want Continue Your Purchase:y/n:")
    print()
    if  m=='y' or m=='Y':
          continue
    else:
        p=50
        for i in tqdm (range (p),desc="Loading…"):
            time.sleep(0.01)
        print()
        print("\t--- Total Bill is :",k,"---")
        print()
        j=(20/100)*k
        print("\t$$ -Discount Bill :",k-j," -$$")
        print()
        print("\t\"FOOD IS A MEDICINE, BUT IT NEED A QUANTITY\"")
        print()
        break
print("\t** THANK YOU FOR VISITING OUR SHOP ** ")
print("--------------------------------------------------------------------------------------------------------------")
print("\t** PLEASE FILL YOUR DETAILS FOR MEMBERSHIP **")
print("--------------------------------------------------------------------------------------------------------------")

w=input("Do you Want Create \"BIG BAZAAR\" MemberShip Account:y/n:")
print()
if w=='y' or w=='Y':
    n= int(input("Enter a no of Account want to create:"))
    for i in range(n):
        print()
        n=input("Enter a name:")
        print()
        a=input("Enter your Address:")
        print()
        ph=int(input("Enter a Phone no:"))
        print()
        print(" ** THANK YOU FOR CREATING MEMBERSHIP ACCOUNT ** ")
        print()
        p=100
        for i in tqdm (range (p),desc="Loading…"):
            time.sleep(0.01)
        print()
        print("\t-->This is your \"BIG BAZAAR\""," ","No:","\'*",ph,"002*\'<--",sep="")
        print()
        print(" From your next \"BIG BAZAAR\" purchase point added on your Membership Card ")
        print(" \t \t ********** ")
        print("\t #Thank You ","Mr/Ms/Mrs.",n,"#",sep="")
        print()
        print("\t \t #Welcome...#")
        print()
        print(" \"INSPIRATION DOES EXIST,BUT IT MUST FIND YOU WORKING \"")
        print("_________________________________________________________________________________________________________")
else:
    print()
    print("--> From your next \"BIG BAZAAR\" purchase point added on your Membership Card <--")
    print(" \t \t********** ")
    print()
    print("\t # THANK YOU ","Mr/Ms/Mrs","#")
    print()
    print("\t \t #WELCOME AGAIN.....#")
    print()
    print(" \"INSPIRATION DOES EXIST,BUT IT MUST FIND YOU WORKING\" ")
    print("_________________________________________________________________________________________________________")