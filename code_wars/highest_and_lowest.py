'''
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
'''

def high_and_low(numbers):
    num_list = numbers.split()
    num_list = [int(num) for num in num_list]
    num_list.sort()

    low_num = num_list[0]
    high_num = num_list[-1]

    # ...
    return f"{high_num} {low_num}"



