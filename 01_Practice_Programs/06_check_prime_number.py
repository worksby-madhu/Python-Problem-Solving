n=int(input("Enter Number:"))
c=0

#Count factors
for i in range (1,n+1):
    if n%i==0:
        c+=1
#Check prime
if c==2:
    print("Prime number")
else:
    print("Not a Prime number")