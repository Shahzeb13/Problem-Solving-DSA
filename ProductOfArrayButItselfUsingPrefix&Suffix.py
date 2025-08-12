


import array
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

# when i = 0 i have to run all the iteraion of j to store the intitial value of reWork 
# after that when i = 1, 2 and so on ! i need to calcualte the rework value by divding it by 2 , j will urn only once to append
# the value of rework to the list
# for e
    # result = 1;
    # list = [];
    # rework = 2;
    # for i in range(len(nums)):
        
    #     print(f"======================={i}th Iteraion Outerloop=======================");
    #     for j in range(len(nums)):
    #         print(f"======================={j}th Iteraion Innerloop=======================");
    #         # if j==0:
    #         #     list.append(reWork);
                
    #         #     continue;
    #         reWork = rework / 2;
    #         list.append(reWork);
            
    #         if j == i:
    #             continue;
             
    #         result = result * nums[j];
    #     reWork = result;
        # list.append(result);
        # [1,2,4,6]
    # for i = 0, 2 * 4 * 6;
    # for i = 1; 4 * 6;
    # for i = 2; 6;\
    # return list
    # problem skipping of index before the current index
    # so for i = 0 , j = 0 , j==i so continue first iteraion
    # for i = 0 , j = 1 , result = 1 * nums[1] == 1 * 2 = 2;
    # list.append(2)
    # for i = 0 , j = 2 , 

    #Trying to optimize 
    # in frist iteration when 1 , I can save the value of result
    # in 2nd iteraion I will save the reult/2 which becomes 24 in currentRes and for 2nd itertion Instead of relooping i will juss
    #  use the current result and save it in the list as the answer for the second loop is 24
    #  in 3rd iteraion I will again divide the current reult by dividing the res/2 and it will become 12 which is the answer for the third loop and
    #  save it in the list
    #  in 4th loop again again curretn result wil become 6 here my logic fails because the result i want is 8;


    #Trying Two pass technique

    prefix = [];
    prefix.append(1); 
    # for index , num in enumerate(nums):
    for i  in range(1 , len(nums)):
        prefix.append(prefix[i-1] * nums[i-1]);
    # return prefix;
            
    print(f"Prefix : {prefix}");

    suffix = [];
    n=len(nums);
    suffix = [1] * n;
    for i in range(len(nums) -2, -1, -1 ):
        print(f"Iteraion No : {i}")
        suffix[i] = suffix[i+1] * nums[i+1];
    print(f"Suffix : {suffix}");
    
    return [(a*b) for a , b in zip(prefix , suffix)];
#    for i = 0 , prefix is hardcoded into prefix array [1]
#    for i = 1; prefix is  i-1 in python points to last elem so 1 is our last and first elem in this case. [1 , 1] 1*1
#    for i = 2,  prefix[2-1] + num[2-1]  == prefix[1] * nums[1] = 1 * 2 =23 so [1 , 1, 2]


res = POAES([1,2,4,6]);
print(res);
