from qkd_fns import *

def secure_channel() :
    # 1. Generate bits Alice will send to Bob.
    print("Generating Alice's bits...")
    alice_bits = gen_bits()
    # 2. Generate bases Alice will use to encode her bits.
    print("Generating Alice's bases...")
    alice_bases = gen_bases()
    # 3. Encode bits to send to Bob.
    print("Encoding bits and send qubits to Bob...")
    encoded_qubits = encode_bits(alice_bits, alice_bases)
    # 4. In this step, the qubits are sent to Bob via fiber optics.
    #    Bob now has the qubits.
    # 5. Generate bases Bob will use to measure the qubits.
    print("Generating Bob's bases...")
    bob_bases = gen_bases()
    # 6. Bob measures Alice's qubits to decode them, using his bases.
    print("Bob decoding qubits...")
    bob_bits = decode_qubits(encoded_qubits, bob_bases)
    # 7. Alice and Bob compare their bases.
    print("Comparing Alice's and Bob's bases...")
    agreeing_indices = compare_bases(alice_bases, bob_bases)
    # 8. Create Alice's key.
    print("Generating Alice's key...")
    alice_key = gen_key(alice_bits, agreeing_indices)
    # 9. Create Bob's key.
    print("Generating Bob's key...")
    bob_key = gen_key(bob_bits, agreeing_indices)
    # 10. If Alice's and Bob's keys match, the communcations channel is secure.
    print("Comparing Alice's and Bob's keys...")
    if alice_key == bob_key :
        print("Secure channel established.")
    # The following block should never run.
    else :
        print("ALERT - eavesdropper detected!")

def insecure_channel_eavesdropper() :
    # The first part of this simulation is identical to the previous one.
    print("Generating Alice's bits...")
    alice_bits = gen_bits()
    
    print("Generating Alice's bases...")
    alice_bases = gen_bases()

    print("Encoding bits and send qubits to Bob...")
    encoded_qubits = encode_bits(alice_bits, alice_bases)

    # Uh-oh - Eve will now intercept Alice's qubits!
    print()
    print("Eve intercepting qubits!")
    eve_bases = gen_bases()
    eve_bits = decode_qubits(encoded_qubits, eve_bases)
    print()
    # The qubits now continue on their way to Bob after Eve's measurements in an attempt to eavesdrop.

    print("Generating Bob's bases...")
    bob_bases = gen_bases()

    print("Bob decoding qubits...")
    bob_bits = decode_qubits(encoded_qubits, bob_bases)

    print("Comparing Alice's and Bob's bases...")
    agreeing_indices = compare_bases(alice_bases, bob_bases)

    print("Generating Alice's key...")
    alice_key = gen_key(alice_bits, agreeing_indices)

    print("Generating Bob's key...")
    bob_key = gen_key(bob_bits, agreeing_indices)

    # Here, Alice's and Bob's keys should NOT match.
    print("Comparing Alice's and Bob's keys...")
    # This block should never run.
    if alice_key == bob_key :
        print("Secure channel established.")
    else :
        print("ALERT - eavesdropper detected!")

cond = True
while cond :
    choice = input("Type '1' to simulate a secure channel, and '2' to simulate an insecure channel with an eavesdropper: ")
    if choice == '1' :
        secure_channel()
        cond = False
    elif choice == '2' :
        insecure_channel_eavesdropper()
        cond = False
    else :
        print("Invalid input! Please try again.")