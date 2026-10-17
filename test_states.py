import numpy as np
from qiskit.quantum_info import Statevector

from Bell_state import create_bell_state
from GHZ_state import create_ghz_circuit
from W_state import create_w_circuit

def test_bell_state():
    qc=create_bell_state(measure=False)
    state=Statevector.from_instruction(qc)
    expected=np.zeros(4)
    expected[0]=1/np.sqrt(2)
    expected[3]=1/np.sqrt(2)
    assert np.allclose(state.data, expected), "Bell State Test: ERROR"
    print("Bell State Test: PASSED")
def test_ghz_state():
    qc=create_ghz_circuit(measure=False)
    state=Statevector.from_instruction(qc)
    expected=np.zeros(8)
    expected[0]=1/np.sqrt(2)
    expected[7]=1/np.sqrt(2)
    assert np.allclose(state.data, expected), "GHZ State Test: ERROR"
    print("GHZ State Test: PASSED")
def test_w_state():
    qc=create_w_circuit(measure=False)
    state=Statevector.from_instruction(qc)
    expected=np.zeros(8)
    expected[1]=1/np.sqrt(3)
    expected[2]=1/np.sqrt(3)
    expected[4]=1/np.sqrt(3)
    assert np.allclose(state.data, expected), "W State Test: ERROR"
    print("W State Test: PASSED")
if __name__ == "__main__":
    print("Đang chạy các bài kiểm tra Statevector...\n")
    test_bell_state()
    test_ghz_state()
    test_w_state()
    print("\nHoàn thành mô phỏng")