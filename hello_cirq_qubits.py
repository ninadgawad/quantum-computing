### Reference: https://www.youtube.com/watch?v=16ZfkPRVf2w

import cirq

circuit = cirq.Circuit();
(q0 ,q1) = cirq.LineQubit.range(2);

circuit.append([cirq.H(q0), cirq.CNOT(q0, q1)])
circuit.append([cirq.measure(qo), cirq.measure(q1)])

sim = cirq.Simulator()
results = sim.run(circuit, repetitions=10)
print(results)



### Run as python
### python hello_qubits.py
###  
### 0 = 1100010001
### 1 = 1100010001 
