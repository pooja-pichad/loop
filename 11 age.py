# 11 logon ka weight input le aur fir average weight print kare. 
# Aur fir yeh bhi check kare ki kya Average weight 5 ka multiple
#  (Yaani 5 se bhaag karne par shesh 0 bachta hai) hai ya nahi? Note: 
#  Isme aapko input ka use karna padega. Aap loop ke andar raw input ka use kar ke
#   11 baar raw_input le sakte ho.




i=1
sum=0
while i<=11:
    weight=int(input("enter a number "))
    sum=sum+weight
    avg=sum/11
    i=i+1
print(avg)
if avg%5==0:
    print("divible hai",avg)
else:
    print("not divisible",avg)