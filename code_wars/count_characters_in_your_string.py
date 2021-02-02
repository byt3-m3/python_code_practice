'''
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''


def count(string):
    # The function code should be here
    data = {}
    for char in string:
        data[char] = string.count(char)

    return data


print(count('aba'))


'''
Results 

Time: 596ms Passed: 104 Failed: 0
Test Results:
 Basic Tests
 should give empty dictionary if string is empty
 should get as a result two A characters
 should get as a result of two a characters and two b characters
 should get as a result of two a characters and two b characters, showing that the result order does not matter
 Random Tests
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
Test Passed
You have passed all of the tests! :)
'''