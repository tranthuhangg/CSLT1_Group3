n=int(input("Enter the first positive interger:"))
m=int(input("Enter the second positive interger:"))
d=min(m,n)
while m%d != 0 or n%d != 0:
        d=d-1
print("The greatest common divisor of",n,"and",m,"is",d)

