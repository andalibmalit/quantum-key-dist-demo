# quantum-key-dist-demo

This is a demo of the [quantum key distribution protocol](https://en.wikipedia.org/wiki/Quantum_key_distribution), implemented in Python using the Qiskit library. When running the program, the user is given the option to simulate an eavesdropper attempting an intercept-and-resend attack on the communications channel. 

The QKD protocol we will implement has the following steps:
1. The sender, Alice, generates a list of random bits, and another of random bases (either Z or X).
2. Alice encodes her bits as qubits using the bases she generated.
3. The receiver, Bob, generates his own random bases and measures Alice's qubits into his own list of classical bits.
4. Alice and Bob compare their bases, and extract a list of indices of matching bases.
5. The bits at the index of each matching basis are compared, and will either match (meaning the channel is secure) or not (implying an eavesdropper).

If the bits at said indices do not match, this means the qubits' state must have been changed in transit by someone attempting to measure them - AKA Eve, the eavesdropper. 