phy=int(input("physics marks ="))
chem=int(input("chemistry marks = "))
mat=int(input("maths marks ="))
avg =(phy+chem+mat)/3
if avg>=40:
    print("pass")
else:
    print("fail")