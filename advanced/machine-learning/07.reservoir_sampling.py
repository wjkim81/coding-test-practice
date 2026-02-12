import random
from typing import List

class ReservoirSampler:
    def __init__(self, k: int):
        self.k = k
        self.reservoir: List[float] = []
        self.n = 0  # number of items seen so far

    def put(self, x: float) -> None:
        self.n += 1

        if len(self.reservoir) < self.k:
            self.reservoir.append(x)
            return

        # j in [0, n-1]
        j = random.randrange(self.n)
        if j < self.k:
            self.reservoir[j] = x

    def query_percentile(self, q: float) -> float:
        """
        q in [0,1]. Returns approximate quantile from reservoir.
        """
        if not self.reservoir:
            raise ValueError("No samples yet")

        s = sorted(self.reservoir)
        idx = int(q * (len(s) - 1))  # simple nearest-rank variant
        return s[idx]
