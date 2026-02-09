# The Negative Space Framework
### An Epistemology of Absence (Void Mapping)

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**"We do not map the territory. We map the holes in the map."**

The **Negative Space Framework** is an experimental AI architecture that shifts focus from "Interpolation" (finding a path from A to B) to "Epistemic Mapping" (identifying exactly why B is currently impossible from A).

> **Core Philosophy**: To cross a void, you must first measure its depth.

## 🚀 Key Capabilities

*   **Void Mapping**: Detects and classifies gaps between current state and goal state.
*   **Gap Taxonomy**: Distinguishes between:
    *   `DEPENDENCY_GAP`: Missing components or data.
    *   `INFORMATION_GAP`: Missing knowledge.
    *   `CONSTRAINT_GAP`: Blockers (budget, time, physics).
    *   `CAPABILITY_GAP`: Missing skills or tools.
*   **Navigation Strategies**: Algorithms like "Gap Hopping" and "Boundary Skirting" to traverse the unknown.
*   **Void Visualization**: Graphical representation of the "shape" of missing information.

## 🛠️ Components

1.  **Core (`core.py`)**: Data structures for `VoidMap` and `Gap`.
2.  **Mapping Engine (`mapping.py`)**: Contrastive analysis logic.
3.  **Navigation Engine (`navigation.py`)**: Pathfinding through negative space.
4.  **Clustering (`clustering.py`)**: Semantic grouping of voids.
5.  **Agents (`agent.py`)**: `VoidAgent` and `VoidCollective`.

## 📦 Getting Started

### Prerequisites
*   Python 3.9+
*   `networkx`
*   `matplotlib`
*   `numpy`

### Installation

```bash
git clone https://github.com/WADELABS/negative-negative.git
cd negative-negative
pip install -r requirements.txt
```

### Usage

Run the interactive demo to see the framework in action:

```bash
python demo.py
```

## 🧠 Example Output

```text
Mapping void between current state and goal...

Void Analysis Complete:
  Total gaps identified: 2
  Void density: 0.180

Critical Findings:
  - Missing processed_training_data
  - Type mismatch: accuracy (float vs int)

Recommendation: Proceed cautiously - while void is small, remaining gaps may be critical.
```

---
*Generated for the Negative Space Framework v1.0*
