

def containsDuplicate(nums):
    nums.sort();
    print(f"Sorted Num : {nums}");

    for i in range(1 , len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False;


res = containsDuplicate([2 , 3, 1 , 4 ,4])
res2 =  containsDuplicate([2 , 3, 1 , 4 ,5])
print(f" Has Duplicate : {res}");
print(f" Has Duplicate : {res2}");
