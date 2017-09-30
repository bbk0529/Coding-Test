m, n, k = raw_input().split()
m=int(m)
n=int(n)
k=int(k)

total_Stations= m*n;
	
for i in range(1, k+1) :
	r, c1, c2 = raw_input().split()
	r=int(r)
	c1=int(c1)
	c2=int(c2)
	total_Stations-=(c2-c1+1)
	
print (total_Stations)