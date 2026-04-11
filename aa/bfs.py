from collections import deque

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G', 'H'],
    'D': ['A', 'I', 'J'],
    'E': ['B'],
    'F': ['B'],
    'G': ['C'],
    'H': ['C'],
    'I': ['D'],
    'J': ['D']
}

type Vertex = str
type Neighbors = list[str]

# Complexidade O(V + E)
# V -> cada vértice entra e sai da fila exatamente uma vez
# E -> vamos percorrer as arestas, mas como nós possuimos um set, não passamos pelos já visitados
# caso contrário seria O(V * E) 

# A BFS é famosa por encontrar o caminho mais curto em grafos não ponderados

# Em um grafo denso essa complexidade tende a O(V²) pois o número de arestas (E) é próximo ao limtie 
# Que seria V², então por mais que ainda seja V + E, isso é equivalente a V² na prática

# Memoria espacial aq é O(V) pois a fila vai ter no máximo V vértices vizinhos de um vértice que está esperando para ser visitado

def bfs(graph: dict[Vertex, Neighbors], start: Vertex):
    visited = {start}
    queue = deque[Vertex]([start])
    
    while queue:
        vertex = queue.popleft()
        print(f"[{vertex}]", end='->')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
print("\n--- Iterative BFS ---")      
bfs(graph, 'A')
print()

"""

--- Iterative BFS ---
[A]->[B]->[C]->[D]->[E]->[F]->[G]->[H]->[I]->[J]->

"""
