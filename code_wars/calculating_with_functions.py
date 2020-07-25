'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Divison should be integer division. For example, this should return 2, not 2.666666...:
'''


def _process(data, base):
    num = data[0]
    oper = data[1]
    if oper == "*":
        return base * num

    if oper == "/":
        return base // num

    if oper == "+":
        return base + num

    if oper == "-":
        return base - num


def zero(data=None):
    if isinstance(data, tuple):
        return _process(data, 0)

    return 0


def one(data=None):
    if isinstance(data, tuple):
        return _process(data, 1)

    return 1


def two(data=None):
    if isinstance(data, tuple):
        return _process(data, 2)

    return 2


def three(data=None):
    if isinstance(data, tuple):
        return _process(data, 3)

    return 3


def four(data=None):
    if isinstance(data, tuple):
        return _process(data, 4)

    return 4


def five(data=None):
    if isinstance(data, tuple):
        return _process(data, 5)

    return 5


def six(data=None):
    if isinstance(data, tuple):
        return _process(data, 6)

    return 6


def seven(data=None):
    if isinstance(data, tuple):
        return _process(data, 7)

    return 7


def eight(data=None):
    if isinstance(data, tuple):
        return _process(data, 8)

    return 8


def nine(data=None):
    if isinstance(data, tuple):
        return _process(data, 9)

    return 9


def plus(num):
    return (num, "+")


def minus(num):
    return (num, "-")


def times(num):
    return (num, "*")


def divided_by(num):
    return (num, "/")


result_1 = one(minus(five()))
result_2 = five(times(seven()))
print(result_1)
print(result_2)
