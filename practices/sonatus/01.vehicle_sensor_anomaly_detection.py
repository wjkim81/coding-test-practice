import numpy as np

def detect_anomalies(readings: list[float], window_size: int = 10) -> list[int]:
    """
    Returns indices of anomalous readings.
    """
    # set k to define define anomaly threshold 
    k = 2
    anomalies = []
    for i in range(window_size, len(readings)):
        window = readings[i - window_size:i]
        window_arr = np.asarray(window)
        mean = window_arr.mean()
        std = window_arr.std()
        # print(f"i: {i}, mean: {mean}, std: {std}")

        if np.abs(readings[i] - mean) > k * std:
            anomalies.append(i)

    return list(anomalies)



if __name__ == "__main__":
    readings = [85.0, 85.2, 85.1, 84.9, 85.0, 85.3, 85.1, 84.8, 85.0, 85.2, 
            85.1, 130.5,  # ← anomaly
            85.0, 85.2]

    print(detect_anomalies(readings))
        