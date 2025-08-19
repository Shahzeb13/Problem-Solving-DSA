def threeSum(nums):
    '''
    low is -1 
    high is -4 
    
    fixed = 0 index = -1 
    low = fixed + 1 = 0
    high = len(NUMS) - 1 = -4
    


    move low = 1
    -1 + 1 + (-4)
    move low = 2
    ml 3
    -1 , 2 , -4
    ml 4 
    -1 , -1 , -4


    new approach 
    I need to compare 3 numbers and then sum them and check if they are equal to zero
    if they are then i will add them into the list


    sorting makes two pointer easy 
    [-4, -1, -1, 0, 1, 2]

    so i nned to fix the first pointer from 0th index to n-2 index


    ======psuedo code=====
    n = len(nums);
    uniqueTriplets = [];
    for i in range(0 , n-2);
        fixed = nums[i];
        low = fixed + 1;
        high = len(nums) - 1;
        while high > low:
            currentSum = num[low] + nums[high] + nums[fixed];
            if currentSum== 0;
                triplet = sorted([num[low] , nums[high] , nums[fixed]])
                if triplet not in list:
                    uniqueTriplets.append(triplet);
            if currentSum < target:
                low +=1;
            elif currentSum > target:
                high +=1;
    return  uniqueTriplets;

    [-1,0,1,2,-1,-4]
    ====dry run====
        for i = 0;
    Iteration 0 :  fixed: -1 , low = 0 , high = -4  UT = []
    iteraion 1 :    fixed -1: low = 1 , high = -4 UT = []
    iteraion 2 : fixed : -1 ,  low = 2 , high = -4 UT = []
    iteratio 3: fixed : -1 , low = -1, high = -4  UT = []
        for i = 1
    Itr 5 : fixed : 0 , low = 1 , high = -4 UT = []
    itr 6 : fixed : 0 , low = 2 , high = -4  UT = []
    Itr 7 : fixed : 0 , low = -1 , high = -4 UT = []
    
        for i = 2
     Itr 8 : fixed : 1 , low = 2 , high = -4 UT = []
    itr 9 : fixed : 1 , low = -1 , high = -4  UT = []
    Itr 10 : fixed : 1 , low = -1 , high = -4 UT = []

          for i = 3
     Itr 8 : fixed : 2 , low = 2 , high = -4 UT = [[2 , 2 , -4]]
    itr 9 : fixed : 2 , low = -1 , high = -4  UT = []
    Itr 10 : fixed : 2 , low = -1 , high = -4 UT = []



    '''
    # sortedNums = sorted(nums);
    # # print(sortedNums);
    nums.sort();
    # print(nums)
    n = len(nums);
    uniqueTriplets = [];
    target = 0;
    for i in range(0 , n-2):
        
        
        if i>0 and nums[i] ==  nums[i-1]:
            continue;
        fixed = nums[i];  # Fixed: Get the value, not the index
        low = i + 1;
        high = len(nums) - 1;
        while high > low:
            currentSum = nums[low] + nums[high] + fixed;
            if currentSum == 0:
                triplet = sorted([nums[low] , nums[high] , fixed])
                if triplet not in uniqueTriplets:
                    uniqueTriplets.append(triplet);
                low +=1;
                high -=1;
            if currentSum < target:
                low +=1;
            elif currentSum > target:
                high -=1;
    return  uniqueTriplets;

'''
[-4, -1, -1, 0, 1, 2]

Itr  fixed   low   high    UT                  Sum
0     -4      -1    2       []                  -3
1     -4      -1    2       []                  -3
2     -4       0    2       []                  -2
3     -4       1    2       []             -    -1          while loop terminates
4     -1      -1    2       [[-1 , -1 , 2]]      0
5     -1       0    2                            1
6     -1       0     1      [[-1 ,-1 ,2],[-1,0,1]]   0       while loop terminates
7     -1       0     2     [[-1 , -1 ,2 ,[-1,0 ,1]]] 0       while loop terminates


'''
    
output = threeSum([-1,0,1,2,-1,-4]);
print(output)
