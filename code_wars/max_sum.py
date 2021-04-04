def max_sequence(arr):
    num_set = set()
    for i in arr:
        num_set.add(i)

    

    return sum(num_set)


res = max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# res = max_sequence([4, -1, 2, 1])
print(res)