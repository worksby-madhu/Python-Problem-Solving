nums = list(map(int, input("Enter numbers: ").split()))
for n in nums:
    c = 0
    # Count factors
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    # Check prime
    if c == 2:
        print(n, "is Prime")
    else:
        print(n, "is Not Prime")