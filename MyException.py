# a = int(input("Enter Number"))
# b = int(input("Enter Number"))
# try:
#     print(a / b)
# except Exception as e:
#     print(e)
# print("my name is ram")

# try:
#     ch1 = int(input("Enter Any Character:"))
# except Exception as e:
#     print(e)

# a,b = int(input("Enter 1st No:")), int(input("Enter 2nd Number:"))
# try:
#     print(a/b)
#     x = int(input('Enter Char :'))
# except ZeroDivisionError as e:
#     print("Pls Dont Enter Zero...",e)
# except ValueError as v:
#     print(v)
# except Exception as Ex:
#     print(Ex)
# finally:
#     print("Inside Finally")

# from time import *
# print(time())
#
# for i in range(1,10001):
#     print("",end="")
#     print(asctime(localtime()))

# from datetime import *
# print(datetime.now())

# from time import *
# start = time()
# for i in range(10):
#     print("",end="")
#     sleep(1)
# end = time()
# print(end-start)

# from time import *
# para = "My name is vivek"
# start = time()
# for i in range(len(para)):
#    print(para[i],end="")
#    sleep(1)
# end = time()
# print(end-start)

list = ["My Name Is Vivek"]
li = list.split(" ")
print(li)