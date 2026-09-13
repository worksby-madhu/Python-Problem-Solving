l=list(map(int,input("Enter numbers:").split()))
rev=[]

for num in l:
    rev=[num]+rev  #List concatenation
print(rev)    