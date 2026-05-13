def compute_bounding_box(points):
    if not points:
        raise ValueError("points must not be empty")

    result = {
        "min": [float("inf")] * 3,
        "max": [float("-inf")] * 3,
    }

    for point in points:
        if len(point) != 3:
            raise ValueError("each point must have 3 coordinates")

        x, y, z = point

        result["min"][0] = min(result["min"][0], x)
        result["min"][1] = min(result["min"][1], y)
        result["min"][2] = min(result["min"][2], z)

        result["max"][0] = max(result["max"][0], x)
        result["max"][1] = max(result["max"][1], y)
        result["max"][2] = max(result["max"][2], z)

    xmin, ymin, zmin = result["min"]
    xmax, ymax, zmax = result["max"]

    result["center"] = (
        (xmin + xmax) / 2,
        (ymin + ymax) / 2,
        (zmin + zmax) / 2,
    )

    result["size"] = (
        xmax - xmin,
        ymax - ymin,
        zmax - zmin,
    )

    result["min"] = tuple(result["min"])
    result["max"] = tuple(result["max"])

    return result