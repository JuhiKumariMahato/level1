n=int(input("enter the no."))
rev=0
x=n
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(x==rev):
    print("the no is pallindrome")
else:
    print("not a pallindrome no")
    

