
from collections import defaultdict
from multiprocessing import Value


def TopKElem(nums , K):
    groups = defaultdict(list)
    freq = {}
    for num in nums:
        groups[num].append(num)
    print(f"Groups : {groups}")
    # numsValues = list(groups.values())
    # return groups;
    for key in groups:
        freq[key] = len(groups[key])
    print(f"freq : {freq}")

    res = []
    Extracted = []

    for i in range(K):
        print(f"------------------{i}th iteration ------------------------- ")
        currentLargestKeyFreq = -1;
        currentlargestKey = None
        
        for key in freq:
            print(f"-------------------------------Key {key} Iteration------------------------------------")
            if key not in Extracted and freq[key] > currentLargestKeyFreq:
                print("If successfull.")
                currentLargestKeyFreq = freq[key]
                currentlargestKey = key;

        if currentlargestKey is not None:
            res.append(currentlargestKey);
            print(f" Result List During {i}th Iteration of outerloop : {res}")
            Extracted.append(currentlargestKey);
            print(f" Result List During {i}th Iteration of outerloop : {Extracted}")
    
    return res


res = TopKElem([1, 2, 3], 5)
print(res)





# def my_counter(nums):
#     freq = {}  # Step 1: empty dictionary
#     for num in nums:  # Step 2
#         if num in freq:  # Step 3
#             freq[num] += 1
#         else:  # Step 4
#             freq[num] = 1
#     return freq






# 1 [1:1 , 2 : 2 , 3 : 3]
# Check and extract the largest one first and then keep track of it to avoid redoing iter
# Extracted = []
# compare the value of each key to the largest predefined
# currentLargest= -1 then compare each of freq values to the currentLargest

