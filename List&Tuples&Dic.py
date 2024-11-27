# list1 = ["Ram","Shyam",123,12345]
# for i in range(len(list1)-1,-1,-1):
# print(list1[i])
# list2 = [1,2,4,3,6,8]
# for data in list2:
#     if(data %2==0):
#          print(data)
# import pyttsx3
import pyttsx3

# a = [1, 2, 12.5, 16.8, "Ram", "Shyam"]
# for data in (a):
#   a = type(data)
#   if(a==str):
#     print(data,"belongs=",a)


# a = []
# n_choice = input("What you want to do:"
#           "\n 1.insert"
#           "\n 2.append"
#           "\n 3.extend"
#           "\n 4.remove"
#           "\n 5.copy"
#           "\n 6.replace")
#
# if n_choice == '1':
#     x = input("Data")
#     a.insert(x)
#     print(a)
#
# if n_choice == '2':
#     y = input("Data")
#     a.append(y)
#     print(a)
#
# if n_choice == '3':
#     z = input("Data")
#     a.extend(z)
#     print(a)
#
# if n_choice == '4':
#     b = input("Data")
#     a.remove(b)
#     if(a==''):
#         print("Nothing to Remove")
#     else:
#         print(a)
#
# if n_choice == '5':
#     m = ["Data"]
#     a.copy(m)
#     print(a)

# a = ["Ram", "Vijay", "Ramesh", "Sakshi", "nayan"]
# for data in a[::-1]:
#     print(data[::-1])


#...........TUPLES...................
# a=(1,2,3,4,5,2,6,2,7,2,8,2,9,2,10)
# print(a)
# print(type(a))
# for i in range(len(a)):
#     print(a[i])
# for data in a:
#     print(a.count(2))
#     count = 0
# for i in range(len(a)):
#     if(a[i]==2):
#         print("found at",i+1)
#         count +=1
#         pyttsx3.speak(f"2 Found at {i+1}")
# print(count,"Times Found")

# a = []
# n = int(input("How many element you list"))
# count = 0
# for i in range(n):
#     a.append(int(input("Enter Data")))
# a = tuple(a)
# print(a)
# print(type(a))

#.....................SET..................

# a={1,2,3,0,-1,2,3,4,17,19,20,3,5,500,1200,3000}
# print(a)
# print(type(a))
#repetation is not allowed in type of set

# A = {1,2,3,4,5}
# B = {3,4,5,6,7}
# print(A.union(B))
# print(A | B)
# print(A.intersection(B))
# print(A&B)
# print(A.difference(B))
# print(A-B)
# print(A.symmetric_difference(B))
# print(A.union(B)-A.intersection(B))
# print((A-B).union(B-A))

# a =[1,2,3,1,2,3,1,2,3,1]
# b = list(set(a))
# for data in b:
#     print(f"{data} found {a.count(data)}times")

# from num2words import num2words
#
# a = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1,12,17,25,31]
# b = list(set(a))
#
# for data in b:
#     word = num2words(data)  # Convert number to words
#     count_word = num2words(a.count(data))  # Convert count to words
#     print(f"{word} found {count_word} times")

#........................DICTIONANRY...........................

# dict={"Director":"Mr.Vivek","CEO":"Mr.Sourabh","Manage":"MR.Vishal"}
# for data in dict:
#     print(data ,"is" , dict[data])


# ans =[]
# for j in range(1,1001):
#     n=j
#     count = 0
#     for i in range(1,n+1):
#         if(n%i==0):
#             count=count+1
#         if(count==2):
#          ans.append(n)
#
# n = int(input("Enter Number Near by Prime:"))
# ans.append(n)
# ans.sort()
# x = ans.index(n)
# print(ans[x-1],ans[x+1])
#
#
# ans=[]
# for j in range(1,10001):
#     n=j
#     sum=0
#     for i in range(1,n):
#         if(n%i==0):
#             sum=sum+i
#         if(sum==n):
#             ans.append(n)
# print(ans)


# n = int(input("Enter Any Number:"))
# sum = 0
# for i in range(1,n):
#     if(n%i==0):
#         sum=sum+i
#     if(sum==n):
#         print("Yes Perfect")
#     else:
#         print("Not Perfect")

# n = int(input("Enter Any Number: "))
# prime_numbers = []
#
# for num in range(2, n + 1):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime_numbers.append(num)
#
# print("Prime Numbers List:", prime_numbers)
