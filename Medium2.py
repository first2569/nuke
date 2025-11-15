string = input()
longestword = ""
buffer = ""
longestlength = 0
length = 0

for char in string:
    if char != " ":
        buffer += char
        length += 1
    else:
        if length > longestlength :
            longestword = buffer
        longestlength = length
        buffer = ""
        length = 0

print(longestword)