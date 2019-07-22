fileContent = open("uniqueWordSample.txt")

countDic = dict()

for line in fileContent:
    
    wds = line.split()

    for w in wds:
        countDic[w] = countDic.get(w, 0) + 1

# print(countDic)
uniqueLst = list()

for (k,v) in countDic.items():
    if v == 1:
        uniqueLst.append(k)
    print(k,":",v,"times")    

print("Number of unique words:",len(uniqueLst))
print("Unique words:",uniqueLst)