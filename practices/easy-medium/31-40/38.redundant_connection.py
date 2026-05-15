from typing import List, Tuple

def redundant_connection(edges: List[List[int]]) -> List[int]:
    parent = [i for i in range(len(edges) + 1)]

    def find(x: int) -> int:
        while parent[x] != x:
            x = parent[x]
        return x

    def union(a: int, b: int) ->bool:
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return False
        return True
    
    for a, b in edges:
        if union(a, b):
            return (a, b)
