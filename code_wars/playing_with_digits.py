def main():
    pass


def dig_pow(n, p):
    num_list = [d for d in str(abs(n))]

    total = 0
    for i, v in enumerate(num_list):
        k = i + p
        total += pow(int(v), k)

    sum_t = total // n

    if total == n * sum_t:
        return abs(sum_t)

    return -1


if __name__ == "__main__":
    # print(8 ** 1)
    # print(9 ** 2)
    # res = dig_pow(89, 1)
    # dig_pow(695, 2)
    # dig_pow(92, 1)
    # res = dig_pow(46288, 3)
    res = dig_pow(92, 1)
    print(res)
