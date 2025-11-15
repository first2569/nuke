vowels = 0
for char in input():
    if char.lower() in "aeiou":
        vowels += 1

print(vowels)