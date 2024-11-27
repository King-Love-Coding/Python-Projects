import random
import string
s1 = list(string.ascii_uppercase)
random.shuffle(s1)
s1 = s1[:3]
# print(s1)
s2 = list(string.ascii_lowercase)
random.shuffle(s2)
s2 = s2[:3]
# print(s2)
s3 = list(string.digits)
random.shuffle(s3)
s3 = s3[:2]
# print(s3)
s4 = list(string.punctuation)
random.shuffle(s3)
s4 = s4[:2]
ans = []
ans.extend(s1)
ans.extend(s2)
ans.extend(s3)
ans.extend(s4)
# print(ans)
n = int(input("Enter how many digit password require "))
if(n<8):
    print("Weak Password")
else:
    # print(ans[:n])
    print("".join(ans[:n]))

