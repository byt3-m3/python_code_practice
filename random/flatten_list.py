import itertools

import timeit
from decimal import Decimal
list_1 = ["a", "b", "c", "b"]
list_2 = [1, 2, 3, 4]

complex_list = [[1, 2, 3, 4], [1, 2, 3], [1, 2]]


def method_1():
    new_list = []
    for z in complex_list:
        if len(z) > 0:
            for y in z:
                if y not in new_list:
                    new_list.append(y)


def method_2():
    new_list = list(itertools.chain.from_iterable(complex_list))

    no_dups = []
    for i in new_list:
        if no_dups.count(i) == 0:
            no_dups.append(i)

    # print(no_dups)


def main():
    """
    In this example we will be taking a complex list that is composed of multiple list, flatten it and remove any
    duplicates.


    """







    res_1 = timeit.timeit('method_1()', setup='from flatten_list import method_1', number=100000)
    res_2 = timeit.timeit('method_2()', setup='from flatten_list import method_2', number=100000)
    print(f'{res_1: 2f}')
    # print(res_2)
    # # print(method_2())
    #
    # print(Decimal("2.5e-8"))

if __name__ == "__main__":
    main()
