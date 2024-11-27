n = input("Enter Any Name")[0:2].capitalize()
if(n == "Mr"):
    n = n.replace("Mr.","")
    print(n)
elif(n == "Mrs"):
    print("female")


# a = [1, 2, 12.5, 16.8, "Ram", "Shyam"]
# for data in (a):
#   a = type(data)
#   if(a==float):
#    print(data,"belongs=",a)
