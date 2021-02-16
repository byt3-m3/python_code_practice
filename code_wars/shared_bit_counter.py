'''
Complete the method that returns true if 2 integers share at least two 1 bits, otherwise return false. For simplicity assume that all numbers are non-negative.

Examples
 7  =  0111 in binary
10  =  1010
15  =  1111

7 and 10 share only a single 1-bit (at index 2) --> false
7 and 15 share 3 1-bits (at indexes 1, 2, and 3) --> true
10 and 15 share 2 1-bits (at indexes 0 and 2) --> true

'''


def dec_to_bin(x):
    return int(bin(x)[2:])

def shared_bits(a, b):

    print(a, b)

    bin_a = f'{a:b}'
    bin_b = f'{b:b}'
    # print(int(bin_a)&int(bin_b))
    print((int(bin_a) & int(bin_b)) % 2)
    if ((int(bin_a) & int(bin_b)) % 2) == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    print(shared_bits(1, 2))
    print(shared_bits(2, 3))
    print(shared_bits(23, 7))
