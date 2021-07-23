n=int(input("enter the number"))
rev=0
x=n
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
print("the reverse number is",rev)
