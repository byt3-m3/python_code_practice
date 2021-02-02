'''
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
FUNDAMENTALSARRAYSOBJECTS
'''


def highest_rank(arr):

    arr.sort()

    return max(arr, key=arr.count)


r = highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12])
print(r)
r = highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10])
print(r)

