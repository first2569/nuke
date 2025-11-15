words = input().lower().split()
counter = []

for word in words:
    for i, count in enumerate(counter):
        if word == count[0]:
            counter[i][1] +=1
            continue
    counter.append([word, 1])
    

print(counter)