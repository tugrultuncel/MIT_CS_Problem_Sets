"""
Calculates how many unique letters are in a string.
"""
s=input("Enter a string: ")
count=0
seen=""
for char in s:
    if char not in seen:
        seen+=char
        count+=1
print("Number of unique letters:",count)