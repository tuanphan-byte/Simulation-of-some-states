from qiskit import QuantumCircuit
def create_bell_state(measure=False):
    bell_circuit=QuantumCircuit(2,2 if measure else 0)
    bell_circuit.h(0)
    bell_circuit.cx(0,1)
    if measure:
        bell_circuit.measure([0,1],[0,1])
    return bell_circuit
    