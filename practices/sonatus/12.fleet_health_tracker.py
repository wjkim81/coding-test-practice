from collections import defaultdict
import heapq

class FleetHealthTracker:
    def __init__(self, component_weights: dict[str, float]):
        """
        component_weights: {"engine": 0.4, "battery": 0.3, "brake": 0.3, ...}
        Weights sum to 1.0.
        """
        self.component_weights = component_weights
        self.required_components = set(component_weights.keys())
        self.vehicle_readings = defaultdict(dict)  # vehicle_id → {component → health}
        self.aggregate_scores = {}  # vehicle_id → aggregate (only complete)
    
    def update_reading(
        self, 
        vehicle_id: str, 
        component: str, 
        health: float  # 0.0 ~ 1.0
    ) -> None:
        """
        Update one component's health reading for a vehicle.
        """
        self.vehicle_readings[vehicle_id][component] = health
        if len(self.vehicle_readings[vehicle_id]) == len(self.required_components):
            risk_score = 0
            # We assume that components is consistent with defined in component_weights, No error check
            for comp, score in self.vehicle_readings[vehicle_id].items():
                risk_score += self.component_weights[comp] * score
            self.aggregate_scores[vehicle_id] = risk_score
    
    def get_riskiest_vehicles(self, k: int) -> list[tuple[str, float]]:
        """
        Return top-K vehicles with LOWEST aggregate health score.
        Sorted ascending by score.
        
        A vehicle's aggregate score is the weighted average of its
        component health readings. Only consider vehicles that have
        readings for ALL components in component_weights.
        """
        return heapq.nsmallest(
            k, 
            self.aggregate_scores.items(),  # ← .items() : (id, score) tuple iterate
            key=lambda x: x[1]  # ← x[1]은 score
        )
