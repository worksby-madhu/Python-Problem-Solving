l=list(map(int,input("Enter numbers:").split()))
# Initialize the three largest numbers
first=second=third=float('-inf')

# Find the top 3 largest numbers
for num in l:
    
    if num>first:
        third=second
        second=first
        first=num  # Update the largest numbers
        
    elif num>second and num<first:
        third=second=num  # Update second largest
        
    elif num>third and num<second and num<first:
        third=num  # Update third largest

print("First largest num:", first)
print("Second largest num:", second)
print("Third largest num:", third)