import functools

a = list(map(int, input().split()))


def compare(value):
    if value % 2 == 0:
        return True
    else:
        return False


evenValueList = list()
sqlst = list()
evenValueList = list(filter(compare, a))

print(evenValueList)

addedlist = list(map(lambda x, y: x * y, evenValueList, evenValueList))


print(list(addedlist))

finalSum = functools.reduce(lambda x, y: x + y, addedlist)

print(finalSum)

