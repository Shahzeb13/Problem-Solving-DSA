


def containerWithMostWater(heights):
    print("=====================Container With Most Water==========================")
    '''
    =======Psuedo code======
    ContainersAreas = [];
    for i in range(len(heights)):
        for j in range(i + 1 , len(heights)):
            currentHeight is min(heights[j] , heights[i]);
            currentWidth is  j - i;
            currentContainerArea = currentHeight * currentWidth;
            append the current area ito containerAreas list

    return the max(ContainersAreas);


    =====dry run======                                  height = min(v1 , v2)     width = index of j  - index of i
    [1,7,2,5,4,7,3,6]
    
    Iteration    index(i)   nextIndex(j)    value(i)  nextvalue(j)          height     width       Area     containerArea
        0          0           1              1             7                  1          1         1         [1] 
        1          0           2              1             2                  1          2         2         [1,2]
        2          0           3              1             5                  1          3         3         [1,2,3]
        3          0           4              1             4                  1          4         4         [1,2,3,4]
        4          0           5              1             7                  1          5         5         [1,2,3,4,5]
        5          0           6              1             3                  1          6         6         [1,2,3,4,5,6]
        6          0           7              1             6                  1          7         7         [1,2,3,4,5,6,7]
        7          1           2              7             2                  2          1         2         [1,2,3,4,5,6,7,2]
        8          1           3              7             5                  5          2         10        [1,2,3,4,5,6,7,2,10]
        9          1           4              7             4                  4          3         12        [1,2,3,4,5,6,7,2,10,12]
        10         1           5              7             7                  7          4         28        [1,2,3,4,5,6,7,2,10,12,28]
        11         1           6              7             3                  3          5         15        [1,2,3,4,5,6,7,2,10,12,28,15]
        12         1           7              7             6                  6          6         36        [1,2,3,4,5,6,7,2,10,12,28,15,36]
        13         2           3              2             5                  2          1         2         [1,2,3,4,5,6,7,2,10,12,28,15,36,2]
        14         2           4              2             4                  2          2         4         [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4]
        15         2           5              2             7                  2          3         6         [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6]
        16         2           6              2             3                  2          4         8         [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8]
        17         2           7              2             6                  2          5         10        [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10]
        18         3           4              5             4                  4          1         4        [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4]
        19         3           5              5             7                  5          2         10        [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4,10]
        20         3           6              5             3                  3          3         9         [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4,10,9]
        21         3           7              5             6                  5          4         20        [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4,10,9,20]
        22         4           5              4             7                  4          1         4         [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4,10,9,20,4]
        23         4           6              4             3                  3          2         6         [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4,10,9,20,4,6]
        24         4           7              4             6                  4          3         12        [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4,10,9,20,4,6,12]
        25         5           6              7             3                  3          1         3         [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4,10,9,20,4,6,12,3]
        26         5           7              7             6                  6          2         12        [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4,10,9,20,4,6,12,3,12]
        27         6           7              3             6                  3          1         3         [1,2,3,4,5,6,7,2,10,12,28,15,36,2,4,6,8,10,4,10,9,20,4,6,12,3,12 ,3]




    =============Two pointer Technique===============

    ===psuedoCode===
    
    low = 0;
    high = len of nums -1
    index is gonna be zero
    containersAreas = [];
    
    while high is larger than low:
        currentheight = min(low , high)
        currentWidth = heights[low] - heights[high];
        currentContainerArea = currentHeight * currentWidth;
        append currentContainerArea to containersAreaList
        low+=1
        high -=1
    return max(currentContainerArea);


    ===Dry Run===


    [1,7,2,5,4,7,3,6]


    Iteration   low      high    value(currentLow)   value(currentHigh)    height      width     Area        containersArea
        0        0         8           1                       6              1          8         8            [8]
        1        1         6           7                       3              3          5         15           [8 , 15]
        2        2         5           2                       7              2          3          6           [8 ,15 , 6]
        3        3         4           5                       4              4          1          4           [8 , 15 , 6 ,4]

    if I move low and high for every iteration! it may skips the right 2 poles






    '''


    # containersAreas = [];
    # for i in range(len(heights)):
    #     for j in range(i + 1 , len(heights)):
    #         currentHeight =  min(heights[j] , heights[i]);
    #         currentWidth =  j - i;
    #         currentContainerArea = currentHeight * currentWidth;
    #         containersAreas.append(currentContainerArea)
            

    # return max(containersAreas);


    
    


    '''
    0    0    1      2     2      2     1    2   [2]
    1    0    2      2     5      2     2    4   [2,4]
    2    0    3      2     8      2     3    6   [2,4,6]
    3    1    2      2     5      2     1    2   [2,4,6,2]
    4    1    3      2     8      2     2    4   [2,3,6,2,4]
    5    2    3      5     8      5     1    5   [2,3,6,2,4,5]


    ===algorithm===
    choose two poles
    choose the pole with smallest height
    calculate the width between them.
    calculae the total area by multiplying width and height for each container

    Hashmap = {

    "2" : 0,
    "2": 1,
    "5" : 2,
    "8" : 3

    }

    How do i find the height and width to calculate the area of the containers so that its in o(n)  and don't miss the critical poles comparison


    ===dryRun===
    First Pass
    [2,2,5, 8]
    iteriaon     low        high        low[val]        high[val]       h       w       A       ContainersAreas
        0         0          3             2                8           2       3       6           [6]
        1         1          2             2                5           2       1       2           [6,2]
        2         
    Second Pass
    iteriaon     low        high        low[val]        high[val]       h       w       A       ContainersAreas
        0         1           3            2                8           2       2       4         [6,2,4]
        2         0           2            2                5           2       2       4          [6,2,4,4]



    ===dry run again===
    [2,2,5,8]
    iteriaon     low        high        low[val]        high[val]       h       w       A       ContainersAreas
        0         0           3            2                8           2       3       6           [6]
        1         1           3            2                8           2       2       4           [6,4]
        2         2           3            5                8           5       1       5           [6,4,5]

        Can I save the first Area in the target and then move pointer based on that target???????
    iteriaon     low        high        low[val]        high[val]       h       w       A       ContainersAreas   Target
        0         0           3             2               8           2       3       6             [6]           2
        1         1           3             2               8           2       2       4             [6,4]         6
        2         2           3             5               8           5       1       5             [6,4,5]       4


    [2,2,5,8]
    iteriaon     low        high        low[val]        high[val]       h       w       A       ContainersAreas  
        0         0           3            2                8           2       3       6           [6]
        1         1           3            2                8           2       2       4           [6,4]
        2         2           3            5                8           5       1       5           [6,4,5]


    [1,7,2,5,4,7,3,6]
    iteriaon     low        high        low[val]        high[val]       h       w       A       ContainersAreas  
        0         0           7             1               6           1       7       7               [7]
        1         1           7             7               6           6       6       36              [7,36]
        2         1           6             7               3           3       5       15              [7,36,15]
        3         1           5             7               7           7       4       28              [7,36,15,28]
        4         1           4             7               4           4       3       12              [7,36,15,28]
        5         1           3             7               5           5       2       10              [7,36,15,28]
        6         1           2             7               2           2       1        2              [7,36,15,28,2]

        ===pseudoCode===

        low is 0 
        high is len(heights) - 1
        index is 0


            while high is greater than lower:
                currentHeight = min(heights[low] , heights[high]);
                currentWidth = j - i;
                currentContainerArea = currentHeight * currentWidth;
                containersAreas -> append current area
                if heights[high] > heights[low]:
                    low += 1;
                else:
                    high -=1
                
            return containersAreas;

            


    '''
        
    # Implementation
    # heights.sort();
    # containersAreas = [];
    low = 0;
    high = len(heights) - 1;
    maximumArea = 0;
    
    while high > low:
        currentHeight = min(heights[low] , heights[high] );
        currentWidth = high - low;
        currentContainerArea = currentHeight * currentWidth;
        # containersAreas.append(currentContainerArea);
        maximumArea = max(maximumArea , currentContainerArea);
        if heights[high] > heights[low]:
            low +=1;
        else:
            high -=1;

    return maximumArea;

output = containerWithMostWater([1,7,2,5,4,7,3,6]);
print(f"Container with Most Water Area : {output} ")
