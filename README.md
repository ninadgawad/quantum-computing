## Quantum Computing Algoritms ##


# WHAT: 
#### A quantum computer is a machine that uses quantum mechanics to perform calculations; instead of using bits and logic gates as current compters, quantum computers use qubits and quantum gates. Qubit is a vector of two complex numbers with unit length.

``` python
from pyquil.quil import Program
from pyquil.api import *
from pyquil.gates import *

p1 = Program(H(0), CNOT(0, 1))
qc1 = get_qc('2q-qvm')
results = qc1.run_and_measure(p1, trials=10)
print(list(zip(results[0], results[1])))

p1 = Program(H(1), CNOT(1, 2))
qc1 = get_qc('Aspen-4-2Q-A')
results = qc1.run_and_measure(p1, trials=10)
print(list(zip(results[1], results[2])))

```

[https://www.youtube.com/watch?v=0Eeuqh9QfNI&feature=youtu.be&t=2745]
