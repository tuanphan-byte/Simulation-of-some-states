import numpy as np
from qiskit import QuantumCircuit

def create_w_circuit(measure=False):
    qc = QuantumCircuit(3, 3 if measure else 0)
    qc.ry(2 * np.arccos(1/np.sqrt(3)), 0)
    qc.ch(0, 1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.x(0)
    
    if measure:
        qc.measure([0, 1, 2], [0, 1, 2])
    return qc