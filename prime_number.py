n=int(input())
for i in range(2,n//2): #we can check the number by 2 for better optimization,
    if n%i==0:
        print("not prime number")
        break
else:
    print("prime number")
