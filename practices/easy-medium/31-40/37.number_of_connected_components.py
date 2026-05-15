from typing import List
from collections import deque, defaultdict

def number_of_connected_components(n: int, edges: List[List[int]]) -> int:
    if len(edges) == 0:
        return n

    edge_map = defaultdict(list)
    for node, neighbor  in edges:
        edge_map[node].append(neighbor)
        edge_map[neighbor].append(node)

    visited = [0] * n
    def bfs(node: int) -> None:
        q = deque()
        q.append(node)
        visited[node] = 1

        while q:
            cur_node = q.popleft()
            for next_node in edge_map[cur_node]:
                if visited[next_node] == 0:
                    visited[next_node] = 1
                    q.append(next_node)

    count = 0
    for node in range(n):
        if visited[node] == 0:
            count += 1
            bfs(node)
    return count

# Union-Find Solution
def number_of_connected_components_union_find(n: int, edges: List[List[int]]) -> int:
    if not edges:
        return n
    
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            x = find(parent[x])
        return x
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
    
    for a, b in edges:
        union(a, b)
    
    # 루트가 자기 자신인 노드 수 = 컴포넌트 수
    count = sum(1 for i in range(n) if find(i) == i)
    return count