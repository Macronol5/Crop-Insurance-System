#import datetime
#from premium import premiumm
def farmers():
 global ld_amount,typ_crop,name_crop
 name = str(input("Enter your name  "))
 age = int(input("Enter your age  "))
 gender = str(input("enter your gender  "))
 state = str(input("enter your state  "))
 city = str(input("enter your city  "))
 ld_amount= int(input("enter land in hectares "))
 address= str(input("enter your address  "))
 typ_crop = str(input("enter type of crop  "))
 name_crop = str(input("enter name of crop  "))
    #date = datetime(input("enter date of cultivation"))
 from datetime import date, datetime
 year = int(input('Enter a year: '))
 month = int(input('Enter a month: '))
 day = int(input('Enter a day: '))
 d = date(year, month, day)
 print("Successfull registration ")
 print("registration date is ",d)
    #p=premiumm(l_amount,type_crop,name_crop)
    #print("you have to pay premium",p)
 global policy_no
 policy_no= []
 i=0
 policy_no.append(name[0:2]+str(1000+i)+city[0:3])
 i+=1
 print("your policy no is : ",policy_no)
farmers()