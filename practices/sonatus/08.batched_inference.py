class BatchedInference:
    def __init__(self, max_batch_size=32, max_wait_ms=50.0, model_fn=None):
        self.max_batch_size = max_batch_size
        self.max_wait_ms = max_wait_ms
        self.model_fn = model_fn
        self.readings = []  # [(reading_dict, timestamp_ms)]
    
    def add_reading(self, reading, timestamp_ms):
        self.readings.append((reading, timestamp_ms))
        
        # Check triggers AFTER append
        size_trigger = len(self.readings) >= self.max_batch_size
        time_trigger = (
            len(self.readings) > 0 and
            timestamp_ms - self.readings[0][1] >= self.max_wait_ms
        )
        
        if size_trigger or time_trigger:
            return self.flush(timestamp_ms)
        return None
    
    def flush(self, current_timestamp_ms):
        if not self.readings:
            return None
        
        readings_only = [r for r, _ in self.readings]
        # Option A: dict 통째로 (우리 합의)
        predictions = self.model_fn(readings_only)
        result = [
            {"vehicle_id": r["vehicle_id"], "prediction": p}
            for r, p in zip(readings_only, predictions)
        ]
        self.readings = []
        return result