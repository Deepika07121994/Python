sequence = input("Enter String:")

def compare(value):
    print(value)
    vowels = ["a", "e", "i", "o", "u"]

    if value in vowels:
        return True
    else:
        return False    
    
    
filterValues = filter(compare, sequence)
lst = list()
for s in filterValues:
    lst.append(s)
    
print("Vowels in input string:",lst)
print("Total Vowels Count:",len(lst))
