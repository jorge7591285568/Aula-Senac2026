from cmath import inf
from pickle import FALSE, TRUE
from platform import node




def bellman_ford(nodes, edges, start, target):
    dist = {n: float('inf') for n in nodes}
    dist[start] = 0
    
    for _ in range(len(nodes) - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:                dist[v] = dist[u] + w
            updated = True
        if not updated:
            break
    
    return dist[target]

# 1. Garanta que o 'D' está aqui dentro:
nodes = ['A', 'B', 'C', 'D'] 

# 2. Defina as suas arestas normalmente:
edges = [
    ('A', 'D', 4)  # O peso aqui é 4
]

# 3. Agora a execução funcionará sem erros:
print(bellman_ford(nodes, edges, 'A', 'D'))
