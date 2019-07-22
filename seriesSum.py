# input value from user
num = int(input("Enter a Number:"))

# Initialize sum value to zero
sum = 0

# range(1, num=4) will be - 1,2,3
for i in range(1, num + 1):
    sum = sum  +  (1/i)
    
print("sum of series:", sum)   
