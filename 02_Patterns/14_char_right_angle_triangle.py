n = int(input("Enter size: "))

for r in range(1, n + 1):
    for c in range(r):
        print(chr(65 + c), end=" ")
    print()