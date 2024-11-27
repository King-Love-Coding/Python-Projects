
from random import *
Balls = ["Red", "Green", "Blue"]
Ques = Balls
FB = choice(Balls)
Balls.remove(FB)
SB = choice(Balls)
Balls.remove(SB)
TB = choice(Balls)
print(FB)
print(SB)
print(TB)
comp_ques = choice(Ques)
n = int(input(f"In Which Glass Have{comp_ques}Ball"))
if(n==1):
  if(FB==comp_ques):
    print("You Win")
  else:
    print(f"{comp_ques}Ball Not In {n}")

elif(n==2):
  if(SB==comp_ques):
    print("You Win")
  else:
    print(f"{comp_ques}Ball Not In {n}")

elif(n==3):
  if(TB==comp_ques):
    print("You Win")
  else:
    print(f"{comp_ques}Ball Not In {n}")


