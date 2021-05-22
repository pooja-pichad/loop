# Ab hum loops ka use karke ek game banayenge.
#  Iss game ko hum "guessing game" bolte hai. 
#  1. Iss game mein humare pass pehle se ek number hota hai. 
#  Abhi ke liye maan lo yeh number 5 hai. 2. Uske baad hum user se 
#  1 se 10 ke beech mein ek number input lete hai. Phir user humare number ko guess 
#  karni ki koshish karta hai. 3. Jaise, agar user ne 3 input kiya. Hum check karenge
#   ki kya 3, 5 ke barabar hai? 4. 3, 5 ke barabar nahi hai isliye hum user se phir koi 
#   number input lenge. 5. Aur check karenge ki kya woh number 5 ke barabar hai? 
#   6. User ko 5 chances milenge number guess karne ke liye.











# number=5
# i=1
# while i<=5:
#     guess=int(input("enter a number "))
#     if guess<number:
#         print("your guess is to low ")
#     if guess>number:
#         print("your guess is to high ")
#     if guess==number:
#         print("you are correct guess")
#         break
#     i=i+1
# if i>5:
    # print("your guess is complete you lose")




n=1
num=5
print("what is your name ")
name=input("enter your name")
print("hello",name,"you are ready for the play game")
while n<=5:
    i=int(input("enter a number"))
    n=n+1
    if i==num:
        print("you are guess is correct you won ")
        # break
    else:
        print("you are not guess correct number you lose")