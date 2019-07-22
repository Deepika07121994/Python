# input no. of row and column
rowAndColumn = list(map(int, input().split()))
#  reading array
c = list()
for i in range(0, rowAndColumn[0]):
    print("value of index: ", i)
    a = list(map(int, input().split()))
    print(a)
    c.append(a)
print(c)

 
print("element with maximum value in the entire array:",max(max(x) for x in c))

print("element with minimum value in the entire array:",min(min(x) for x in c))

rminlst = list()
rmaxlst = list()

for x in c:
    rminlst.append(min(x))
    rmaxlst.append(max(x))

print("elements with minimum values row-wise:", rminlst)
print("elements with maximum values row-wise:", rmaxlst)
cminlst = list()
cmaxlst = list()

for each in range(0, rowAndColumn[1]):
    clist = list()
    for m in c:
        clist.append(m[each])
    cmaxlst.append(max(clist))
    cminlst.append(min(clist))

print("elements with minimum values column-wise:", cminlst)
print("elements with maximum values column-wise: ", cmaxlst)   
