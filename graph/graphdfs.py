def dfs(graph, start):

  visited = set()
  stack = [start]

  while stack:
    vertex = stack.pop()
    if vertex not in visited:
      visited.add(vertex)
      print(vertex, end = ' ') 
      for neighbor in graph[vertex]:
        stack.append(neighbor)

  return visited

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

dfs(graph, 'A')


"""

dynamic implementaion
n=int(input("enter the number of times:"))
for i in range(n):
  key = eval(input("enter key"))
  value = eval(input("enter value"))
  d[key] = value
  
dfs(graph,'a')

"""

