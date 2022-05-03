
N = 1000
adj = [[] for i in range(N)]

def dfsUtil(u, node,visited,
			road_used, parent, it):
	c = 0

	for i in range(node):
		if (visited[i]):
			c += 1
	if (c == node):
		return

	visited[u] = True
	road_used.append([parent, u])

	print(u, end = " ")

	for x in adj[u]:

		if (not visited[x]):
			dfsUtil(x, node, visited,
					road_used, u, it + 1)


	for y in road_used:
		if (y[1] == u):
			dfsUtil(y[0], node, visited,
					road_used, u, it + 1)


def dft(node):

	
	visited = [False for i in range(node)]

	
	road_used = []

	for i in range(node):
		visited[i] = False

	dfsUtil(0, node, visited,
			road_used, -1, 0)
			

def insertEdge(u, v):
	
	adj[u].append(v)
	adj[v].append(u)


if __name__ == '__main__':
	
	node = 11
	edge = 13

	insertEdge(0, 1)
	insertEdge(0, 2)
	insertEdge(1, 5)
	insertEdge(1, 6)
	insertEdge(2, 4)
	insertEdge(2, 9)
	insertEdge(6, 7)
	insertEdge(6, 8)
	insertEdge(7, 8)
	insertEdge(2, 3)
	insertEdge(3, 9)
	insertEdge(3, 10)
	insertEdge(9, 10)


	dft(node)


