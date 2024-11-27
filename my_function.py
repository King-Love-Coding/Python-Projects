# def swap(a,b):
#     return(b,a)
# a,b=int(input("Enter First : ")), int(input("Enter Second : "))
# a,b=swap(a,b)
# print(a,b)

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#          fact = fact*i             #Short hand operator
#     return(fact)
# n = int(input("Enter Any Number:"))
# ans = factorial(n)
# print(ans)

# def prime(n):
#     count =0
#     for i in range(1,n+1):
#         if(n%i==0):
#             count = count+1
#     if(count==2):
#         print("prime number")
#     else:
#         print("Not Prime")
# n = int(input("Enter Any Value"))
# prime(n)

# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = 1/fact*i
#     return (fact)
# n = int(input("Enter any number:"))
# ans = fact(n)
# print(ans)

# def swap(a):
#     a[0],a[1]=a[1],a[0]
#     print(a)
# a=[10,20]
# swap(a)
# print(a)


# def show(x="Good Morning"):
#     print(x)
#
# show()
# show("Good Night")
# show("Good Afternoon")
# show()


# def show(name,total):
#     print("name is ",name)
#     print("total is ",total)
#
# show("ram",100)
# show(total=150,name="raj")



def min(*n):
    min = n[0]
    for i in range(len(n)):
        if(min>n[i]):
            min = n[i]
    print("minimum element is",min)

def max(*n):
    max = n[0]
    for i in range(len(n)):
        if (max < n[i]):
            max = n[i]
    print("maximum element is",max)

min(20,15,60,10,30,45)
max(40,60,80,100,20,10)