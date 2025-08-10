# You need to find the length of the longest run of
#  numbers that are consecutive integers appearing somewhere in the array.

# It doesn’t matter where they appear in the array,
#  just how many consecutive numbers you can chain together from the array elements.

# For example:

# nums = [0, 3, 2, 5, 4, 6, 1, 1]

#     The consecutive numbers you can chain here are: 0, 1, 2, 3, 4, 5, 6

#     Length = 7

# You return 7.






def LCS(nums):

    LS = []
    setNumsList = sorted(list(set(nums)));
    print(setNumsList)
    for i in range(len(setNumsList)):
        if i >= len(setNumsList) - 1:
            LS.append(setNumsList[i])
            break;
        if setNumsList[i]+1 == setNumsList[i+1] or setNumsList[i]-1 == setNumsList[i+1]:
            LS.append(setNumsList[i]);
        else: 
            LS.append(setNumsList[i]);
            print(f"Current Index : {i}")
            print(f"Ls Value During {i}th Iteraiton : {LS}");
            if len(LS) >= ((len(setNumsList)-1)- i):
                return len(LS);
            LS = [];
            continue;

    print(f'LS : {LS}');
    return len(LS);
   # [-9, -7, -4, -3, -1, 2, 3, 4, 5, 7, 8, 9]


  

# res  = LCS([0, 3, 2, 5, 4, 6, 1, 1 , 7 ,15,  8]);

# res  = LCS([9,1,4,7,3,-1,0,5,8,-1,6]);

# res  = LCS([2,20,4,10,3,4,5]);

# res  = LCS([9,1,4,7,3,-1,0,5,8,-1,6]);
# res  = LCS([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]);
# [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]

res  = LCS([-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7]);
print(res)
    
        

         

