# Quantum Computing 
A quantum computer is a machine that uses quantum mechanics to perform calculations; instead of using bits and logic gates as current compters, quantum computers use qubits and quantum gates. Qubit is a vector of two complex numbers with unit length.

Quantum computing is a revolutionary technology that leverages the principles of quantum mechanics to process information. 
Unlike classical computers, which use bits as the smallest unit of data (either 0 or 1), quantum computers use quantum bits or qubits. 
Qubits can exist in multiple states simultaneously due to superposition, and they can be entangled, enabling complex computations at unprecedented speeds.

## Benefits
Quantum computing holds the promise of solving certain problems much faster than classical computers. This includes tasks like cryptography, where it can potentially break current encryption methods, and optimization problems, which are prevalent in various industries. Quantum computers can also simulate quantum systems accurately, making them invaluable for scientific research and material science.

## Areas where Quantum Computing can help: 
- Optimization/Financial Modeling/Climate Modeling
- Chemistry 
- Encryption/Cryptography
- Security
- Operations
- Artificial Intelligence

## Why Quantum Computing work? 
- Superposition    
- Entanglement

## What can we do with Quantum Computers ? 
We can write algorithms using Quantum Computers to solve these complex problems which work on 2^N qbit scale to solve the problems 

## Quantum supremacy
John Preskill has introduced this term *quantum supremacy* to refer to the hypothetical speedup advantage that a quantum computer would have over a classical computers.

# Language and Tools

## Q# ("Q" Sharp)
Q# (pronounced "Q sharp") is a domain-specific programming language developed by Microsoft for quantum computing. It is designed to be used for writing quantum algorithms, simulating quantum systems, and compiling quantum programs for execution on a quantum computer or quantum simulator.

Here is a simple example of quantum code in Q#, a quantum programming language developed by Microsoft:

```scss
operation BellStatePrep () : Unit {
    using (qubits = Qubit[2]) {
        H(qubits[0]);
        CNOT(qubits[0], qubits[1]);
    }
}
```
scss
Copy code
operation BellStatePrep () : Unit {
    using (qubits = Qubit[2]) {
        H(qubits[0]);
        CNOT(qubits[0], qubits[1]);
    }
}
This code prepares the quantum state known as a Bell state, which is a type of entangled state often used in quantum computing experiments and quantum communication protocols. The code uses two qubits, and applies a Hadamard gate (H) to the first qubit followed by a controlled-NOT (CNOT) gate on both qubits.

## Cirq
Cirq is a software library for writing, manipulating, and optimizing quantum circuits and then running them against quantum computers and simulators. Cirq attempts to expose the details of hardware, instead of abstracting them away, because, in the Noisy Intermediate-Scale Quantum *(NISQ)* regime, these details determine whether or not it is possible to execute a circuit at all.

## Qiskit 
Qiskit is an open-source framework for working with quantum computers at the level of circuits, pulses, and algorithms.
A central goal of Qiskit is to build a software stack that makes it easy for anyone to use quantum computers. However, Qiskit also aims to facilitate research on the most important open issues facing quantum computation today.


### Qiskit Modules ###
![Qiskit](https://github.com/ninadgawad/QuantumAlgorithm/blob/master/Qiskit.png)


## Things to Learn 
1. Quantum Gates and Circuits
2. Qubits, Bloch Sphere and Basis States 
3. Bernstein-Vazirani Algorithm 
4. Multiple Qubits and Entanglement 


## Key features
- Superposition: The ability of a quantum bit (qubit) to exist in multiple states simultaneously.
- Entanglement: The phenomenon where the state of one qubit is correlated with the state of another, even at great distances.
- Interference: The ability of quantum systems to interfere with each other, which can be harnessed for quantum algorithms.
- Amplitude amplification: A technique used in quantum algorithms to amplify the probability of the desired outcome.
- Quantum parallelism: The ability of a quantum computer to perform multiple calculations at once, due to the superposition and entanglement of qubits.
- Quantum tunneling: The ability of quantum systems to tunnel through potential barriers, which can be used for quantum optimization algorithms.
- No cloning theorem: The principle that it is impossible to perfectly copy an unknown quantum state, which has implications for quantum cryptography.

## Benefits of Quantum Computing
Quantum computing could contribute greatly to the fields of security, finance, military affairs and intelligence, drug design and discovery, aerospace designing, utilities (nuclear fusion), polymer design, machine learning, artificial intelligence (AI), Big Data search, and digital manufacturing. 
Quantum computers could be used to improve the secure sharing of information. Or to improve radars and their ability to detect missiles and aircraft. Another area where quantum computing is expected to help is the environment and keeping water clean with chemical sensors.
Here are some potential benefits of quantum computing:
Financial institutions may be able to use quantum computing to design more effective and efficient investment portfolios for retail and institutional clients. They could focus on creating better trading simulators and improve fraud detection.
The healthcare industry could use quantum computing to develop new drugs and genetically-targeted medical care. It could also power more advanced DNA research.
For stronger online security, quantum computing can help design better data encryption and ways to use light signals to detect intruders in the system.
Quantum computing can be used to design more efficient, safer aircraft and traffic planning systems.
40%


### Quantum Encryption and Decryption with Qiskit
```python
# Importing necessary libraries from Qiskit
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Define the quantum circuit for encryption
def quantum_encryption():
    # Create a Quantum Circuit with 1 qubit and 1 classical bit
    circuit = QuantumCircuit(1, 1)
    
    # Apply Hadamard gate to create superposition
    circuit.h(0)
    
    # Measure the qubit
    circuit.measure(0, 0)
    
    return circuit

# Define the quantum circuit for decryption
def quantum_decryption(circuit):
    # Create a Quantum Circuit with 1 qubit and 1 classical bit
    decrypt_circuit = QuantumCircuit(1, 1)
    
    # Apply Hadamard gate to decode the superposition state
    decrypt_circuit.h(0)
    
    # Measure the qubit
    decrypt_circuit.measure(0, 0)
    
    return decrypt_circuit

# Encrypt the message
encryption_circuit = quantum_encryption()

# Print the encryption circuit
print("Encryption Circuit:")
print(encryption_circuit.draw())

# Decrypt the message (using the same circuit here for simplicity)
decryption_circuit = quantum_decryption(encryption_circuit)

# Print the decryption circuit
print("Decryption Circuit:")
print(decryption_circuit.draw())

# Simulate the encryption circuit
backend = Aer.get_backend('qasm_simulator')
tqc = transpile(encryption_circuit, backend)
qobj = assemble(tqc)
encryption_result = execute(encryption_circuit, backend, shots=1024).result()
encryption_counts = encryption_result.get_counts()

# Simulate the decryption circuit
decryption_result = execute(decryption_circuit, backend, shots=1024).result()
decryption_counts = decryption_result.get_counts()

# Plot the results
print("Encryption Counts:")
print(encryption_counts)
plot_histogram(encryption_counts)
plt.title("Encryption Results")
plt.show()

print("Decryption Counts:")
print(decryption_counts)
plot_histogram(decryption_counts)
plt.title("Decryption Results")
plt.show()

```


### BB84 Example with Python Code (Using Simulated Qubits)
BB84 is a quantum key distribution protocol that uses the unique properties of quantum mechanics to establish a secure key between two parties. 
It ensures that any eavesdropping attempt can be detected, providing a robust foundation for secure communication in the quantum age.

```python
import numpy as np

# Function to encode a bit using a given basis
def encode_bit(bit, basis):
    if basis == 'rectilinear':
        return '0' if bit == 0 else '1'
    elif basis == 'diagonal':
        return '+' if bit == 0 else '-'

# Function to measure a qubit using a given basis
def measure_qubit(qubit, basis):
    if basis == 'rectilinear':
        return 0 if qubit in ['0', '+'] else 1
    elif basis == 'diagonal':
        return 0 if qubit in ['0', '+'] else 1

# Simulate Alice's bit and basis selection
np.random.seed(42)
alice_bits = np.random.randint(2, size=10)
alice_bases = np.random.choice(['rectilinear', 'diagonal'], size=10)

# Alice encodes the bits into qubits
alice_qubits = [encode_bit(bit, basis) for bit, basis in zip(alice_bits, alice_bases)]

# Simulate Bob's basis selection
bob_bases = np.random.choice(['rectilinear', 'diagonal'], size=10)

# Bob measures the qubits
bob_results = [measure_qubit(qubit, basis) for qubit, basis in zip(alice_qubits, bob_bases)]

# Announce and compare bases
matching_indices = [i for i in range(10) if alice_bases[i] == bob_bases[i]]
shared_key = [alice_bits[i] for i in matching_indices]

print(f"Alice's bits:       {alice_bits}")
print(f"Alice's bases:      {alice_bases}")
print(f"Bob's bases:        {bob_bases}")
print(f"Bob's measurement:  {bob_results}")
print(f"Matching indices:   {matching_indices}")
print(f"Shared key:         {shared_key}")

```


# Reference:
- [Quantum Computing](https://en.wikipedia.org/wiki/Quantum_computing)
- [Q#](https://azure.microsoft.com/en-us/resources/development-kit/quantum-computing/#overview)
- [Cirq](https://cirq.readthedocs.io/en/stable/index.html)
- [Qiskit](https://qiskit.org/documentation/index.html)
- [Beginner’s Guide To Quantum Computing](https://www.youtube.com/watch?v=JRIPV0dPAd4)
- [Qiskit Developer](https://developer.ibm.com/depmodels/quantum-computing/projects/qiskit)
- [Qiskit Textbook Link](https://qiskit.org/textbook/preface.html)

# Latest News
12/29/2021 - [Research opens the door to fully light based quantum computing](https://www.tomshardware.com/news/research-opens-the-door-to-fully-light-based-quantum-computing)

08/28/2022 - [Investopedia Quantum Computing](https://www.investopedia.com/terms/q/quantum-computing.asp)
