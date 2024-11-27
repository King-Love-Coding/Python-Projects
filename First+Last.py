a = int(input("Enter Five Digit Number:"))
b = int(a / 10000)
d = int (a // 1000)%10
c = int(a % 10)
e= int(a//10)%10
sum = b + d + c + e
print("Addition of First and Last Number is:", sum)