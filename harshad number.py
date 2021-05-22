# harshad number :
    # it is take any number and add this two digit number and check the
    #  addition value is divisible bye this two digit number then it is divisible then its harshad 
    # number then it not divisiblr then it not harshad number 
# forEx; 43
#     4+3=7
#     7/43



# num=int(input("enter a number "))
# i=0
# while i<1:
#     a=num%10
#     b=(num//10)%10
#     c=(num//10)//10
#     d=a+b+c
#     i=i+1
#     if num%d==0:
#         print("harshad number")
#     else:
#         print("not harshad number")

i=1
while i<1000:
    a=i%10
    b=(i//10)%10
    c=(i//10)//10
    d=a+b+c
    i=i+1
    if i%d==0:
        print("harshad number",i)
    else:
        print("not harshad number",i)