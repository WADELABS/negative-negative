"""
src/constraints/mechanical_linkage.py
Mechanical Linkage: Defining the 'Missing Bracket' via physical constraints.
"""

from typing import Dict, List, Tuple
import math

class MechanicalLinkage:
    """
    Infers the existence and parameters of missing physical components
    based on the 'Negative Space' between known constraints.
    """
    def __init__(self):
        self.bolt_patterns = {
            "SMALL_BLOCK_CHEVY": {"holes": 4, "diameter": 3.75, "angle": 90},
            "BMW_R_SERIES_FLANGE": {"holes": 5, "diameter": 5.0, "angle": 72}
        }

    def infer_missing_bracket(self, engine_mounts: Tuple[float, float], frame_rail: Tuple[float, float]) -> Dict:
        """
        Calculates the geometry of a bracket that doesn't exist yet, 
        but is necessitated by the void between engine and frame.
        """
        x1, y1 = engine_mounts
        x2, y2 = frame_rail
        
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
        
        return {
            "status": "INFERRED",
            "component": "ADAPTER_BRACKET",
            "required_length": round(distance, 4),
            "mount_angle": round(angle, 2),
            "epistemological_standing": "CERTAIN_BY_GEOMETRY"
        }

    def match_bolt_pattern(self, detected_holes: int, measured_diameter: float) -> str:
        """
        Identifies a specific mechanical pattern from partial or 'ghost' data.
        """
        for name, specs in self.bolt_patterns.items():
            if specs["holes"] == detected_holes and abs(specs["diameter"] - measured_diameter) < 0.1:
                return f"MATCH FOUND: {name}"
        
        return "UNKNOWN_PATTERN: Possible custom fabrication or hallucinated hardware."
