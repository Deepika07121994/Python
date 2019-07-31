num = int(input("Enter a number:"))

if num == 1 and num == 0:
    print(num, "is a not prime")

elif num > 1:
    for i in range(2, num):
         if (num % i) == 0:
            print(num, "is not Prime")
            break
    else:
        print(num,"is a prime number")        
else:
    print(num, "is not prime")   

