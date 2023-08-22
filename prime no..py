a=int(input("enter a no."))
if(a==1):
    print("not a prime no.")
if (a>1):
    for i in range(2,a):
        if(a%i==0):
           print("not a prime no.")
           break
    else:
        print("prime no.")