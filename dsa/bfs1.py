graph = {
	5 : [3,7],
	3 : [2,4],
	2 : [],
	4 : [8],
	7 : [8],
	8 : []
}

visited_nodes = []
queue = []


def bfs(ip_visited,ip_graph,ip_node):
	ip_visited.append(ip_node)
	queue.append(ip_node)
	
	while queue:
		m = queue.pop(0)
		print(m)

		for neighbour in graph[m]:
			if neighbour not in ip_visited:
				ip_visited.append(neighbour)
				queue.append(neighbour)
		
#driver code
bfs(visited_nodes,graph,5)