n = int(input("Enter size: "))

for r in range(n):
    for c in range(n):
        if c <= r:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()