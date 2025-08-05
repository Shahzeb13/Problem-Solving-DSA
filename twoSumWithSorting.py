def twoSumWithSorting(nums , target):
    A = []
    for i, num in enumerate(nums):
        A.append([num, i])
    print(f"A : {A}")
    A.sort();
    print(f"A After Sorting based on Value : {A}")
    
    i = 0;
    j=len(A) - 1;
    print(f" I : {i} || j : {j}")

    while i < j:
        current = A[i][0] + A[j][0];
        print(f"Current : {current}");
        if current == target:
            return target;

        if current > target:
            j = j - 1;
        elif current < target:
            i = i + 1;
        

res = twoSumWithSorting([5 ,9 , 4, 1] , 10);
print(f"Result : {res}")


