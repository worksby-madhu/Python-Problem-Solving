n=int(input("Enter size:"))

# Iterate through rows
for r in range(n):
    
    # Iterate through columns
    for c in range(n):
        
        # Print * on the border of the square
        if r==0 or r==n-1 or c==0 or c==n-1:
            print("*",end=" ")
            
        # Print spaces inside the square
        else:
            print(" ",end=" ")
    print()