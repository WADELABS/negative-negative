"""
src/inference/gap_actuator.py
Void-to-Action: Triggering ASH inquiries from Negative Space voids.
"""

from typing import Dict, Any, List

class GapActuator:
    """
    The 'Gap-Actuator' bridges the void between doubt and execution.
    """
    def __init__(self, ignorance_threshold: float = 0.2):
        self.ignorance_threshold = ignorance_threshold

    def actuate_gap(self, mapped_void: Dict[str, Any]) -> Dict[str, Any]:
        """
        Determines if a mapped void requires an ASH inquiry or is 'Acceptable Ignorance'.
        """
        uncertainty = mapped_void.get("uncertainty", 1.0)
        salience = mapped_void.get("salience", 0.0)

        # Heuristic: Acceptable Ignorance
        if uncertainty < self.ignorance_threshold:
            return {
                "action": "IGNORE",
                "reason": f"Uncertainty ({uncertainty}) meets Acceptable Ignorance threshold."
            }

        # Trigger ASH Inquiry
        return {
            "action": "TRIGGER_ASH",
            "signal": "VOID_DETECTED",
            "target_layer": self._determine_target_layer(mapped_void),
            "payload": mapped_void
        }

    def _determine_target_layer(self, mapped_void: Dict[str, Any]) -> str:
        # Determine if the void is physical (Apparatus) or logical (System/Harness)
        if "hardware" in mapped_void.get("type", ""):
            return "APPARATUS"
        return "SYSTEM"
