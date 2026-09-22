num=1
n=int(input("Enter number of rows:"))
for r in range(n):
    #spaces
    for c in range(r+1):
        print(" ",end=" ")
    #print numbers in reverse pyramid
    for c in range(2*n-(2*r+1)):                    
        print(num,end=" ")
        num+=1
    print()    