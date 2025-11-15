def check(txt):
    for i in range(len(txt)):
        if txt[i] != txt[-i-1]:
            return False

    return True

print(check(input().replace(" ", "").lower()))