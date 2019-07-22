a = list(map(int, input().split()))

b = list(map(int, input().split()))

# alist = list()
# blist = list()
addedlist = list()

# alist.append(a)
# blist.append(b)


addedlist = map(lambda x, y: x + y, a, b)
print(list(addedlist))

