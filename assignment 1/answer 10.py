n=int(input("number  = "))
s=""
while n>0:
    if n%2==0:
        s=s+"0"
        n=n//2
    else:
        n=n-1
        s=s+"1"
        n=n//2
print(s[::-1])