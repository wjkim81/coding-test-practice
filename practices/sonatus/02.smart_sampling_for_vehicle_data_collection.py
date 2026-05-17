import random

def select_events_to_upload(
    events: list[dict],
    bandwidth_budget_mb: float,
) -> list[str]:
    # Intent:
    # 1. Split budget 50/50: uncertain pool + random pool
    # 2. Uncertain: sort by |confidence - 0.5|, greedy fill
    # 3. Random: shuffle remaining (excluding uncertain picks), greedy fill
    # 4. Edge: under-fill OK, never over-fill
    # Note: Diversity sampling omitted; would extend by adding 3rd pool with
    #       stratified sampling over scenario_features.
    
    UNCERTAIN_RATIO = 0.5
    RANDOM_RATIO = 0.5
    
    uncertain_budget = bandwidth_budget_mb * UNCERTAIN_RATIO
    random_budget = bandwidth_budget_mb * RANDOM_RATIO
    
    collected_ids = []
    picked = set()
    
    # Uncertain pool: most uncertain first
    events_by_uncertainty = sorted(events, key=lambda e: abs(e['confidence'] - 0.5))
    used = 0.0
    for event in events_by_uncertainty:
        if used + event["data_size_mb"] <= uncertain_budget:
            collected_ids.append(event["event_id"])
            picked.add(event["event_id"])
            used += event["data_size_mb"]
    
    # Random pool: from remaining
    remaining = [e for e in events if e["event_id"] not in picked]
    random.shuffle(remaining)
    used = 0.0
    for event in remaining:
        if used + event["data_size_mb"] <= random_budget:
            collected_ids.append(event["event_id"])
            used += event["data_size_mb"]
    
    return collected_ids