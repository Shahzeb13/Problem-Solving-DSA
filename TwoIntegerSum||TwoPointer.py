def TwoIntegerSum2(numbers , target):
    print("==========TwoIntegerSum2===========");
    '''
    ===problem===
    So, i have an array and a target! I have to return the indeces of the 1-index array of the two nums that matches the target

    Constraints:

    2 <= numbers.length <= 1000
    -1000 <= numbers[i] <= 1000
    -1000 <= target <= 1000

    I can use brute force solution here 
    The element of the array can be negative/positive
    The Target can also be negative/positive

    I will aim for O(n log n ) or O(n) soluton after bruteforce

    ===pseudo Code===
    for i in range(len(numbers)):
        for j in range(i+1 , len(numbers));
            if numbers[i] + numbers[j] == target;
            return [i+1 , j+1]


    ===dry run===

     [-10, -3, 0, 2, 5, 8, 12]

    Iteration    i      j       i[val]     j[val]     sum            target is -5

        I don't wanna waste my time doing brute force! I know how it works  

    '''
    # #implemenentation of bruteforce
    # for i in range(len(numbers)):
    #     for j in range(i+1 , len(numbers)):
    #         if numbers[i] + numbers[j] == target:
    #             return [i+1 , j+1]


    '''
    Using TwoPointer Technique

    ===PsuedoCode===
    low is 0
    high is len(numbers) -1;
    
    while high > low:
        currentSum = numbers[low] + numbers[high];
        if currentSum == target:
            return [low + 1 , high + 1]
        if currentSum < target:
            low +=1;
        else:
            high -=1







    '''

    #Implementation 

    low = 0;
    high = len(numbers) -1;
    
    while high >low:
        curr = numbers[low] + numbers[high];
        if curr == target:
            return [low + 1 , high + 1];
        if curr < target:
            low += 1;
        else:
            high -= 1;



output = TwoIntegerSum2([-7 ,1,2 ,3,4], 7);
print(output);
