import sys

def maxSum(arr, n, k):
    # Initialize result
    max_sum = -sys.maxsize

    # Consider all blocks starting with i.
    for i in range(n - k + 1):
     # 5 - 3 + 1 = 3                so i and j range are the same o to 3
    #  [5, 2, -1, 0, 3]
    #so range becomes  0 to 2
    # runs for three iterations
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]
#dry run
	'''
     outer   lnner        val[i]      val[j]          currentSum
        0      0             5           5                0 + 5 = 5
        0      1             5           2                5 + 2 = 7
        0      2             5          -1                7 + -1 = 6
        1      0             2           5                 0 + 2 = 2
        1      1             2           2                  2-1  = 1
        1      2             2          -1                  1 + 0 = 1
        




    '''
  
        # Update result if required.
        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3]
    k = 3
    n = len(arr)
    print(maxSum(arr, n, k))
