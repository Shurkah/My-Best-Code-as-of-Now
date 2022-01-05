fin = open("english.txt", "r", encoding="utf8")

words = []
z = 5

for line in fin:
    line = fin.readline()
    if len(line) > z:
        words.append(line.strip())


def lastz(w):
    last = w[-z:]
    return last


def firstz(w):
    first = w[:z]
    return first


dict1 = {}
for i in words:
    if lastz(i) not in dict1:
        dict1[lastz(i)] = [i]
    else:
        dict1[lastz(i)].append(i)

dict2 = {}
for i in words:
    if firstz(i) not in dict2:
        dict2[firstz(i)] = [i]
    else:
        dict2[firstz(i)].append(i)

for i in dict1:
    if i in dict2:
        for w1 in dict1[i]:
            for w2 in dict2[i]:
                s = w1[:-z] + w2
                if w1 != w2 and s != w1 and s != w2:
                    print(s)

fin.close()
