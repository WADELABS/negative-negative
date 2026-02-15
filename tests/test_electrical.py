"""
tests/test_electrical.py
Verification of electrical shadow and phantom relay detection.
"""

import unittest
import sys
import os

# Ensure the 'src' directory is in the path for the IDE and test runner
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.inference.electrical_shadow import ElectricalShadow

class TestElectrical(unittest.TestCase):
    def setUp(self):
        self.shadow = ElectricalShadow()

    def test_electrical_void_mapping(self):
        """Test detection of missing components in the 1967 BMW scenario."""
        # Scenario: Missing relay in the ignition path
        components = ["IGNITION_SWITCH", "COIL", "BATTERY"]
        result = self.shadow.map_electrical_void(components, 2)
        
        self.assertEqual(result["status"], "ANALYZED")
        # Ensure 'RELAY' is identified as missing in the IGNITION_TO_COIL path
        ign_path = next(f for f in result["findings"] if f["path"] == "IGNITION_TO_COIL")
        self.assertIn("RELAY", ign_path["missing_components"])

    def test_phantom_relay_localization(self):
        """Test heuristic for locating phantom relays."""
        match = self.shadow.locate_phantom_relay(["no_ignition_crank"])
        self.assertIn("PHANTOM RELAY DETECTED", match)

if __name__ == "__main__":
    unittest.main()
