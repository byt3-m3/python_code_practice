from collections import namedtuple

circuit = namedtuple('circuit', ['id', 'carrier', 'bw'])


def recursive_search(_list: list, carrier, **kwargs):
    # This is a recursive call
    results = kwargs.get("r_list", [])

    over = kwargs.get("over")
    under = kwargs.get("under")

    if len(_list) > 0:  # Condition checks if the search list is not empty
        ckt = _list.pop()
        if ckt.carrier == carrier:
            if over:
                if ckt.bw > over:
                    results.append(ckt)
            if under:
                if ckt.bw < under:
                    results.append(ckt)

    if len(_list) == 0:  # Condition checks if the search list is empty
        return results

    '''
    
    '''
    return recursive_search(_list, carrier, r_list=results, over=over, under=under)


def iterative_search(_list: list, carrier, **kwargs):
    # This is a iterative call
    results = []
    for ckt in _list:
        if ckt.carrier == carrier:
            results.append(ckt)
    if len(results) > 0:
        return results
    else:
        return None


def main():
    a = circuit(id="1", carrier='clink', bw=100)
    b = circuit(id="2", carrier='clink', bw=250)
    e = circuit(id="3", carrier='clink', bw=50)
    f = circuit(id="3", carrier='clink', bw=35)
    c = circuit(id="3", carrier='wstream', bw=350)
    d = circuit(id="4", carrier='wstream', bw=450)

    my_list = [a, b, c, d, e, f]

    r_results = recursive_search(my_list, 'clink', under=55)
    print(r_results)
    if r_results is not None:
        print(len(r_results))

    # i_results = iterative_search(my_list, 'clink')
    # print(i_results)
    # if i_results is not None:
    #     print(len(i_results))


if __name__ == "__main__":
    main()
