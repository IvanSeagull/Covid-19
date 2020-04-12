import COVID19Py
from sys import exit
N=1
print("\n----COVID-19----")
covid19= COVID19Py.COVID19()

latest = covid19.getLatest()

usa = covid19.getLocationByCountryCode("US")
ru = covid19.getLocationByCountryCode("RU")



def AskTocontinue():
    print("\n\nContinue?   y/n")
    que=input()
    if que =="y":
        print("\n\n----------------")
    elif que == "n":
        print("\nWash your hands!")
        exit()

while N!=0:
    print("\nChoose county")
    print("\n1 - global")
    print("2 - USA")
    print("3 - Russia")
    print("0 - Exit")

    x=int(input("\nChoice: "))

    if x==1:
        print("\nGlobal")
        print("Confirmed: " , latest['confirmed'] ,  "\nDeaths: " , latest['deaths'])
        AskTocontinue()
    elif x==2:
        print("\nCounty: USA")
        print("Confirmed: " , usa[0]['latest']['confirmed'] ,  "\nDeaths: " , usa[0]['latest']['deaths'])
        AskTocontinue()
    elif x==3:
        print("\nCounty: Russia")
        print("Confirmed: " , ru[0]['latest']['confirmed'] ,  "\nDeaths: " , ru[0]['latest']['deaths'])
        AskTocontinue()
    elif x==0:
        print("\nWash your hands!")
        exit()