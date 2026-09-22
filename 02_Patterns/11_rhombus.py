n = int(input("Enter size: "))

for r in range(n):
    # spaces
    for c in range(n - r - 1):
        print(" ", end=" ")

    # stars
    for c in range(2 * r + 1):
        print("*", end=" ")

    print()

for r in range(n - 1):
    # spaces
    for c in range(r + 1):
        print(" ", end=" ")

    for c in range(2 * n - (2 * r + 3)):
        print("*", end=" ")

    print()