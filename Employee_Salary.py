a = int(input("Enter Salary:"))
da = int(a * 12/100)
ta = int(a * 14/100)
hra = int(a * 10/100)
pf = int(a * 6/100)
lic = int(a * 5/100)
a = a+da+ta+hra-pf-lic
print("Salary",a)
