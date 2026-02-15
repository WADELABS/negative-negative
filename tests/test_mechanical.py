"""
tests/test_mechanical.py
Verification of mechanical linkage and 'Missing Bracket' inference.
"""

import unittest
from src.constraints.mechanical_linkage import MechanicalLinkage

class TestMechanical(unittest.TestCase):
    def setUp(self):
        self.linkage = MechanicalLinkage()

    def test_bracket_inference(self):
        """Test calculation of bridge geometry between engine and frame."""
        engine = (0, 0)
        frame = (10, 10)
        result = self.linkage.infer_missing_bracket(engine, frame)
        
        self.assertEqual(result["status"], "INFERRED")
        self.assertAlmostEqual(result["required_length"], 14.1421, places=4)
        self.assertEqual(result["mount_angle"], 45.0)

    def test_bolt_pattern_match(self):
        """Test identification of known mechanical patterns."""
        # BMW R Series Flange
        match = self.linkage.match_bolt_pattern(5, 5.0)
        self.assertIn("BMW_R_SERIES_FLANGE", match)
        
        # Unknown/Scam Pattern
        mismatch = self.linkage.match_bolt_pattern(4, 5.0)
        self.assertIn("UNKNOWN_PATTERN", mismatch)

if __name__ == "__main__":
    unittest.main()
