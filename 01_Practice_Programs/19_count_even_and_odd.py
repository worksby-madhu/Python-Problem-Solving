n = int(input("Enter number of elements: "))
a = list(map(int, input("Enter numbers: ").split()))

even = 0
odd = 0

for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)