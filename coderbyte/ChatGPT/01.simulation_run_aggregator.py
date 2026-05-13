def summarize_simulations(runs, target_metric, group_by_param):
    result = {}

    for run in runs:
        if run.get("status") != "ok":
            continue

        parameters = run.get("parameters", {})
        metrics = run.get("metrics", {})

        if group_by_param not in parameters:
            continue

        if target_metric not in metrics:
            continue

        value = metrics[target_metric]

        if not isinstance(value, (int, float)):
            continue

        group_value = parameters[group_by_param]
        design_id = run.get("design_id")

        if group_value not in result:
            result[group_value] = {
                "count": 0,
                "sum": 0.0,
                "min": float("inf"),
                "max": -float("inf"),
                "best_design_id": None,
            }

        group = result[group_value]
        group["count"] += 1
        group["sum"] += value

        if value < group["min"]:
            group["min"] = value
            group["best_design_id"] = design_id

        if value > group["max"]:
            group["max"] = value

    for group_value, group in result.items():
        group["mean"] = group["sum"] / group["count"]
        del group["sum"]

    return result