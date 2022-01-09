from random import getrandbits
from qiskit import QuantumCircuit, execute, Aer

def gen_bits() :
    bits = list()
    for i in range(500) :
        bits.append(str(getrandbits(1)))

    return bits

def gen_bases() :
    bases = list()
    for i in range(500) :
        init = str(getrandbits(1))
        if init == '0' :
            bases.append('Z')
        else : bases.append('X')

    return bases

def encode_bits(bits, bases) :
    encoded_qubits = list()
    for i in range(len(bits)) :
        qc = QuantumCircuit(1,1)
        if bits[i] == '0' :
            if bases[i] == 'Z' :
                pass
            elif bases[i] == 'X' : 
                qc.h(0)
        elif bits[i] == '1' :
            if bases[i] == 'Z' :
                qc.x(0)
            elif bases[i] =='X' :
                qc.x(0)
                qc.h(0)
        encoded_qubits.append(qc)

    return encoded_qubits

def decode_qubits(qubits, bases) :
    bits = list()
    for i in range(len(qubits)) :
        qc = qubits[i]
        if bases[i] == 'Z' :
            qc.measure(0,0)
        elif bases[i] == 'X' :
            qc.h(0)
            qc.measure(0,0)

        job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots = 1)
        results = job.result()
        counts = results.get_counts()
        measured_cbit = max(counts, key=counts.get)

        bits.append(measured_cbit)

    return bits

def compare_bases(bases1, bases2) :
    agreeing_indices = list()
    for i in range(len(bases1)) :
        if bases1[i] == bases2[i] :
            agreeing_indices.append(i)

    return agreeing_indices

def gen_key(bits, indices) :
    key = list()
    for index in indices :
        key.append(bits[index])

    return key