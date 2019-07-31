
import functools

a = list(map(int, input().split()))

# def add(value):
#     return value + value

sum = functools.reduce(lambda x, y: x+y, a)
print("Sum of list element:", sum)