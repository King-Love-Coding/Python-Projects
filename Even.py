#  n=int(input("Enter Any Number :"))
# if(n%2):
#     print("ODD")
# else:
#     print("EVEN")

# n=(input("Enter Any Number"))[-1]
# if(n in 2,4,6,8,10):
#     print("ODD")
# else:
#     print("EVEN")

# n=input("Enter Number:")[-1]
# if(n=='0' or n=='2' or n=='4'or n=='6' or n=='8'):
#     print("EVEN")
# else:
#     print("ODD")

start = 1
end = 100
even_number=[]
odd_number=[]
for i in range(start,end):
    if(i%2==0):
        even_number.append(i)
    else:
        odd_number.append(i)
print("Even Numbers:",even_number)
print("Odd Numbers:",odd_number)
