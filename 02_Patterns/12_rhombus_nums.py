num=1
n=3
for r in range(n):
    #spaces
    for c in range(n-r-1):
        print(" ",end=" ")
    #stars
    for c in range(2*r+1):
        print(num,end=" ")
        num+=1
    print()
n=2
for r in range(n):
    #spaces
    for c in range(r+1):
        print(" ",end=" ")
    for c in range(2*n-(2*r+1)):                    
        print(num,end=" ")
        num+=1
    print()    