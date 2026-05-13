import numpy as np

def normalize_features(X):
    X = np.asarray(X, dtype=float)

    if X.size == 0:
        raise ValueError("X must not be empty")

    if X.ndim != 2:
        raise ValueError("X must be a 2D array")

    valid_mask = np.isfinite(X)
    valid_counts = valid_mask.sum(axis=0)

    X_clean = np.where(valid_mask, X, np.nan)

    means = np.nanmean(X_clean, axis=0)
    stds = np.nanstd(X_clean, axis=0)

    X_norm = np.full_like(X, np.nan, dtype=float)

    for j in range(X.shape[1]):
        if valid_counts[j] == 0:
            continue

        col_mask = valid_mask[:, j]

        if stds[j] == 0:
            X_norm[col_mask, j] = 0.0
        else:
            X_norm[col_mask, j] = (X[col_mask, j] - means[j]) / stds[j]

    stats = {
        "mean": means,
        "std": stds,
        "valid_count": valid_counts,
    }

    return X_norm, stats