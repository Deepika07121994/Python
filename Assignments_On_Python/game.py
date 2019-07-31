def common_element(cricket, Football, Badminton):
    set1 = set(cricket)
    set2 = set(Football)
    set3 = set(Badminton)

    s1 = set1.intersection(set2)
    nameInAll = s1.intersection(set3)
    commonlst = list(nameInAll)
    print("List those players who play all three games:", commonlst)


cricket = ["PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football = ["PKM", "ALN", "RMZ", "CS", "MCS"]
Badminton = ["PKM", "ALN", "NV", "KM", "RMV"]
common_element(cricket, Football, Badminton)

cricketDic = dict()
footballDic = dict()
badmintonDic = dict()


nameInOne = list()
def uniquePlayer(arr1, arr2, arr3):
    
    for c in cricket:
        cricketDic[c] = 1
    for f in Football:
        footballDic[f] = 1
    for b in Badminton:
        badmintonDic[b] = 1

    for (k, v) in cricketDic.items():
         if k not in Football and k not in Badminton:
            nameInOne.append(k)

    for (k, v) in footballDic.items():
        if k not in cricket and k not in Badminton:
            nameInOne.append(k)

    for (k, v) in badmintonDic.items():
        if k not in Football and k not in cricket:
            nameInOne.append(k)
    print("List those players who play exactly one game:", nameInOne)

uniquePlayer(cricket, Football, Badminton);
