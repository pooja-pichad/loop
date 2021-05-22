i=0
str1='python'
while i<len(str1):
    if str1[i]=='y'or str1[i]=='h':
        i=i+1
        continue
    print("current letter",str1[i])
    i=i+1