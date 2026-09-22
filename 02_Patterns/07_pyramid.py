n=int(input("Enter number of rows: "))

for r in range(n):
    #spaces
    for c in range(n-r):
        print(" ",end=" ")
    #stars
    for c in range(2*r+1):
        print("*",end=" ")
    print()