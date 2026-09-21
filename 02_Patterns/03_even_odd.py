even,odd=2,1
for r in range(1,5):
    for c in range(1,5):
        if r%2==0:
            print(odd,end=" ")
            odd+=2
        else:
            print(even,end=" ")
            even+=2
    print()
    