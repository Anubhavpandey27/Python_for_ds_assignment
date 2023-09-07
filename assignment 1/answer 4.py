l1=[]
n1=int(input(""))
for i in range(0,n1):
    a=int(input(" "))
    l1.append(a)
opt=int(input("1.delete \n 2.Insert"))
if opt==2:
    a=int(input(" index value"))
    b=input("value ")
    l1.insert(a,b)
else:
    op=int(input(" 1.delete by value \n 2. delete by index \n 3.delete range"))
    if(op==1):
        k=input("enter you want to delete")
        l1.remove(k)
    elif op==2:
        k=int(input("enter index"))
        del l1[k]
    else:
        st=int(input("strating index"))
        ed=int(input("ending value"))
        for i in range(st,ed+1):
            del l1[i]


print(l1)