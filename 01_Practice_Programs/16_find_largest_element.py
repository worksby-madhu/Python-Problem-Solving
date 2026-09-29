n=int(input("Enter size:"))
a = list(map(int, input("Enter nums:").split()))

#Using max()
print(max(a))

#Using loop
largest=a[0]
for i in a:
    if i>largest:
        largest=i
print(largest)

#Using sort()
a.sort()
print(a[-1])