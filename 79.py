import math
l,r=map(int,raw_input().split())
p=l*r
if math.sqrt(p).is_integer():
    print 'yes'
else:
    print 'no'
