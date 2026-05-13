import numpy as np

def detect_unstable_predictions(X, pred, ref, threshold_std=3.0):
    X = np.asarray(X, dtype=float)
    pred = np.asarray(pred, dtype=float)
    ref = np.asarray(ref, dtype=float)

    if X.size == 0 or pred.size == 0 or ref.size == 0:
        raise ValueError("X, pred, and ref must not be empty")

    if X.shape != pred.shape or X.shape != ref.shape:
        raise ValueError("X, pred, and ref must have the same shape")

    valid_mask = np.isfinite(X) & np.isfinite(pred) & np.isfinite(ref)

    if not np.any(valid_mask):
        raise ValueError("no valid samples")

    abs_error = np.abs(pred[valid_mask] - ref[valid_mask])

    mean_error = abs_error.mean()
    std_error = abs_error.std()

    threshold = mean_error + threshold_std * std_error

    valid_indices = np.where(valid_mask)[0]
    unstable_indices = valid_indices[abs_error > threshold]

    return {
        "unstable_indices": unstable_indices.tolist(),
        "mean_error": mean_error,
        "std_error": std_error,
        "num_unstable": unstable_indices.size,
    }