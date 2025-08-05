

def containsDuplicate(nums):
    nums.sort();
    print(f"Sorted Num : {nums}");

    low = 0;
    high = len(nums) - 1;


    while high > low:
        if nums[low] == nums[high]:
            return True;
    
        if nums[low] != nums[high]:
            low = low + 1;

    return False




res = containsDuplicate([2 , 3, 1 , 4 ,4])
res2 =  containsDuplicate([2 , 3, 1 , 4 ,5])
print(f" Has Duplicate : {res}");
print(f" Has Duplicate : {res2}");
