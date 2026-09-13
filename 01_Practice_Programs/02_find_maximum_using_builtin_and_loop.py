nums=list(map(int, input("Enter numbers: ").split()))

#Using Built-in function max()
print(max(nums))

#Using loop
maximum=float('-inf')

for i in nums:
    if i>maximum:
        maximum=i
        
print("Maximum value is:",maximum)