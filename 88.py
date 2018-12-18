c,d=map(int,raw_input().split())
if(c>d):
    min1=c
else:
    min1=d
while(1):
    if(min1%c==0 and min1%d==0):
        print(min1)
        break
    min1=min1+1
