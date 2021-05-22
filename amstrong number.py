# aramstrong number :- number of n digits which are equal to sum of nth power of its digit.
# 153......(number of digit is n)
# n=3    .....1 power is 3 + 5 p0wer is 3 + 3 power is 3 =153....it armstrong number



num=int(input("enter a number "))
sum=0
x=num
while num>0:
    sum=sum+(num%10)*(num%10)*(num%10)
    num=num//10
if sum==x:
    print("it is amstrong number")
else:
    print("it is not amstrong number")