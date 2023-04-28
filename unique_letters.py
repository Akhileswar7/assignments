string=input()
s=""
for i in string:
    if i in s:
        continue
    s=s+i
for i in range(0,len(s)):
    if len(s)==i+1:
        print(s[i])
    else:
        print(s[i],end=",")
