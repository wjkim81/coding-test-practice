def deduplicate_burst_events(
    events: list[tuple[float, str]],
    time_window: float
) -> list[tuple[float, str]]:
    
    if not events:
        return []
    
    result = []
    last_seen = {}
    for ts, event_type in events:
        is_new_burst = (
            event_type not in last_seen 
            or ts - last_seen[event_type] > time_window
        )
        if is_new_burst:
            result.append((ts, event_type))
        last_seen[event_type] = ts  # 어떤 case든 항상 갱신

    return result

        