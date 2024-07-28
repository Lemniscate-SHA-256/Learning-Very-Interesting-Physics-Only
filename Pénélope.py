import numpy as np
import matplotlib.pyplot as plt

# Predefined data for a few elements
ELEMENT_DATA = {
    1: {
        'name': 'Hydrogen',
        'ground_state': '1s1',
        'excited_states': ['2s1', '2p1'],
        'quantum_states': [(1, 0, 0, 1/2), (2, 0, 0, 1/2), (2, 1, -1, 1/2), (2, 1, 0, 1/2), (2, 1, 1, 1/2)]
    },
    2: {
        'name': 'Helium',
        'ground_state': '1s2',
        'excited_states': ['2s2', '2p2'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2)]
    },
    3: {
        'name': 'Lithium',
        'ground_state': '1s2 2s1',
        'excited_states': ['2s2', '2p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2)]
    },
    4: {
        'name': 'Beryllium',
        'ground_state': '1s2 2s2',
        'excited_states': ['2s2 2p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2)]
    },
    5: {
        'name': 'Boron',
        'ground_state': '1s2 2s2 2p1',
        'excited_states': ['2s2 2p2'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2)]
    },
    6: {
        'name': 'Carbon',
        'ground_state': '1s2 2s2 2p2',
        'excited_states': ['2s2 2p3'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2)]
    },
    7: {
        'name': 'Nitrogen',
        'ground_state': '1s2 2s2 2p3',
        'excited_states': ['2s2 2p4'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2)]
    },
    8: {
        'name': 'Oxygen',
        'ground_state': '1s2 2s2 2p4',
        'excited_states': ['2s2 2p5'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2)]
    },
    9: {
        'name': 'Fluorine',
        'ground_state': '1s2 2s2 2p5',
        'excited_states': ['2s2 2p6'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2)]
    },
    10: {
        'name': 'Neon',
        'ground_state': '1s2 2s2 2p6',
        'excited_states': ['3s2 3p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2)]
    },
    11: {
        'name': 'Sodium',
        'ground_state': '1s2 2s2 2p6 3s1',
        'excited_states': ['3p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2)]
    },
    12: {
        'name': 'Magnesium',
        'ground_state': '1s2 2s2 2p6 3s2',
        'excited_states': ['3p2'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2)]
    },
    13: {
        'name': 'Aluminum',
        'ground_state': '1s2 2s2 2p6 3s2 3p1',
        'excited_states': ['3p2', '3d1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2)]
    },
    14: {
        'name': 'Silicon',
        'ground_state': '1s2 2s2 2p6 3s2 3p2',
        'excited_states': ['3p3', '3d2'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2)]
    },
    15: {
        'name': 'Phosphorus',
        'ground_state': '1s2 2s2 2p6 3s2 3p3',
        'excited_states': ['3p4', '3d3'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2)]
    },
    16: {
        'name': 'Sulfur',
        'ground_state': '1s2 2s2 2p6 3s2 3p4',
        'excited_states': ['3p5', '3d4'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2)]
    },
    17: {
        'name': 'Chlorine',
        'ground_state': '1s2 2s2 2p6 3s2 3p5',
        'excited_states': ['3p6', '3d5'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2)]
    },
    18: {
        'name': 'Argon',
        'ground_state': '1s2 2s2 2p6 3s2 3p6',
        'excited_states': ['4s1', '4p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2)]
    },
    19: {
        'name': 'Potassium',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 4s1',
        'excited_states': ['4p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2)]
    },
    20: {
        'name': 'Calcium',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 4s2',
        'excited_states': ['4p2'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2)]
    },
    21: {
        'name': 'Scandium',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d1 4s2',
        'excited_states': ['4p1', '3d2'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)]
    },
    22: {
        'name': 'Titanium',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d2 4s2',
        'excited_states': ['4p1', '3d3'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)]
    },
     23: {
        'name': 'Vanadium',
        'symbol': 'V',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d3 4s2',
        'excited_states': ['4p1', '3d4'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 50.9415, 'density': 6.0}
    },
    24: {
        'name': 'Chromium',
        'symbol': 'Cr',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d5 4s1',
        'excited_states': ['4p1', '3d6'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 51.9961, 'density': 7.19}
    },
    25: {
        'name': 'Manganese',
        'symbol': 'Mn',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d5 4s2',
        'excited_states': ['4p1', '3d6'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 54.938044, 'density': 7.21}
    },
    26: {
        'name': 'Iron',
        'symbol': 'Fe',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d6 4s2',
        'excited_states': ['4p1', '3d7'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 55.845, 'density': 7.87}
    },
    27: {
        'name': 'Cobalt',
        'symbol': 'Co',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d7 4s2',
        'excited_states': ['4p1', '3d8'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 58.933194, 'density': 8.9}
    },
    28: {
        'name': 'Nickel',
        'symbol': 'Ni',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d8 4s2',
        'excited_states': ['4p1', '3d9'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 58.6934, 'density': 8.9}
    },
    29: {
        'name': 'Copper',
        'symbol': 'Cu',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s1',
        'excited_states': ['4p1', '3d11'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 63.546, 'density': 8.96}
    },
    30: {
        'name': 'Zinc',
        'symbol': 'Zn',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2',
        'excited_states': ['4p1', '3d11'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 65.38, 'density': 7.14}
    },
    31: {
        'name': 'Gallium',
        'symbol': 'Ga',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p1',
        'excited_states': ['4p2', '3d11'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 69.723, 'density': 5.91}
    },
    32: {
        'name': 'Germanium',
        'symbol': 'Ge',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p2',
        'excited_states': ['4p3', '3d11'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 72.63, 'density': 5.323}
    },
    33: {
        'name': 'Arsenic',
        'symbol': 'As',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p3',
        'excited_states': ['4p4', '3d11'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 74.921595, 'density': 5.776}
    },
    34: {
        'name': 'Selenium',
        'symbol': 'Se',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p4',
        'excited_states': ['4p5', '3d11'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 78.96, 'density': 4.809}
    },
    35: {
        'name': 'Bromine',
        'symbol': 'Br',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p5',
        'excited_states': ['4p6', '3d11'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (3, 2, -2, -1/2), (3, 2, -2, 1/2)],
        'properties': {'atomic_mass': 79.904, 'density': 3.122}
    },
    36: {
        'name': 'Krypton',
        'symbol': 'Kr',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6',
        'excited_states': ['5s1', '5p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2)],
        'properties': {'atomic_mass': 83.798, 'density': 3.749}
    },
    37: {
        'name': 'Rubidium',
        'symbol': 'Rb',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s1',
        'excited_states': ['5p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (5, 0, 0, -1/2), (5, 0, 0, 1/2)],
        'properties': {'atomic_mass': 85.4678, 'density': 1.532}
    },
    38: {
        'name': 'Strontium',
        'symbol': 'Sr',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s2',
        'excited_states': ['5p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (5, 0, 0, -1/2), (5, 0, 0, 1/2)],
        'properties': {'atomic_mass': 87.62, 'density': 2.64}
    },
    39: {
        'name': 'Yttrium',
        'symbol': 'Y',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d1 5s2',
        'excited_states': ['5p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (5, 0, 0, -1/2), (5, 0, 0, 1/2)],
        'properties': {'atomic_mass': 88.90584, 'density': 4.47}
    },
    40: {
        'name': 'Zirconium',
        'symbol': 'Zr',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d2 5s2',
        'excited_states': ['5p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (5, 0, 0, -1/2), (5, 0, 0, 1/2)],
        'properties': {'atomic_mass': 91.224, 'density': 6.52}
    },
    41: {
        'name': 'Niobium',
        'symbol': 'Nb',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d4 5s1',
        'excited_states': ['5p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (5, 0, 0, -1/2), (5, 0, 0, 1/2)],
        'properties': {'atomic_mass': 92.90637, 'density': 8.57}
    },
    42: {
        'name': 'Molybdenum',
        'symbol': 'Mo',
        'ground_state': '1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s1',
        'excited_states': ['5p1'],
        'quantum_states': [(1, 0, 0, -1/2), (1, 0, 0, 1/2), (2, 0, 0, -1/2), (2, 0, 0, 1/2), (3, 0, 0, -1/2), (3, 0, 0, 1/2), (4, 0, 0, -1/2), (4, 0, 0, 1/2), (5, 0, 0, -1/2), (5, 0, 0, 1/2)],
        'properties': {'atomic_mass': 95.95, 'density': 10.22}
    },
    # Continue adding elements with detailed data...
}

def get_element_data(atomic_number):
    return ELEMENT_DATA.get(atomic_number, None)

def calculate_quantum_states(atomic_number):
    element_data = get_element_data(atomic_number)
    if element_data:
        return element_data['quantum_states']
    return []

def visualize_states(element_data):
    fig, ax = plt.subplots()
    
    ground_state = element_data['ground_state']
    excited_states = element_data['excited_states']
    quantum_states = element_data['quantum_states']
    
    y_vals = [0] * len(quantum_states)
    x_vals = range(len(quantum_states))
    
    labels = [f'n={n}, l={l}, m={m}, s={s}' for (n, l, m, s) in quantum_states]
    
    ax.scatter(x_vals, y_vals, label='Quantum States')
    for i, label in enumerate(labels):
        ax.annotate(label, (x_vals[i], y_vals[i]), textcoords="offset points", xytext=(0,10), ha='center')
    
    ax.set_title(f"{element_data['name']} Quantum States")
    ax.set_xlabel("State Index")
    ax.set_ylabel("Energy Level (Arbitrary Units)")
    plt.xticks(x_vals, labels, rotation='vertical')
    plt.legend()
    plt.tight_layout()
    plt.show()

def main():
    try:
        atomic_number = int(input("Enter the atomic number of the element: "))
        element_data = get_element_data(atomic_number)
        
        if not element_data:
            print("Element data not found. Please try another atomic number.")
            return
        
        print(f"Element: {element_data['name']}")
        print(f"Ground State: {element_data['ground_state']}")
        print(f"Excited States: {', '.join(element_data['excited_states'])}")
        
        quantum_states = calculate_quantum_states(atomic_number)
        if quantum_states:
            visualize_states(element_data)
        else:
            print("No quantum states available for visualization.")
    except ValueError:
        print("Invalid input. Please enter a valid atomic number.")

if __name__ == "__main__":
    main()
