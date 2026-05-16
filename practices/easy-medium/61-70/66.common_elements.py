from typing import List

def find_common_elements(nums_list: List[List[int]]) -> List[int]:
    if not nums_list:
        return []
    
    common = set(nums_list[0])
    for row in nums_list[1:]:
        common &= set(row)  # set intersection!
        if not common:
            return []
    
    return sorted(common)
