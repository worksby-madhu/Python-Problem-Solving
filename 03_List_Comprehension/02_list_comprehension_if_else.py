#print whether the nums are even or odd
l=[1,2,3,4,5,6]

# Check each number and store "even" if it is divisible by 2,
# otherwise store "odd"
r=["even" if x % 2==0 else "odd" for x in l]

print(r)