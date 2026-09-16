def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev
text = input("Enter a string: ")
print("Reversed String:", reverse_string(text))