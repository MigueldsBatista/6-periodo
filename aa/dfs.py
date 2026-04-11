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

def dfs_iterative(graph: dict[Vertex, Neighbors], start_node: Vertex):
    visited = {start_node}
    # Pilha explícita evita Stack Overflow da recursão
    stack = [start_node]
    
    while stack:
        vertex = stack.pop() # LIFO O(1)
        print(f"[{vertex}]", end='->')
        
        # Processamento do vértice aqui
        # Adiciona vizinhos à pilha (extend é eficiente)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)


def dfs_recursive(
    graph: dict[Vertex, Neighbors],
    node: Vertex,
    visited: set | None =None
):
    if visited is None:
        visited = set()
        
    if node not in visited:
        print(f"[{node}]", end='->')

        visited.add(node)
        
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)


print("\n--- Iterative DFS ---")
dfs_iterative(graph, 'A')
print()
print("\n--- Recursive DFS ---")
dfs_recursive(graph, 'A')
print()

"""

--- Iterative DFS ---
[A]->[D]->[J]->[I]->[C]->[H]->[G]->[B]->[F]->[E]->

--- Recursive DFS ---
[A]->[B]->[E]->[F]->[C]->[G]->[H]->[D]->[I]->[J]->

"""

