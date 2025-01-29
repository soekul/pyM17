from m17.misc import print_4bits, print_bits, print_8bits, print_16bits


def test_b(x):
    """
    Test the binary print functions
    :param x: number to test

    """
    print(print_4bits(int(x)))
    print(print_bits(int(x)))
    print(print_8bits(int(x)))
    print(print_16bits(int(x)))
