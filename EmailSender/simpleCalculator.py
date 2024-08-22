# define the function needed :add,sub,mul,div
def add(a,b):
    answer = a+b
    print(str(a)+"+"+str(b)+"="+str(answer)+"\n")

def sub(a,b):
    answer = a-b
    print(str(a)+"-"+str(b)+"="+str(answer)+"\n")

def mul(a,b):
    answer = a*b
    print(str(a)+"*"+str(b)+"="+str(answer)+"\n")

def div(a,b):
    answer = a/b
    print(str(a)+"/"+str(b)+"="+str(answer)+"\n")
while True:

 print("A-> Addition")
 print("B-> Substraction")
 print("C-> Multipication")
 print("D-> Division")
 print("E-> Exit")

 choice = input("Input your choice::")

 if (choice=="a" or choice=="A"):
     print("ADDTION")
     a = int(input("ENter frist Number::"))
     b = int(input("Enter second NUmber::"))
     add(a,b)
 elif(choice=="b" or choice=="B"):
     print("SUBSTRATION")
     a = int(input("ENter frist Number::"))
     b = int(input("Enter second NUmber::"))
     sub(a,b)
 elif(choice=="c" or choice=="C"):
     print("Multipication")
     a = int(input("ENter frist Number::"))
     b = int(input("Enter second NUmber::"))
     mul(a,b)
 elif(choice=="d" or choice=="D"):
     print("DIVISION")
     a = int(input("ENter frist Number::"))
     b = int(input("Enter second NUmber::"))
     div(a,b)
 elif(choice=="e" or choice=="E"):
     print("Program is Ended")
     quit()