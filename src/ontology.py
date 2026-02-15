"""
src/ontology.py
Ontological Mapping: Defining the boundaries of the known.
"""

from typing import Dict, List, Any
from .doubt import DoubtEngine
from .inference.gap_actuator import GapActuator

class Ontology:
    """
    The Semantic Map: Handling the classification and actuation of 'The Void'.
    """
    def __init__(self):
        self.doubt_engine = DoubtEngine()
        self.actuator = GapActuator()
        self.nodes = set()
        self.edges = {}

    def analyze_claim(self, claim: str) -> Dict[str, Any]:
        """
        Maps the void and triggers the Gap-Actuator.
        """
        words = claim.split()
        doubt_score = self.doubt_engine.calculate_doubt(claim)
        
        mapped_void = {
            "claim": claim,
            "uncertainty": doubt_score,
            "salience": 1.0 - doubt_score,
            "semantic_density": round(len(set(words)) / len(words), 4) if words else 0,
            "type": "epistemological_gap"
        }
        
        # ACTIVATE GAP-ACTUATOR
        actuation = self.actuator.actuate_gap(mapped_void)
        
        return {
            "mapped_void": mapped_void,
            "actuation": actuation
        }

    def add_fact(self, source: str, target: str, relationship: str):
        """Adds a fact to the sparse semantic map."""
        self.nodes.add(source)
        self.nodes.add(target)
        if source not in self.edges:
            self.edges[source] = []
        self.edges[source].append({"target": target, "rel": relationship})

    def get_inference_gaps(self, target_node: str) -> List[str]:
        """Identifies nodes that are poorly connected/defined."""
        if target_node not in self.nodes:
            return ["Node not found in current ontology."]
        
        connections = self.edges.get(target_node, [])
        if len(connections) < 2:
            return [f"High Inference Gap: '{target_node}' is semantically isolated."]
        return []
