n=int(input("Enter size:"))

for r in range(n):
    for c in range(n-r):# Decrease the number of stars in each row
        print("*",end=" ")
    print()