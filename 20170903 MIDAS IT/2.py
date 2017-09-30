n=input()
a=[]
totalnum=[]
for i in range(n):
	sum=0
	a=raw_input()
	b=list(a)
	
	for j in range(len(a)/2):
		sum+=(abs(ord(b[j]) - ord(b[-j-1])))
	totalnum.append(sum)
for i in range(n):
		print (totalnum[i])