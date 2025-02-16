from random import choice

# Generates a message of 𝑘 bits
def generate_msg(k):
    msg = ''.join(choice(['0', '1']) for _ in range(k))
    return msg

# Calculates the remainder/crc
def calc_rem(a, b):
    rem = a[0:len(b) - 1]
    for i in range(len(a) - len(b) + 1):
        rem += a[i + len(b) - 1]
        if rem[0] == '1':
            rem = ''.join('0' if x == y else '1' for x, y in zip(rem, b))
        rem = rem[1:]
    return rem

# Generates the k + |P| - 1 bit frame T for transmission
def generate_T(M, P):
    rem = calc_rem(M + "0" * (len(P) - 1), P)
    T = ''.join([M, rem])
    return T

# Generates transmission errors at any bit positions of T
def generate_error(frame):
    recv = ''.join('1' if bit == '0' else '0' if bit == '1' and choice([True] + [False] * 15) else bit for bit in frame)
    return recv

# Applies CRC to the received frame to determine if the frame should be accepted or discarded
def check(recv, P):
    if calc_rem(recv, P) == "0" * (len(P)-1):
        return "Accepted"
    return "Discarded"

k = 10
P = "110101"
M = generate_msg(k)
T = generate_T(M, P)
recv = generate_error(T)
flag = check(recv, P)
print(f"Input Message M: {M}")
print(f"Transmission Frame T: {T}")
print(f"Received Frame: {recv}")
print(f"Received Frame Should Be: {flag}")
