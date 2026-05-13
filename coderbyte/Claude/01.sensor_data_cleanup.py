import numpy as np

def clean_sensor_data(data: np.ndarray, k: float = 3.0) -> np.ndarray:
    data = data.copy()  # 입력을 mutate하지 않는 게 좋은 습관
    T, C = data.shape
    t = np.arange(T)

    for c in range(C):
        col = data[:, c]

        # Step 1: stats ignoring NaN
        mean_c = np.nanmean(col)
        std_c = np.nanstd(col)

        # Step 2: mark outliers as NaN
        outliers = np.abs(col - mean_c) > k * std_c
        col[outliers] = np.nan

        # Step 3: interpolate NaNs along time
        nan_mask = np.isnan(col)
        if nan_mask.any():
            col[nan_mask] = np.interp(
                t[nan_mask],
                t[~nan_mask],
                col[~nan_mask],
            )
        # data[:, c]는 col을 가리키는 view라서 자동 반영됨

    return data