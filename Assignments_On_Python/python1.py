# x = int(input("Please enter an integer: "))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('more')

words = ['Deepika','Sheela','Akshaya']
for e in words:
   if len(e) > 6:
        words.insert(0, e)

# Hourly rate

# hrs = input("Enter Hours:")
# h = float(hrs)
# rs = input("Enter Rate:")
# r = float(rs)
# if h > 40.0 :
#     rp = h * r
#     exp = (h- 40.0) * (r * 0.5)
#     p = rp + exp
# elif h <= 40.0 :
#     	p = h * r

# print("Pay:",p)


# Conditional 

# sc = input("Enter Score: ")
# score = float(sc)

# if score >= 0.0 and score <= 1.0 :
#     if score >= 0.9:
#         print("A")
     
#     elif score >= 0.8:
#         print("B")
        
#     elif score >= 0.7:
#         print("C")
    
#     elif score >= 0.6:
#         print("D")
        
#     elif score < 0.6:
#         print("F")
# else : 
# 	print("out of range!!! error")

# Open file

# lines = open('pythin-testing.txt')

# for line in lines:
#     rds = line.rstrip()
#     print("rds:", rds)
#     wrds = line.split()
#     print("wrds:", wrds)


# fname = input("Enter file name: ")
# fh = open(fname)
# l = list()        
# for line in fh:
#     lst = line.rstrip()
#     wrds = lst.split()
#     for w in wrds:
#         #  if num not in final_list: 
#             # final_list.append(num) 
#         l.append(w)
# l.sort()
# # remove duplicate
# l = list(dict.fromkeys(l))
# print(l)
# class Employee:
#     def __init__(self, name):
#         print("employee called")

# class permanent_Employee(Employee):
#     def __init__(self, name):
#         print("Permanent employee called")

# emp = permanent_Employee("abc")
