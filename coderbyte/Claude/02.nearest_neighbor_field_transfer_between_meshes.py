import numpy as np
from sklearn.neighbors import NearestNeighbors

def transfer_field_nn(
    source_points: np.ndarray,
    source_values: np.ndarray,
    target_points: np.ndarray,
) -> np.ndarray:
    """
    Transfer a scalar or vector field from source mesh to target mesh
    using nearest-neighbor interpolation.
    """
    # Build KD-tree on source points (O(N log N))
    nn = NearestNeighbors(n_neighbors=1, algorithm='kd_tree')
    nn.fit(source_points)

    # Query M target points (O(M log N))
    _, indices = nn.kneighbors(target_points)   # shape (M, 1)
    nearest_idx = indices[:, 0]                  # shape (M,)

    # Fancy indexing handles both scalar (N,) and vector (N, D) fields
    return source_values[nearest_idx]