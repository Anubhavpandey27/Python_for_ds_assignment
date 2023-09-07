l1=[]
n1=int(input("l1 size"))
l2=[]
n2=int(input("l2 size"))
for i in range(0,n1):
    a=int(input(""))
    l1.append((a))
for i in range(0,n2):
    a=int(input(""))
    l2.append((a))
for i in range(0,n2):
    a=l2[i]
    l1.append((a))
print(l1)