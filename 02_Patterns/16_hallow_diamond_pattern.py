n = int(input("Enter size:"))

# Upper half
for i in range(n):
    spaces = n - i - 1

    if i == 0:
        print(" " * spaces + "*")
    else:
        print(" " * spaces + "*" + " " * (2 * i - 1) + "*")

# Lower half
for i in range(n - 1, -1, -1):
    spaces = n - i - 1

    if i == 0:
        print(" " * spaces + "*")
    else:
        print(" " * spaces + "*" + " " * (2 * i - 1) + "*")