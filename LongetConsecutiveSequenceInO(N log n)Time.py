
def LCS(nums):

    LS = [];
    StreaksList = [];
    setNumsList = sorted(list(set(nums)));
    print(setNumsList)
    for i in range(len(setNumsList)):
        print(f"=========================Iteration  {i}================================");
        print("\n");
        if i >= len(setNumsList) - 1: # 9
            LS.append(setNumsList[i]);
            print(f"value of Ls in Upper if blockd during {i}th iteration : {LS}");
            StreaksList.append(LS);
            print(f"StreakList Before Breaking: {StreaksList}")
            break;
        if setNumsList[i]+1 == setNumsList[i+1]:
            LS.append(setNumsList[i]);
            print(f"Ls Valie during {i}th Iteration : {LS}" );
            # StreaksList.append(LS);
            print(f"Streaks List so Far : {StreaksList}");
        else: 
            LS.append(setNumsList[i]);
            # print(f"Current Index : {i}")
            print(f"Ls Value During {i}th Iteraiton : {LS}");
            # if len(LS) >= ((len(setNumsList)-1)- i): #9 - 5 for 5th Iteration 
            #     return len(LS);
            StreaksList.append(LS);
            print(f"Streaks List so Far : {StreaksList}");
            LS = [];
            continue;

    print(f'LS : {LS}');
    return max(len(s) for s in StreaksList);
#   [-7, -5, -3, 0, 1, 2, 4, 6, 8, 9]


  

# res  = LCS([0, 3, 2, 5, 4, 6, 1, 1 , 7 ,15,  8]);

# res  = LCS([9,1,4,7,3,-1,0,5,8,-1,6]);

# res  = LCS([2,20,4,10,3,4,5]);

# res  = LCS([9,1,4,7,3,-1,0,5,8,-1,6]);
# res  = LCS([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]);
# [4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]

res  = LCS([-7,2,-3,8,9,0,8,4,-5,8,-5,-5,1,6,4]);
print(res)
