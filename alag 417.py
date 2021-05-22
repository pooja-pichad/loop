# Ek loop banao jo user se 10 numbers ko input le. 
# Input lene ke baad unn saare numbers ka sum print kare. 
# **Note: Iss program ka counter 50 se shuru hona chaiye. 
# Aur aise code likho ki counter mein subtract karke loop chale. Dimaag mein yeh 
# rakhiye ki hum humesha ** Yeh program kuch aise chalega. Har baar input() ka use kar 
# ke user se ek number input lega. Final line mein isne Total Sum: 417 print kara hai.
#  Yeh isiliye print kia hai kyunki 10+16+9+10+56+78+98+43+21+76 ka sum 417 hai.





i=50
sum=0
while i>40:
    num=int(input("enter a number"))
    sum=sum+num
    i=i-1
print(sum)
