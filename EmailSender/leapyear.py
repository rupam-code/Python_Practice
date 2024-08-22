
print("This is a leap year checker program ")
year = int(input("Enter a year you want to check= "))
def leap(year):
    print("Cheking")
    if ((year%400==0) or (year%4==0 and year%100!=0)):
        print("The year",year,"is leap year")
    else :
        print("The year",year,"is not a leap year")

leap(year)