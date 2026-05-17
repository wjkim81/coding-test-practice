import heapq

def top_k_confident_vehicles(
    scores: list[tuple[str, float]],
    k: int
) -> list[str]:

    if not scores:
        return []
    
    collected = {}
    
    for score in scores:
        vehicle_id, scr = score

        if vehicle_id not in collected or scr > collected[vehicle_id]:
            collected[vehicle_id] = scr

    return heapq.nlargest(k, collected, key=lambda x: collected[x])


    



