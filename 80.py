def odddig():
	v=int(input())
	a=[]
	while(v!=0):
		a.append(v%10)
		v//=10
	for i in range(len(a)-1,-1,-1):
		if a[i]%2!=0:
			print(a[i]),
try:
	odddig()
except:
	print('invalid')
