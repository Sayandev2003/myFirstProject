phy = int(input("Enter your PHYSICS marks = "))
chem = int(input("Enter your CHEMISTRY marks = "))
bio = int(input("Enter your BIOLOGY marks = "))
maths = int(input("Enter your MATHS marks = "))
com = int(input("Enter your COMPUTER marks = "))
geo = int(input("Enter your GEOGRAPHY marks = "))
hist = int(input("Enter your HISTORY marks = "))
gk = int(input("Enter your GENERAL KNOWLEDGE marks = "))
eng = int(input("Enter your ENGLISH marks = "))

marks = phy + chem + bio + maths + com + geo + hist + gk + eng

print(f"Your Total MARKS is = {marks} out of 900" )

avg_marks = round(marks / 9, 2)

print("Your Average Marks is = ", avg_marks)

if avg_marks >= 90:
    print ("GRADE A+")
elif avg_marks >= 80:
    print("GRADE A")
elif avg_marks >= 70:
    print("GRADE B")
elif avg_marks >= 60:
    print("GRADE C")
elif avg_marks >= 50:
    print("GRADE D")
elif avg_marks >= 40:
    print("GRADE E")
else:
    print("FAILED")