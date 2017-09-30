parent = {}
rank = {}
​
def make_set(v):
    parent[v] = v
    rank[v] = 0
​

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]
​

def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:
        
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1
​
def kruskal(vertices, edges):    
    for v in vertices:
        make_set(v)
    mst = []   
    edges.sort()
    
    for edge in edges:
        weight, v, u = edge
                
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    total=0
    for i in range(len(mst)) :
		total+=mst[i][0]
​	return total

edges=[]
vertices=[]





n,w=raw_input().split() #1행 입력
n=int(n)
w=int(w)

temp=set([])
for i in range(w) :
	edge1, edge2, cost = raw_input().split()
	cost=int(cost)
	edges.append((cost,edge1,edge2))
	vertices.extend([edge1,edge2])
	
vertices=set(vertices)
vertices=list(vertices)

print (kruskal(vertices, edges))