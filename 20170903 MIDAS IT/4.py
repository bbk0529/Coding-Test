n=input()
L=[]
D=[]


def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)
    
for i in range(n):
	L.append(input())

for i in range(n-1):
	D.append(L[i+1]-L[i]) # 입력받은 값들의 차를 저장 

f_gcm=max(D) # 초기값 최대공약수를 D의 최대값으로 설정 
	
for i in range(n-1) :
	gcm=gcd(D[i], D[i-1])
	if f_gcm > gcm :
		f_gcm = gcm

count=0
for i in range(n-1) :
	count+=D[i]/f_gcm-1
	
print (count)