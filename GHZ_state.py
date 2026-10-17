from qiskit import QuantumCircuit

def create_ghz_circuit(measure=False):
    ghz_circuit=QuantumCircuit(3, 3 if measure else 0)
    ghz_circuit.h(0)
    ghz_circuit.cx(0,1)
    ghz_circuit.cx(1,2)
    if measure:
        ghz_circuit.measure([0,1,2], [0,1,2])
    return ghz_circuit