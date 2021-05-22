# Ek loop banao jo user se 10 numbers ko input le. 
# Input lene ke baad unn saare numbers ka sum print kare. 
# Yeh program kuch aise chalega. Har baar input() ka use kar ke user se ek number input lega. 
# Final line mein isne Total Sum: 417 print kara hai. 
# Yeh isiliye print kia hai kyunki 10+16+9+10+56+78+98+43+21+76 ka sum 417 hai.




# i=1
# while i<=10:
#     sum=int(input("enter a number"))
#     sum=sum+i
#     i=i+1
# print(sum)

i=1
sum=0
while i<=10:
    num=int(input("enter a number"))
    sum=num+sum
    i=i+1
print(sum)
