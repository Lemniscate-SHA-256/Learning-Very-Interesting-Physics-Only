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
    # Continue adding elements up to 118 (Oganesson) with actual data
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
