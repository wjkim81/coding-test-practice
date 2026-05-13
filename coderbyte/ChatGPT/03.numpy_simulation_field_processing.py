import numpy as np

def normalize_fields(fields):
    if not fields:
        raise ValueError("fields must not be empty")

    stacked = np.concatenate([f.ravel() for f in fields])

    mask = np.isfinite(stacked)
    valid_values = stacked[mask]

    if valid_values.size == 0:
        raise ValueError("all values are invalid")

    global_mean = valid_values.mean()
    global_std = valid_values.std()

    normalized_fields = []

    for field in fields:
        finite_mask = np.isfinite(field)

        normalized = field.copy()

        if global_std == 0:
            normalized[finite_mask] = 0.0
        else:
            normalized[finite_mask] = (
                field[finite_mask] - global_mean
            ) / global_std

        normalized_fields.append(normalized)

    stats = {
        "mean": global_mean,
        "std": global_std,
        "count": valid_values.size,
    }

    return normalized_fields, stats



