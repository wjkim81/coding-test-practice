class ComponentNode:
    def __init__(self, name: str, is_faulty: bool = False):
        self.name = name
        self.is_faulty = is_faulty
        self.children: list[ComponentNode] = []

def count_faulty_subsystems(root: ComponentNode) -> int:
    """
    Count how many components have at least one faulty 
    component in their subtree (including themselves).
    """
    
    # 1. 자식들 재귀 결과 모음
    sub_count = 0
    for ch in root.children:
        sub_count += count_faulty_subsystems(ch)
    
    # 2. 자손에 faulty 있나? (count > 0이면 있음)
    has_descendant_faulty = sub_count > 0
    
    # 3. 자기가 faulty subsystem?
    if root.is_faulty or has_descendant_faulty:
        sub_count += 1
    
    return sub_count

    
    