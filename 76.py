s=int(raw_input())
factor=0
for i in range(1,s):
    factor=i
    s%i==0
if(factor>1):
    print 'yes'
else:
    print 'no'
