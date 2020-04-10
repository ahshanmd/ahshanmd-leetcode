def PairSumTwoPointers(A, total, sum):
    low = 0
    high = total - 1
    while (low < high):
        if (A[low] + A[high] == sum):
            return True
        elif (A[low] + A[high] < sum):
            low = low + 1
        else:
            high = high - 1
    return False

print(PairSumTwoPointers([1, 2, 4, 7], 4, 6))
