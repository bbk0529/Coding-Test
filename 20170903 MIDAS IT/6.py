n=input()
a=raw_input().split()
A = [int(x) for x in a] # 숫자로 변환

benifit=[n/x * A[x-1] for x in range(1, n+1)] 
print(max(benifit))
