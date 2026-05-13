import numpy as np

def build_training_batch(samples):
    if not samples:
        raise ValueError("samples must not be empty")

    X_list = []
    y_list = []
    valid_ids = []
    expected_dim = None

    for sample in samples:
        features = sample.get("features")
        target = sample.get("target")

        if features is None or target is None:
            continue

        features = np.asarray(features, dtype=float)

        if features.ndim != 1:
            continue

        if not np.all(np.isfinite(features)):
            continue

        if not np.isfinite(target):
            continue

        if expected_dim is None:
            expected_dim = features.shape[0]

        if features.shape[0] != expected_dim:
            continue

        X_list.append(features)
        y_list.append(float(target))
        valid_ids.append(sample.get("id", None))

    if not X_list:
        raise ValueError("no valid samples")

    X = np.stack(X_list, axis=0)
    y = np.asarray(y_list, dtype=float)

    return X, y, valid_ids