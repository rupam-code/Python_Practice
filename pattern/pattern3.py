n = int(input("Enter a number:"))

for i in range (1,n-1):
    for j in range (1,n-1):
        if (j<=8-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
    