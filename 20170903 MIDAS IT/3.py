n=input()
w=raw_input().split()
W = [int(x) for x in w] # 숫자로 변환
maxn=0 #무게로 인해 공짜로 살수 있는 최대개수
count=0
for i in range(n) :
	count=0
	for j in range(n) :
		if  (W[j] - W[i]) <= 4  and  (W[j] - W[i]) >=0 : #무게의 차가 4보다 작으면 공짜로 살 수 있다.
			count+=1 #공짜로 살 수 있는 것들의 합을 구한다.
	if maxn<count :
		maxn=count
print(len(W) - maxn +1)
	