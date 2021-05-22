# in this question we are calculate a factorial vaule of any number 



num=int(input("enter a number "))
i=1
while num>0:
    i=i*num
    num=num-1
print("factorial=",i)
