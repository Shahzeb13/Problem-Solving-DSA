def twoSumWithHashMap(nums , target):

    indexes = {};
    for i , num in enumerate(nums):
        indexes[num] = i;
    print(f"Indexes : {indexes}");

    for i ,num in enumerate(nums):
        difference = target - num;
        
        if difference in indexes and indexes[difference] != i:
            return [i, indexes[difference]]


res = twoSumWithHashMap([5 ,9 , 4, 1] , 10);
print(f"Result : {res}")
