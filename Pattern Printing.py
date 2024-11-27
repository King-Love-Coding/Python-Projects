# for i in range(1,6):
#     print("*"*5)

# k = 1
# for i in range(1,5):
#     for j in range(1,7):
#         print(k,end="")
#         k = k+1
#         if(k==10):
#             k = 0
#     print("")

for i in range(1,6):
    for j in range(1,6):
        if((i==3 or j==3)or (i==1 and j>=3) or (j==5 and i>=3) or(i==5 and j<=3) or (i<=3 and j==1)):
              print(" * ",end="")
        else:
            print("•", end="")

    print("")
