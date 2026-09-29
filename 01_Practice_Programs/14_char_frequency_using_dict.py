name="subhadra"
d={}

# Count the frequency of each character
for ch in name:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)