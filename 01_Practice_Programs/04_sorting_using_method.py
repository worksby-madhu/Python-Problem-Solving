l=list(map(int,input("Enter numbers:").split()))

l.sort()  # Sort the list in ascending order
print(l)

print(l.sort())  #Returns None sort() changes the original list instead of returning a new list
