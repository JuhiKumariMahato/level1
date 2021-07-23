n=int(input("enter the no"))
arm=0
x=n
while(n>0):
    r=n%10
    arm=arm+r**3
    n=n//10
if(arm==x):
    print("the number is an armstrong no")
else:
    print("not an armstrong no")
    

    
      
