s = input("Enter a string: ")
vow = 0
cons = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vow += 1
        else:
            cons += 1

print("Vowels:", vow)
print("Consonants:", cons)