


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








    '''


    containersAreas = [];
    for i in range(len(heights)):
        for j in range(i + 1 , len(heights)):
            currentHeight =  min(heights[j] , heights[i]);
            currentWidth =  j - i;
            currentContainerArea = currentHeight * currentWidth;
            containersAreas.append(currentContainerArea)
            

    return max(containersAreas);






output = containerWithMostWater([1,7,2,5,4,7,3,6]);
print(f"Container with Most Water Area : {output} ")
