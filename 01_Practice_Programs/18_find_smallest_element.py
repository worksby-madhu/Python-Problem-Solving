n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter numbers: ").split()))

smallest = a[0]

for i in a:
    if i < smallest:
        smallest = i

print("Smallest:", smallest)