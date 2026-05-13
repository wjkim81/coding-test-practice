import numpy as np

def compute_field_error(pred, ref):
    if pred.shape != ref.shape:
        raise ValueError("pred and ref must have the same dimension")
    
    pred_flat = pred.ravel()
    ref_flat = ref.ravel()

    pred_mask = np.isfinite(pred_flat)
    ref_mask = np.isfinite(ref_flat)

    valid_mask = pred_mask & ref_mask

    if not np.any(valid_mask):
        raise ValueError("no valid values to compare")
    
    pred_valid = pred_flat[valid_mask]
    ref_valid = ref_flat[valid_mask]

    mae = np.mean(np.abs(pred_valid - ref_valid))
    rmse = np.sqrt(np.mean((pred_valid - ref_valid) ** 2))
    max_error = np.max(np.abs(pred_valid - ref_valid))
    valid_count = pred_valid.size

    return {
        "mae": mae,
        "rmse": rmse,
        "max_error": max_error,
        "valid_count": valid_count,
    }