


from calendar import c
from re import L


def POAES(nums):
    # hashmap = {};
    # for i , num in enumerate(nums):
    #     hashmap[num] = i;
    # # print(hashmap)
    # i = 0;
    
    # for key , value in hashmap.items():
    #     sum = 
    #     if value == i:
    #         continue;
        
    
    #algorithm 
        # loop over nums
        # for current index, access and multipy all other indexes values.
        # store each index value into a list

    #psuedo COde
    #     result = "";
    #     list
    # for index of every element in nums:
    #     result is equal to sum of num[i+1] , num[i+2] and num[len(num) -1];
    #     append result to the list


    # problem
    # Problem arises when loop reaches index 1 ! the approach becomes invalid
    
    # Trying with two pointer approach
    # low is equal to 0;
    # high is equal to len(nums) -1;
    # index is 0
    # while High is greateer thean low:
    #     when i will be 1 I will continue it and then store the result of 
    #     ohter values. Then i will divide 
    #     for 0 index result will be 96, 96 /2 => 96/2 => 48 saved = 48;
    #     for 1 index reuslt iwll be 48 so no loop iteraiion. 48/2 =24; saved = 24;
    #     for 2 index result will be saved which is 24 , 24/2 is 12 so saved is 12
    #     for 3 index result will be saved which is 12 , here logic breaks cause Real
    #     anwer is 16


    result = 1;
    list = [];
    for i in range(len(nums)):
        print(f"======================={i}th Iteraion Outerloop=======================");
        for j in range(len(nums)):
            print(f"======================={j}th Iteraion Innerloop=======================");
            if j == i:
                continue;
            result = result * nums[j];
        list.append(result);
        result = 1;
    # for i = 0, 2 * 4 * 6;
    # for i = 1; 4 * 6;
    # for i = 2; 6;\
    return list
    # problem skipping of index before the current index
    # so for i = 0 , j = 0 , j==i so continue first iteraion
    # for i = 0 , j = 1 , result = 1 * nums[1] == 1 * 2 = 2;
    # list.append(2)
    # for i = 0 , j = 2 , 



res = POAES([1,2,4,6]);
print(res);
