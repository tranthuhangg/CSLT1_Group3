import random
a=0
y=random.randrange(1,100,1)
print(y)
for i in range(1,100,1):
    b=random.randrange(1,100,1)
    if y<b:
        y=b
        a+=1
        print(b,"Update")
    else:
        print(b)
print('The maximum value found was:',y)
print('The maximum value was updated',a,'times')