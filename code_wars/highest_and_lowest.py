def high_and_low(numbers):
    num_list = numbers.split()
    num_list = [int(num) for num in num_list]
    num_list.sort()

    low_num = num_list[0]
    high_num = num_list[-1]

    # ...
    return f"{high_num} {low_num}"



