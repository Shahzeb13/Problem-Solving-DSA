def threeSum(nums):
    print("======================Three Sum======================");
    '''
    So ,I have a problem where an array is given to me and i have to return the list of 
    three numbers that Sum is equal to one. 
    ======Brute Force Solution========
    I will have to use three loops in brute force
    loop 1 will iterato from 0 to len(nums);
    loop 2 will 1 from to to len(nums):
    loop 3 will 2 from to len(nums):
    target is zero
    list of lists
    for i in len of nums:
        for j in range between 1 and len(nums):
            for k in range between 2 and len(nums):
                if (k == len(nums) - 1);
                break;
                if nums[i] + nums[j] + nums[k] == 0;
                    list of lists.append ([num[i] , num[j] , num[k]]);
    return list of lists;


    =====dry run ========
    [-1,0,1,2,-1,-4]

    =====first iteration======
    i = -1 , j = 0 , k = 1
    -1 + 0 + 1
    listoflists.appends([-1 , 0 , 1]),
    

    ====2nd=====
    i = -1 , j = 0 , k = 2;
    -1 + 0 + 2
    ====3rd========
    i = -1 , j = 0 , k = -1 
    -1 + 0 -1 = -2
    =====4th=====
    i = -1 , j = 0 , k = -4;
    -1 + 0 -4



    [-1,0,1,2,-1,-4]
    ==== Now J will become index 2
    
    ====5TH Iteraion======
    i = -1 , j = 1 , k = 2
    -1 + 1 + 2

    ====6th iteration ====
    i = -1  j = 1 , k = -1
    -1 + 1 -1

    ======7th iteration =====
    i = -1 , j = 1 , k = -4
    -1+1-4
    
    [-1,0,1,2,-1,-4]
    ===Now j index will become 3====

    =====8th iteration ====
    i = -1 , j = 2 , k = -1
    -1 + 2 -1
    listOflist = [[-1 , 0 , 1],[-1 , 2 , -1]];

    ======= 9th ======
    i = -1 , j = 2 , k = -4
    -1 + 2 - 4
    
    [-1,0,1,2,-1,-4]
    ====Now j will become index 4====

    --------10th iteraion=========
    i = -1 , j = -1 , k = -4;
    -1 -1 -4


    [-1,0,1,2,-1,-4]
    ======Now J ends so i will become index 1=====

    =======11TH iteraion========
    i = 0 , j = 1, k = 2;
    0 + 1 + 2

    ==========12th=======
    i = 0 , j = 1 ; k = -1;
    0 + 1 -1 
    listOflist = [[-1 , 0 , 1],[-1 , 2 , -1] , [ 0 , 1 , -1]];

    =======13th Iteration ===
    i =0 , j = 1 , k = -4
    0 + 1 -4

    ======14th iteriaon=======
    i = 0 , j = 2 , k = -1
    0 + 2 -1

    [-1,0,1,2,-1,-4]
    =======15th iteraion=====
    i = 0 , j = 2 , k = -4;
    0 + 2 -4

    ====16th Iteraion=====
    i = 0; j = -1 , k = -4
    = 0-1+4

    ======17th iteraion=====
    now , i will become index 2 
    i = 1 , j = 2,  k = -1
    1 + 2 -1
    =====18th=======
    i = 1 , j = 2 , k = -4
    1 + 2 -4 
    ======19th========
    now, i will become index 3
    i = 2 ,  j = -1 , k = -4;
    2 -1 -4 
    ========20th iteration ======
     [-1,0,1,2,-1,-4]
     now , i will become index 4
     i = -1 , j = -4


    
    when k inner loop ends , break from the loop



    '''
    


    target = 0;

    list = [];
    n = len(nums);
    for i in range(n -2 ):
        for j in range( i+1  , n - 1 ):
            for k in range(j + 1 , n):
                if nums[i] + nums[j] + nums[k] == target:
                    triplet = sorted([nums[i] , nums[j] , nums[k]])
                    # print(f"before check : {list}");
                    if triplet not in list:
                        list.append(triplet);
                    
    # print(sorted(list))
    return list;




    '''
    [[-1, 0, 1], [-1, 2, -1], [0, 1, -1]]
    
        

    '''

output = threeSum([-1,0,1,2,-1,-4]);
print(output);
