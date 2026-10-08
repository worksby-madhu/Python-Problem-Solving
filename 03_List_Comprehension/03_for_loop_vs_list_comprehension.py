#using loop
r=[]
l=[1,2,3,4,5]
for num in l :
    r.append(num*2)
print(r)

#using list comprehension
r1=[x*2 for x in l]
print(r1)

#multiply cube 
r2=[x**3 for x in l]
print(r2)