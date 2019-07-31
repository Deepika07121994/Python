num1 = int(input("Enter num1:"))

num2 = int(input("Enter num2:"))

for i in range(num1, num2+1):

    if num1 > 1:

        for j in range(2, i):
             if (i % j) == 0:
                 break
        else:
            print(i)    