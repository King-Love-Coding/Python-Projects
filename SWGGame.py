# import random
# list=["S","W","G"]
# chances = 10
# comp_point = 0
# user_point = 0
# i=1
# while(i<=10):
#     print(f"Game- {i}")
#     comp_choice = random.choice(list)
#     user_choice = input(f"Select Your Choice{list}")
#     if(user_choice==comp_choice):
#         print("ohhhh Tie")
#     elif(comp_choice=="S" and user_choice=="W"):
#         comp_point = comp_point+1
#         print("Computer Wins !!!!")
#     elif(comp_choice=="W" and user_choice=="G"):
#         user_point = user_point+1
#         print("User Wins !!!!")
#     elif (comp_choice == "G" and user_choice == "S"):
#         comp_point = comp_point+ 1
#         print("Computer Wins !!!!")
#
#     elif (comp_choice == "G" and user_choice == "W"):
#         user_point = user_point + 1
#         print("User Wins !!!!")
#
#     elif (comp_choice == "S" and user_choice == "G"):
#         user_point = user_point + 1
#         print("User Wins !!!!")
#
#     elif (comp_choice == "G" and user_choice == "S"):
#         comp_point = comp_point + 1
#         print("Computer Wins !!!!")
#
#     print(f"Competed {i} Remains{10-i}")
#     print(f"user points{user_point} comp_point{comp_point}")
#     i = i+1
#
# if(comp_point==user_point):
#     print("ohooo Draw")
# elif(comp_point>user_point):
#     print(f"Computer Win By{comp_point-user_point}")
# else:
#     print(f"User Wins By{user_point-comp_point}")

from random import choice

list=['S','W','G']
comp_point=0
user_point=0
for i in range(1,6):
    comp_choice=choice(list)
    user_choice=input(f"Select Any One From {list}").upper()
    if(comp_choice==user_choice):
        print("Tie...")
    elif(comp_choice=='S' and user_choice=='W'):
        comp_point+=1
    elif (comp_choice == 'S' and user_choice == 'G'):
        user_point += 1

    elif (comp_choice == 'W' and user_choice == 'G'):
        comp_point += 1
    elif (comp_choice == 'W' and user_choice == 'S'):
        user_point += 1

    elif (comp_choice == 'G' and user_choice == 'S'):
        comp_point += 1
    elif (comp_choice == 'G' and user_choice == 'W'):
        user_point += 1

    print(f"Complete Chances {i} Remains {5-i}")
    print(f"computer Select ={comp_choice} user select {user_choice}")
    print(f"Computer Points= {comp_point} User point ={user_point}")

if(comp_point>user_point):
    print(f"Computer Wins By {comp_point-user_point}")
elif(user_point> comp_point):
    print(f"User Wins By {user_point-comp_point}")
else:
    print("Tie")