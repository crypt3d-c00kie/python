graph = {
	5 : [3,7],
	3 : [2,4],
	2 : [],
	4 : [8],
	7 : [8],
	8 : []
}

visited = []

def dfsx(ip_graph, ip_visited, ip_node):
	for key in ip_graph:
		ip_visited.append(key)
	
	for i in ip_visited:
		print(i, graph[i])

def dfs(ip_graph,ip_visited,ip_node):
	if ip_node not in ip_visited:
		print(ip_node)
		ip_visited.append(ip_node)
		for value in ip_graph[ip_node]:
			#recursion is used in dfs
			dfs(ip_graph,ip_visited,value)
			
#driver code

dfs(graph, visited, 5)