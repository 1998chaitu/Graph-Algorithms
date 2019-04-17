import heapq

def dijkstras(src,graph):
	vertex_map[src][0]=0
	dist[src]=0

	vertex_map[src][0]=0
	heapq.heapify(heap)
	
	while(len(heap)!=1):
		cur_vtx=heapq.heappop(heap)
		heapq.heapify(heap)
		dist[cur_vtx[1]]=cur_vtx[0]
		cur_vtx=cur_vtx[1]

		for i in range(len(graph[cur_vtx])):
			v=graph[cur_vtx][i][0]
			vd=graph[cur_vtx][i][1]
			if(v in vertex_map):
				if(dist[cur_vtx]+vd < vertex_map[v][0]):
					vertex_map[v][0]=dist[cur_vtx]+vd
					heapq.heapify(heap)


#enter no of vertices, edges
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
heap=[]
dist=[]
vertex_map={}
for i in range(n+1):
	dist.append(99999)
	vertex_map[i]=[99999,i]
	heap.append(vertex_map[i])

for i in range(m):
	#enter edges and weight bw 2 edges
	x,y,wt=map(int,input().split())
	graph[x].append((y,wt))
	graph[y].append((x,wt))
dijkstras(1,graph)
print(dist[1:])