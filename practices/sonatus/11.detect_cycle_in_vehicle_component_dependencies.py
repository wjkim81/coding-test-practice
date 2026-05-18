from collections import defaultdict, deque

def has_dependency_cycle(
    dependencies: dict[str, list[str]]
) -> bool:
    graph = defaultdict(list)
    in_degrees = defaultdict(int)
    
    # Build reversed graph (dependency → dependent)
    for component, dep_list in dependencies.items():  # ← .items()
        for dependency in dep_list:
            graph[dependency].append(component)
            in_degrees[component] += 1
    
    # Initialize queue with in-degree 0 nodes
    dq = deque()
    for component in dependencies:  # ← 모든 component 체크
        if in_degrees[component] == 0:  # defaultdict 덕분에 OK
            dq.append(component)
    
    # Kahn's: process and reduce in-degrees
    visited = 0
    while dq:
        component = dq.popleft()
        visited += 1
        for next_component in graph[component]:
            in_degrees[next_component] -= 1
            if in_degrees[next_component] == 0:
                dq.append(next_component)
    
    return visited != len(dependencies)  # ← cycle 있으면 True