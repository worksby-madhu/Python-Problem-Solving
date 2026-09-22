num=1
n=int(input("Enter number of rows: "))
for r in range(n):
    #spaces
    for c in range(n-r-1):
        print(" ",end=" ")
    #stars
    for c in range(2*r+1):
        print(num,end=" ")
        num+=1
    print()