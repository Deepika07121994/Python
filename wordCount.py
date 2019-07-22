fileContent = open("wordCountSample.txt")

countDic = dict()

for line in fileContent:
    wds = line.split()
    for w in wds:
        countDic[w] = countDic.get(w, 0) + 1
print(countDic)

max = 0
word1 = None
word2 = None

min = list(countDic.values())[0]
for (k, v) in countDic.items():
   
    if v < min:
        min = v
        word1 = k
    if v > max:
        max = v
        word2 = k
print("Word appearing maximum times:", word2, ";", max, "times")
print("Word appearing minimum times:", word1, ";", min, "times")

